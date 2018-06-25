from mutagen.easymp4 import MP4
from audiotagger.data.fields import Fields as fld


class AudioTaggerUtils(object):
    def __init__(self, logger):
        self.log = logger

    def apply_utf8(self, x):
        return x.encode("utf-8").decode("utf-8")

    def convert_to_audio_object(self, file_paths):
        return [MP4(path) for path in file_paths]

    def is_m4a(self, filename):
        return True if filename.split(".")[-1] == "m4a" else False

    def rename_columns(self, df):
        return df.rename(columns=fld.TAG_MAP)
