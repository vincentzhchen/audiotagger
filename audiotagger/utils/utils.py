from mutagen.easymp4 import MP4
from audiotagger.data.fields import Fields as fld


class AudioTaggerUtils(object):
    def __init__(self):
        pass

    @staticmethod
    def apply_utf8(x):
        return x.encode("utf-8").decode("utf-8")

    @staticmethod
    def convert_to_m4a(file_paths):
        return [(path, MP4(path)) for path in file_paths]

    @staticmethod
    def is_m4a(filename):
        return True if filename.split(".")[-1] == "m4a" else False

    @staticmethod
    def rename_columns(df):
        return df.rename(columns=fld.ID3_to_field)

    @staticmethod
    def filter_by_artist(df, artist):
        ret = df
        return ret.loc[df[fld.ARTIST] == artist]
