import os
import pandas as pd
from audiotagger.utils.utils import AudioTaggerUtils


class AudioTaggerInput(object):
    def __init__(self, root, logger):
        self.log   = logger
        self.root  = root
        self.utils = AudioTaggerUtils(logger=logger)

        # load inputs
        self._load_all_file_paths()
        self._load_all_audio_files()

    def _filter_by_artist(self, df, artist):
        df = df[df["ARTIST"] == artist]
        return df

    def is_apple_file(self, filename):
        return filename.endswith("m4a")

    def _load_all_file_paths(self):
        """
        Loads all the file paths from a given root directory.
        """
        self.log.info("Loading all audio file paths...")
        # x = (root, dirs, files) | x[0] = root, x[1] = dirs, x[2] = files


    def _load_all_audio_files(self):
        """
        Load all audio file objects from an initialized list of file paths.
        """
        self.log.info("Loading all audio files...")
        all_audio_files = self.utils.convert_to_audio_object(self.all_audio_file_paths)
        # df = []
        # for song in all_audio_files:
        #     df.append(pd.DataFrame(dict(song.tags, **{"SONG": [song]})))
        # all_audio_files = pd.concat(df)
        all_audio_files = [dict(song.tags, **{"SONG": [song]}) for song in all_audio_files]
        all_audio_files = pd.DataFrame(all_audio_files)
        all_audio_files = self.utils.rename_columns(all_audio_files)
        self.all_audio_files = all_audio_files

    def view_loaded_audio(self):
        df = pd.concat([pd.DataFrame(dict(song.tags)) for song in self.all_audio_files])
        self.log.log_dataframe(df)

    def get_all_audio(self):
        return self.all_audio_files

    def get_all_audio_filtered_by_artist(self, artist):
        return self._filter_by_artist(df=self.all_audio_files, artist=artist)

    def write_to_excel(self, filepath):
        """
        Writes input data to Excel for debugging.

        :param filepath: output filepath to write the data to
        """
        self.log.info("Saving initial audio tags to Excel...")
        writer = pd.ExcelWriter(filepath, date_format="YYYY-MM-DD", datetime_format="YYYY-MM-DD")

        for m in dir(self):
            if "__" not in m:
                attr = getattr(self, m)
                if attr.__class__ == pd.DataFrame and not attr.empty:
                    self.log.info("Saving {} in Excel".format(m))
                    attr.to_excel(writer, sheet_name=m, index=False, encoding="utf-8")

        writer.save()

    def write_to_csv(self, filepath):
        for m in dir(self):
            if "__" not in m:
                attr = getattr(self, m)
                if attr.__class__ == pd.DataFrame and not attr.empty:
                    self.log.info("Saving {} in Excel".format(m))
                    attr.to_csv(filepath, index=False)