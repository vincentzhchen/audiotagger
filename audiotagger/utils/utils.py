import os
from mutagen.easymp4 import MP4
from mutagen.mp4 import MP4Tags

import pandasdateutils as pdu
from audiotagger.core.paths import audiotagger_log_dir
from audiotagger.data.fields import Fields as fld


class AudioTaggerUtils(object):
    def __init__(self):
        pass

    @staticmethod
    def get_file_extension(path_to_some_file):
        filename, file_extension = os.path.splitext(path_to_some_file)
        return file_extension

    @staticmethod
    def is_m4a(path_to_some_file):
        file_extension = AudioTaggerUtils.get_file_extension(path_to_some_file)
        return True if file_extension == ".m4a" else False

    @staticmethod
    def is_mp3(path_to_some_file):
        file_extension = AudioTaggerUtils.get_file_extension(path_to_some_file)
        return True if file_extension == ".mp3" else False

    @staticmethod
    def is_wav(path_to_some_file):
        file_extension = AudioTaggerUtils.get_file_extension(path_to_some_file)
        return True if file_extension == ".wav" else False

    @staticmethod
    def is_flac(path_to_some_file):
        file_extension = AudioTaggerUtils.get_file_extension(path_to_some_file)
        return True if file_extension == ".flac" else False

    @staticmethod
    def is_ape(path_to_some_file):
        file_extension = AudioTaggerUtils.get_file_extension(path_to_some_file)
        return True if file_extension == ".ape" else False

    @staticmethod
    def filter_m4a_files(arg):
        if isinstance(arg, str):
            arg = [arg]

        return [x for x in arg if AudioTaggerUtils.is_m4a(x)]

    @staticmethod
    def apply_utf8(x):
        return x.encode("utf-8").decode("utf-8")

    @staticmethod
    def convert_to_mp4_obj(file_paths):
        return [MP4(path) for path in file_paths]

    @staticmethod
    def rename_columns(df):
        return df.rename(columns=fld.ID3_to_field)

    @staticmethod
    def filter_by_artist(df, artist):
        ret = df
        return ret.loc[df[fld.ARTIST] == artist]

    @staticmethod
    def metadata_to_tags(df_metadata):
        df_metadata[fld.TRACK_NUMBER] = df_metadata[
            [fld.TRACK_NO, fld.TOTAL_TRACKS]].apply(tuple, axis="columns")
        df_metadata[fld.DISC_NUMBER] = df_metadata[
            [fld.DISC_NO, fld.TOTAL_DISCS]].apply(tuple, axis="columns")
        df_metadata.drop([fld.TRACK_NO, fld.TOTAL_TRACKS,
                          fld.DISC_NO, fld.TOTAL_DISCS],
                         axis="columns", inplace=True)
        df_metadata[fld.YEAR] = df_metadata[fld.YEAR].astype(str)
        df_metadata = df_metadata.applymap(lambda x: [x])

        tag_dict = {}
        df_metadata.columns = [
            fld.field_to_ID3.get(c, c) for c in df_metadata.columns]
        metadata_dicts = df_metadata.to_dict(orient="records")
        for d in metadata_dicts:
            path = d.pop("PATH")[0]
            tags = MP4Tags()
            tags.update(d)
            tag_dict.update({path: tags})
        return tag_dict

    @staticmethod
    def traverse_directory(src):
        """Recursively traverses a directory.

        Notes:
            1. Returns all the leaves (file paths) in the directory tree.
            2. If the source is a file path, then return the source as a list.

        Args:
            src (str): Source directory in a list.

        Returns:
            all_file_paths (list): List of all leaf file paths.
        """

        # if src is a file path, then return it as a list
        if os.path.isfile(src):
            return [src]

        if not os.path.exists(src):
            raise ValueError(f"{src} does not exist.")

        # walk directory ree
        all_file_paths = []
        for root, dirs, files in os.walk(src):
            for file in files:
                file_path = os.path.join(root, file)
                all_file_paths.append(file_path)

        return all_file_paths

    @staticmethod
    def dry_run(df, prefix=None):
        out_file = os.path.join(audiotagger_log_dir(),
                                f"dry_run_{pdu.now(as_string=True)}.xlsx")
        if prefix is not None:
            out_file = os.path.join(audiotagger_log_dir(),
                                    prefix + "_" +
                                    f"dry_run_{pdu.now(as_string=True)}.xlsx")
        df.to_excel(out_file, index=False)
