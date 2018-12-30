import os
import warnings
from mutagen.mp4 import MP4Tags
import pandasdateutils as pdu

from audiotagger.core.paths import audiotagger_log_dir
from audiotagger.data.fields import Fields as fld


class TagUtil(object):
    def __init__(self):
        pass

    @classmethod
    def rename_columns(cls, df):
        return df.rename(columns=fld.ID3_to_field)

    @classmethod
    # TODO: move this to a filter module / class
    def filter_by_artist(cls, df, artist):
        ret = df
        return ret.loc[df[fld.ARTIST.CID] == artist]

    @classmethod
    def clean_metadata(cls, df_metadata):
        df_metadata = TagUtil.rename_columns(df_metadata)

        # TODO: hack to drop cover since that fails UTF-8 encoding
        if "COVER" in df_metadata.columns:
            df_metadata = df_metadata.drop("COVER", axis="columns")

        # remove leading and trailing white spaces
        for col in df_metadata:
            t = eval(f"fld.{col}.INPUT_TYPE")
            if t == str:
                df_metadata[col] = df_metadata[col].str.strip()

        df_metadata = TagUtil.split_track_and_disc_tuples(df=df_metadata)
        return df_metadata

    @classmethod
    def enforce_dtypes(cls, df, io_type):
        # apply correct typing
        if io_type == "INPUT_FROM_AUDIO_FILE":
            for col in df:
                t = eval(f"fld.{col}.OUTPUT_TYPE")
                if t == "utf-8":
                    df[col] = df[col].str.decode("utf-8")
                df[col] = df[col].astype(eval(f"fld.{col}.INPUT_TYPE"))
            df = df.replace("nan", "")

        elif io_type == "INPUT_FROM_METADATA_FILE":
            for col in df:
                df[col] = df[col].astype(eval(f"fld.{col}.INPUT_TYPE"))

        elif io_type == "OUTPUT_TYPE":
            for col in df:
                t = eval(f"fld.{col}.OUTPUT_TYPE")
                if t == "utf-8":
                    df[col] = df[col].str.encode("utf-8")
                else:
                    df[col] = df[col].astype(t)

        return df

    @classmethod
    def metadata_to_tags(cls, df_metadata):
        # only want to have tuples right before building the tag object
        df_metadata = TagUtil.build_track_and_disc_tuples(df=df_metadata)

        # convert to correct output data type
        df_metadata = TagUtil.enforce_dtypes(df=df_metadata,
                                             io_type="OUTPUT_TYPE")

        # put all values into a list for MP4Tags
        df_metadata = df_metadata.applymap(lambda x: [x])

        # convert all fields to ID3 values for MP4Tags
        df_metadata.columns = [fld.field_to_ID3.get(c, c) for c in df_metadata]

        tag_dict = {}
        # generate the metadata tag dictionaries
        metadata_dicts = df_metadata.to_dict(orient="records")
        for d in metadata_dicts:
            path = d.pop(fld.PATH.CID)[0]
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
    def split_track_and_disc_tuples(cls, df, drop_original=True):
        if fld.TRACK_NO_TUPLE.CID in df.columns:
            df[fld.TRACK_NO.CID] = df[fld.TRACK_NO_TUPLE.CID].apply(
                lambda x: x[0])
            df[fld.TOTAL_TRACKS.CID] = df[fld.TRACK_NO_TUPLE.CID].apply(
                lambda x: x[1])
            if drop_original:
                df = df.drop(fld.TRACK_NO_TUPLE.CID, axis="columns")

        if fld.DISC_NO_TUPLE.CID in df.columns:
            df[fld.DISC_NO.CID] = df[fld.DISC_NO_TUPLE.CID].apply(
                lambda x: x[0])
            df[fld.TOTAL_DISCS.CID] = df[fld.DISC_NO_TUPLE.CID].apply(
                lambda x: x[1])
            if drop_original:
                df = df.drop(fld.DISC_NO_TUPLE.CID, axis="columns")

        return df

    @classmethod
    def build_track_and_disc_tuples(cls, df, drop_components=True):
        if (fld.TRACK_NO.CID in df) and (fld.TOTAL_TRACKS.CID in df):
            df[fld.TRACK_NO_TUPLE.CID] = df[
                [fld.TRACK_NO.CID, fld.TOTAL_TRACKS.CID]
            ].apply(tuple, axis="columns")
            if drop_components:
                df.drop([fld.TRACK_NO.CID, fld.TOTAL_TRACKS.CID],
                        axis="columns", inplace=True)

        if (fld.DISC_NO.CID in df) and (fld.TOTAL_DISCS.CID in df):
            df[fld.DISC_NO_TUPLE.CID] = df[
                [fld.DISC_NO.CID, fld.TOTAL_DISCS.CID]
            ].apply(tuple, axis="columns")
            if drop_components:
                df.drop([fld.DISC_NO.CID, fld.TOTAL_DISCS.CID],
                        axis="columns", inplace=True)
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

    @classmethod
    def sort_metadata(cls, df_metadata):
        df_metadata = df_metadata.sort_values(
            [fld.ALBUM_ARTIST.CID, fld.YEAR.CID, fld.ALBUM.CID, fld.DISC_NO.CID,
             fld.TRACK_NO.CID, fld.TITLE.CID])

        excess_cols = [c for c in df_metadata if
                       c not in fld.BASE_METADATA_COLS]
        cols = fld.BASE_METADATA_COLS + excess_cols
        df_metadata = df_metadata[cols]
        return df_metadata

    @classmethod
    def save_tags_to_file(cls, df_metadata, logger=None):
        tag_dict = TagUtil.metadata_to_tags(df_metadata=df_metadata)
        for k in tag_dict:
            if logger is not None:
                logger.info(f"Saving {tag_dict[k]} to {k}")
            tag_dict[k].save(k)
