import os
import pandas as pd

import pandasdateutils as pdu
from audiotagger.data.fields import Fields as fld
from audiotagger.settings import settings as settings
from audiotagger.util import file_util as futil
from audiotagger.util import input_output_util as ioutil
from audiotagger.util import tag_util as tutil


class AudioTaggerInput(object):
    def __init__(self, src, logger, options):
        if src is None:
            raise Exception("INVALID SOURCE")
        else:
            self.src = src

        self.log = logger
        self.options = options

        # for Excel metadata files
        if futil.is_xlsx(self.src):
            if not os.path.exists(self.src):
                raise ValueError(f"{self.src} does not exist.")

            # load inputs
            self._load_all_m4a_files_into_df_from_excel()

        # for directory of audio files or a single audio file
        elif os.path.isdir(self.src) or os.path.isfile(self.src):
            if not os.path.exists(self.src):
                raise ValueError(f"{self.src} does not exist.")

            # load inputs
            self._load_all_m4a_files_into_df_from_path()

        else:
            raise Exception("INVALID SOURCE")

        self.metadata = tutil.sort_metadata(self.metadata)

        if self.options.write_to_excel:
            base_dir = settings.LOG_DIRECTORY
            file_path = os.path.join(
                base_dir, f"input_{pdu.now(as_string=True)}.xlsx")
            # choose to not write cover byte string into file
            metadata = self.metadata.drop(
                columns=fld.COVER.CID, errors="ignore")
            ioutil.write_to_excel(df=metadata, file_path=file_path)
            self.log.info(f"Saved input metadata to {file_path}")

    def _load_all_m4a_files_into_df_from_excel(self):
        metadata = pd.read_excel(self.src, sheet_name="metadata", dtype=str)
        metadata = tutil.enforce_dtypes(df=metadata,
                                        io_type="INPUT_FROM_METADATA_FILE")
        self.metadata = metadata

    def _load_all_m4a_files_into_df_from_path(self):
        """Load metadata from m4a files into a dataframe.

        """
        m4a_file_paths = futil.traverse_directory(self.src, "m4a")
        self.log.info(f"LOADED {len(m4a_file_paths)} file paths.")

        metadata_records = futil.generate_metadata_records(m4a_file_paths)
        self.log.info(f"LOADED {len(metadata_records)} records.")

        metadata = pd.DataFrame(metadata_records)
        metadata = metadata.rename(columns={"PATH_SRC": fld.PATH_SRC.CID,
                                            "PATH_DST": fld.PATH_DST.CID, })
        self.log.info(f"LOADED raw metadata df, shape: {metadata.shape}.")

        metadata = metadata.rename(columns=fld.ID3_to_field)
        skip_cols = [c for c in metadata if c not in fld.ID3_to_field.values()]
        if skip_cols:
            self.log.info(f"SKIPPED these fields: {skip_cols}.")
        existing_cols = [c for c in metadata if c in fld.ID3_to_field.values()]
        metadata = metadata[existing_cols]

        # flatten list metadata records; missing values are NaN from pandas
        metadata = metadata.applymap(
            lambda x: x[0] if not isinstance(x, float) else x)
        self.log.debug(f"Flattened list metadata records.")

        metadata = tutil.split_track_and_disc_tuples(df=metadata)
        self.log.debug(f"Split track and disc tuples.")

        # TODO: hack to fill missing disc numbers
        metadata[fld.DISC_NO.CID].fillna(1, inplace=True)
        metadata[fld.TOTAL_DISCS.CID].fillna(1, inplace=True)

        metadata = tutil.enforce_dtypes(df=metadata,
                                        io_type="INPUT_FROM_AUDIO_FILE")
        self.log.debug(f"Enforced data types.")

        # if missing base metadata col, add it back
        missing = [c for c in fld.BASE_METADATA_COLS if c not in metadata]
        for c in missing:
            self.log.debug(f"{c} is a missing base metadata column -- setting "
                           f"it with empty string.")
            metadata[c] = ""  # everything is str except for disc and track no.

        self.metadata = metadata

    def get_metadata(self):
        """Get cleaned metadata.

        All cleaning should be done at instantiation.  Do not modify here.

        """
        df = self.metadata
        return df
