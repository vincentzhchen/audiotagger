import os
from mutagen.easymp4 import MP4
from mutagen.mp4 import MP4Tags

import pandasdateutils as pdu
from audiotagger.core.paths import audiotagger_log_dir
from audiotagger.data.fields import Fields as fld


class FileUtils(object):
    def __init__(self):
        pass

    @classmethod
    def get_file_extension(cls, path_to_some_file):
        filename, file_extension = os.path.splitext(path_to_some_file)
        return file_extension

    @classmethod
    def is_m4a(cls, path_to_some_file):
        file_extension = FileUtils.get_file_extension(path_to_some_file)
        return True if file_extension == ".m4a" else False

    @classmethod
    def is_mp3(cls, path_to_some_file):
        file_extension = FileUtils.get_file_extension(path_to_some_file)
        return True if file_extension == ".mp3" else False

    @classmethod
    def is_wav(cls, path_to_some_file):
        file_extension = FileUtils.get_file_extension(path_to_some_file)
        return True if file_extension == ".wav" else False

    @classmethod
    def is_flac(cls, path_to_some_file):
        file_extension = FileUtils.get_file_extension(path_to_some_file)
        return True if file_extension == ".flac" else False

    @classmethod
    def is_ape(cls, path_to_some_file):
        file_extension = FileUtils.get_file_extension(path_to_some_file)
        return True if file_extension == ".ape" else False

    @classmethod
    def filter_m4a_files(cls, arg):
        if isinstance(arg, str):
            arg = [arg]

        return [x for x in arg if FileUtils.is_m4a(x)]

    @classmethod
    def apply_utf8(cls, x):
        return x.encode("utf-8").decode("utf-8")

    @classmethod
    def convert_to_mp4_obj(cls, file_paths):
        return [MP4(path) for path in file_paths]

    @classmethod
    def traverse_directory(cls, src):
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

    @classmethod
    def is_xlsx(cls, path_to_some_file):
        """Checks if a file is an Excel (.xlsx) file.

        Args:
            path_to_some_file (str): Path to the file.

        Returns:
            Returns True if the file is an xlsx file else False.
        """
        file_extension = FileUtils.get_file_extension(path_to_some_file)
        return True if file_extension == ".xlsx" else False


class TagUtils(object):
    def __init__(self):
        pass

    @classmethod
    def rename_columns(cls, df):
        return df.rename(columns=fld.ID3_to_field)

    @classmethod
    def filter_by_artist(cls, df, artist):
        ret = df
        return ret.loc[df[fld.ARTIST.CID] == artist]

    @classmethod
    def clean_metadata(cls, df_metadata):
        df_metadata = TagUtils.rename_columns(df_metadata)

        # TODO: hack to drop cover since that fails UTF-8 encoding
        if "COVER" in df_metadata.columns:
            df_metadata = df_metadata.drop("COVER", axis="columns")

        # mutagen stores ratings as a byte; maintain this
        if fld.RATING in df_metadata.columns:
            df_metadata[fld.RATING.CID].fillna(bytes(0), inplace=True)

        df_metadata = TagUtils.split_track_and_disc_tuples(df=df_metadata)
        return df_metadata

    @classmethod
    def metadata_to_tags(cls, df_metadata):
        df_metadata[fld.TRACK_NUMBER.CID] = df_metadata[
            [fld.TRACK_NO.CID, fld.TOTAL_TRACKS.CID]].apply(tuple, axis="columns")
        df_metadata[fld.DISC_NUMBER.CID] = df_metadata[
            [fld.DISC_NO.CID, fld.TOTAL_DISCS.CID]].apply(tuple, axis="columns")
        df_metadata.drop([fld.TRACK_NO.CID, fld.TOTAL_TRACKS.CID,
                          fld.DISC_NO.CID, fld.TOTAL_DISCS.CID],
                         axis="columns", inplace=True)
        df_metadata[fld.YEAR.CID] = df_metadata[fld.YEAR.CID].astype(str)

        # apply correct typing
        for col in df_metadata:
            t = eval(f"fld.{col}.OUTPUT_TYPE")
            if t == "utf-8":
                df_metadata[col] = df_metadata[col].apply(
                    lambda x: x.encode("utf-8"))
            else:
                df_metadata[col] = df_metadata[col].astype(t)
        df_metadata = df_metadata.replace("nan", "")

        # put all values back into a list for MP4Tags
        df_metadata = df_metadata.applymap(lambda x: [x])

        # convert all fields back to ID3 values for MP4Tags
        df_metadata.columns = [
            fld.field_to_ID3.get(c, c) for c in df_metadata.columns]

        tag_dict = {}
        # generate the metadata tag dictionaries
        metadata_dicts = df_metadata.to_dict(orient="records")
        for d in metadata_dicts:
            path = d.pop(fld.PATH.CID)[0]
            # do not include this field if the rating is 0
            if d[fld.RATING.ID3] == [bytes(0)]:
                d.pop(fld.RATING.ID3)
            tags = MP4Tags()
            tags.update(d)
            tag_dict.update({path: tags})
        return tag_dict

    @classmethod
    def dry_run(cls, df, prefix=None):
        # TODO: this may not be something to abstract as each
        #       implementation's dry run is not the same
        out_file = os.path.join(audiotagger_log_dir(),
                                f"dry_run_{pdu.now(as_string=True)}.xlsx")
        if prefix is not None:
            out_file = os.path.join(audiotagger_log_dir(),
                                    prefix + "_" +
                                    f"dry_run_{pdu.now(as_string=True)}.xlsx")
        df.to_excel(out_file, index=False)

    @classmethod
    def split_track_and_disc_tuples(cls, df):
        if fld.TRACK_NUMBER.CID in df.columns:
            df[fld.TRACK_NO.CID] = df[fld.TRACK_NUMBER.CID].apply(
                lambda x: x[0])
            df[fld.TOTAL_TRACKS.CID] = df[fld.TRACK_NUMBER.CID].apply(
                lambda x: x[1])
            df = df.drop(fld.TRACK_NUMBER.CID, axis="columns")

        if fld.DISC_NUMBER.CID in df.columns:
            df[fld.DISC_NO.CID] = df[fld.DISC_NUMBER.CID].apply(
                lambda x: x[0])
            df[fld.TOTAL_DISCS.CID] = df[fld.DISC_NUMBER.CID].apply(
                lambda x: x[1])
            df = df.drop(fld.DISC_NUMBER.CID, axis="columns")

        return df

    @classmethod
    def flatten_list_values(cls, df_metadata):
        """Takes the first element of all list objects in dataframe.

        Args:
            df_metadata (dataframe): A metadata dataframe from parsing
                audio files.

        Returns:
            anonymous (dataframe): Returns the metadata dataframe with
                no list objects in the cells.
        """
        f = lambda x: x[0] if isinstance(x, list) else x
        df_metadata = df_metadata.applymap(f)

        return df_metadata
