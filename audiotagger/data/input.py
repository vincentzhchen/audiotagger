import os
import pandas as pd

from audiotagger.data.fields import Fields as fld
from audiotagger.utils.utils import FileUtils, TagUtils


class AudioTaggerInput(object):
    def __init__(self, src, logger, xl_input_file=None, is_dry_run=False):
        self.log = logger
        self.src = src
        self.is_dry_run = is_dry_run

        if self.src is None and xl_input_file is None:
            raise ValueError("Must include root directory "
                             "containing audio files.")

        if xl_input_file is not None:
            self.read_from_excel(file_path=xl_input_file)
            return

        # load inputs
        self._load_all_audio_file_paths()
        self._load_all_m4a_tuples()
        self._load_all_audio_files_into_df()

    def _load_all_file_paths(self):
        """Loads all file paths in the given root directory.

        The files can be of any kind (e.g. text, xlsx, ...) and not
        just audio files (m4a, mp3, flac, ...) at this point.

        """
        self.log.info("Loading all file paths...")
        self.all_file_paths = FileUtils.traverse_directory(self.src)
        self.log.info(f"LOADED {len(self.all_file_paths)} file paths.")

    def _load_all_audio_file_paths(self):
        """Loads all audio file paths into memory.

        """
        self._load_all_file_paths()
        self.all_audio_file_paths = []

        # M4A
        m4a_file_paths = FileUtils.filter_m4a_files(self.all_file_paths)
        if m4a_file_paths:
            self.log.info("Loading all m4a file paths...")
            self.m4a_file_paths = m4a_file_paths
            self.log.info(f"LOADED {len(self.m4a_file_paths)} m4a file paths.")
            self.all_audio_file_paths += m4a_file_paths

    def _load_all_m4a_tuples(self):
        """Loads all m4a file paths into memory.

        The file path is used to create an MP4 object and is stored
        as a (file_path, MP4 obj) tuple.

        """
        self.log.info("Loading all m4a objects...")
        self.m4a_obj = FileUtils.convert_to_mp4_obj(self.m4a_file_paths)
        self.log.info(f"LOADED {len(self.m4a_obj)} m4a objects.")

    def _load_all_audio_files_into_df(self):
        """Load all audio file into a dataframe.

        The actual audio object is stored into the dataframe as well (in
        the "SONG" column.

        """
        self.log.info("Loading all audio file metadata into dataframe...")
        all_audio_obj = []
        all_audio_obj += self.m4a_obj  # add flac / mp3/ etc. here
        all_audio_obj = [dict(song.tags, **{"PATH": [song.filename]})
                         for song in all_audio_obj]
        metadata = pd.DataFrame(all_audio_obj)
        metadata = TagUtils.rename_columns(metadata)

        # TODO: hack to drop cover since that fails UTF-8 encoding
        if "COVER" in metadata.columns:
            metadata = metadata.drop("COVER", axis="columns")

        # metadata = metadata.applymap(lambda x: x.encode('unicode_escape').
        #                              decode('utf-8') if isinstance(x,
        #                                                            str) else x)

        f = lambda x: x[0] if isinstance(x, list) else x
        metadata = metadata.applymap(f)

        metadata = TagUtils.split_track_and_disc_tuples(df=metadata)
        metadata = metadata.drop([fld.TRACK_NUMBER, fld.DISC_NUMBER],
                                 axis="columns")
        self.metadata = metadata

    def get_all_audio_file_paths(self):
        return self.all_audio_file_paths

    def get_metadata(self):
        df = TagUtils.enforce_dtypes(self.metadata)
        return df

    def read_from_excel(self, file_path):
        df = pd.read_excel(file_path)
        self.metadata = df

    def write_to_excel(self, file_path):
        """
        Writes input data to Excel for debugging.

        Args:
            file_path (str): output file_path to write the data to.

        """
        writer = pd.ExcelWriter(file_path,
                                date_format="YYYY-MM-DD",
                                datetime_format="YYYY-MM-DD")

        for m in dir(self):
            if "__" not in m:
                attr = getattr(self, m)
                if attr.__class__ == pd.DataFrame and not attr.empty:
                    self.log.info(f"Saving [{m}] to Excel.")
                    attr.to_excel(writer, sheet_name=m, index=False,
                                  encoding="utf-8")

        writer.save()
        self.log.info(f"Compiled input data saved in {file_path}")
        return
