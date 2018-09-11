import os
import pandas as pd
from audiotagger.utils.utils import AudioTaggerUtils


class AudioTaggerInput(object):
    def __init__(self, root, logger, xl_input_file=None):
        self.log = logger
        self.root = root
        self.utils = AudioTaggerUtils()

        # load inputs
        self._load_all_file_paths()
        self._load_all_m4a_files()
        self._load_all_audio_files_into_df()

    def _load_all_file_paths(self):
        """Loads all file paths in the given root directory.

        """
        self.log.info("Loading all file paths...")
        all_file_paths = []
        for root, dirs, files in os.walk(self.root):
            for file in files:
                file_path = os.path.join(root, file)
                all_file_paths.append(file_path)
        self.all_file_paths = all_file_paths
        self.log.info("LOADED {} file paths.".format(len(self.all_file_paths)))

        self._load_all_audio_file_paths()

    def _load_all_audio_file_paths(self):
        """Loads all audio file paths into memory.

        """
        self.all_audio_file_paths = []

        # M4A
        m4a_file_paths = [x for x in self.all_file_paths if x.endswith(".m4a")]
        if m4a_file_paths:
            self.m4a_file_paths = m4a_file_paths
            self.log.info("LOADED {} m4a file paths."
                          .format(len(self.m4a_file_paths)))
            self.all_audio_file_paths += m4a_file_paths

    def _load_all_m4a_files(self):
        """Loads all m4a file paths into memory.

        """
        self.log.info("Loading all m4a objects...")
        self.m4a_obj = self.utils.convert_to_m4a(self.m4a_file_paths)
        self.log.info("LOADED {} m4a objects.".format(len(self.m4a_obj)))

    def _load_all_audio_files_into_df(self):
        """Load all audio file into a dataframe.

        The actual audio object is stored into the dataframe as well (in
        the "SONG" column.

        """
        self.log.info("Loading all audio file metadata into dataframe...")
        all_audio_obj = []
        all_audio_obj += self.m4a_obj  # add flac / mp3/ etc. here
        all_audio_obj = [
            dict(song.tags, **{"SONG": [song]}) for song in all_audio_obj]
        metadata = pd.DataFrame(all_audio_obj)
        metadata = self.utils.rename_columns(metadata)
        self.metadata = metadata

    def get_all_audio_file_paths(self):
        return self.all_audio_file_paths

    def get_metadata(self):
        return self.metadata

    def write_to_excel(self, filepath):
        """
        Writes input data to Excel for debugging.

        :param filepath: output filepath to write the data to
        """
        self.log.info("Saving initial audio tags to Excel...")
        writer = pd.ExcelWriter(filepath, date_format="YYYY-MM-DD",
                                datetime_format="YYYY-MM-DD")

        for m in dir(self):
            if "__" not in m:
                attr = getattr(self, m)
                if attr.__class__ == pd.DataFrame and not attr.empty:
                    self.log.info("Saving {} in Excel".format(m))
                    attr.to_excel(writer, sheet_name=m, index=False,
                                  encoding="utf-8")

        writer.save()
        return
