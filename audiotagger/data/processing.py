# SPDX-License-Identifier: GPL-3.0-or-later
"""Process loaded data here.

"""
from audiotagger.data import fields as fld
from audiotagger.util import (audiotagger_logger, tag_util as tutil)


class RawDataProcessor():
    """For cleaning up data per metadata structure requirements.

    There should be a different processor for different types of
    loaded data (e.g. data loaded from an m4a needs to be processed
    differently than data loaded from a metadata file).

    """

    def __init__(self, logger=None):
        self.logger = logger if (
            logger is not None) else audiotagger_logger.get_logger()

    def process_loaded_m4a_data(self, metadata):
        """Assumes metadata is from m4a file.

        """
        metadata = self._rename_raw_columns(metadata)
        metadata = self._clean_data(metadata)
        metadata = self._enforce_dtypes(metadata)
        metadata = tutil.sort_metadata(metadata)
        return metadata

    def process_loaded_metadatafile_data(self, metadata):
        # pylint: disable=invalid-name
        """Assumes metadata is from cleaned metadata file.

        Since the data has already been processed into the correct
        format, there should be minimal work to be done here.

        """
        metadata = self._enforce_dtypes(metadata)
        metadata = tutil.sort_metadata(metadata)
        return metadata

    def _rename_raw_columns(self, metadata):
        """Conform raw tag names to audiotagger fields.

        """
        metadata = metadata.rename(columns=fld.TO_FIELD)
        skip_cols = [c for c in metadata if c not in fld.TO_FIELD.values()]
        if skip_cols:
            self.logger.info("SKIPPED these fields: %s.", skip_cols)
        existing_cols = [c for c in metadata if c in fld.TO_FIELD.values()]
        metadata = metadata[existing_cols]
        return metadata

    def _clean_data(self, metadata):
        """Standard processing applied to loaded audio file data.

        All default values are set here as well.

        """
        # flatten list metadata records; missing values are NaN from pandas
        metadata = metadata.applymap(lambda x: x[0]
                                     if not isinstance(x, float) else x)
        self.logger.debug("Flattened list metadata records.")

        metadata = tutil.split_track_and_disc_tuples(df=metadata)
        self.logger.debug("Split track and disc tuples.")

        metadata = self._guarantee_base_metadata_cols(metadata)

        # these values cannot be NULL
        metadata[fld.TRACK_NO.CID].fillna(1, inplace=True)
        metadata[fld.TOTAL_TRACKS.CID].fillna(1, inplace=True)
        metadata[fld.DISC_NO.CID].fillna(1, inplace=True)
        metadata[fld.TOTAL_DISCS.CID].fillna(1, inplace=True)
        return metadata

    def _enforce_dtypes(self, metadata):
        """dtype enforcement assumes input has valid values.

        For example, if the disc number is a NoneType or NaN, it will
        fail to enforce to int.  Fill this before hand.

        """
        metadata = tutil.enforce_dtypes(df=metadata,
                                        io_type="INPUT_FROM_AUDIO_FILE")
        self.logger.debug("Enforced data types.")
        return metadata

    def _guarantee_base_metadata_cols(self, metadata):
        """Set default values here and include missing metadata.

        """
        # if missing base metadata col, add it back
        missing = (c for c in fld.BASE_METADATA_COLS if c not in metadata)
        for c in missing:
            # TODO: make this a constant field
            if c in [
                    fld.TRACK_NO.CID, fld.TOTAL_TRACKS.CID, fld.DISC_NO.CID,
                    fld.TOTAL_DISCS.CID
            ]:
                self.logger.debug(
                    "%s is a missing base metadata column -- "
                    "setting it with 1.", c)
                metadata[c] = 1
            else:
                self.logger.debug(
                    "%s is a missing base metadata column -- "
                    "setting it with empty string.", c)
                # everything is str except for disc and track no.
                metadata[c] = ""

        return metadata
