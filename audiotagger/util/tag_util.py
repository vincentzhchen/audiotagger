from mutagen.mp4 import MP4Tags

from audiotagger.data.fields import Fields as fld


class TagUtil(object):
    def __init__(self):
        pass

    @classmethod
    def enforce_dtypes(cls, df, io_type):
        """Enforces the field type from input metadata dataframe.

        This implementation assumes that the column name is the same as
        the field variable name.

        """
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
            df = df.replace("nan", "")

        elif io_type == "OUTPUT_TYPE":
            for col in df:
                t = eval(f"fld.{col}.OUTPUT_TYPE")
                if t == "utf-8":
                    df[col] = df[col].str.encode("utf-8")
                else:
                    df[col] = df[col].astype(t)

        return df

    @classmethod
    def remove_non_metadata_fields_from_metadata_dict(cls, metadata_dict):
        """Removes custom fields from a metadata dict.

        The metadata dict is of the form {metadata_field: [value], ...}

        """
        for col in fld.CUSTOM_COLS:
            metadata_dict.pop(col, None)
        return metadata_dict

    @classmethod
    def dict_to_mp4tag(cls, d):
        """Convert python dictionary to MP4Tag object.

        """
        tags = MP4Tags()
        tags.update(d)
        return tags

    @classmethod
    def metadata_to_tags(cls, df):
        # only want to have tuples right before building the tag object
        df = TagUtil.build_track_and_disc_tuples(df=df)

        # convert to correct output data type
        df = TagUtil.enforce_dtypes(df=df, io_type="OUTPUT_TYPE")

        # put all values into a list for MP4Tags
        df = df.applymap(lambda x: [x])

        # convert all fields to ID3 values for MP4Tags
        df = df.rename(columns=fld.field_to_ID3)

        tag_dict = {}
        # generate the metadata tag dictionaries
        metadata_dicts = df.to_dict(orient="records")
        for d in metadata_dicts:
            path_src = d[fld.PATH_SRC.CID][0]
            d = TagUtil.remove_non_metadata_fields_from_metadata_dict(d)
            d = TagUtil.dict_to_mp4tag(d)
            tag_dict.update({path_src: d})
        return tag_dict

    @classmethod
    def split_track_and_disc_tuples(cls, df, drop_original=True):
        """Given a metadata dataframe, split any track / disc tuples.

        """
        part = lambda x: x[0]
        total = lambda x: x[1]

        if fld.TRACK_NO_TUPLE.CID in df.columns:
            df[fld.TRACK_NO.CID] = df[fld.TRACK_NO_TUPLE.CID].apply(part)
            df[fld.TOTAL_TRACKS.CID] = df[fld.TRACK_NO_TUPLE.CID].apply(total)

            if drop_original:
                df = df.drop(columns=fld.TRACK_NO_TUPLE.CID)

        if fld.DISC_NO_TUPLE.CID in df.columns:
            df[fld.DISC_NO.CID] = df[fld.DISC_NO_TUPLE.CID].apply(part)
            df[fld.TOTAL_DISCS.CID] = df[fld.DISC_NO_TUPLE.CID].apply(total)

            if drop_original:
                df = df.drop(columns=fld.DISC_NO_TUPLE.CID)

        return df

    @classmethod
    def build_track_and_disc_tuples(cls, df, drop_components=True):
        """Given a metadata dataframe, construct track / disc tuples.

        """
        if (fld.TRACK_NO.CID in df) and (fld.TOTAL_TRACKS.CID in df):
            df[fld.TRACK_NO_TUPLE.CID] = tuple(zip(
                df[fld.TRACK_NO.CID], df[fld.TOTAL_TRACKS.CID]))

            if drop_components:
                df = df.drop(columns=[fld.TRACK_NO.CID, fld.TOTAL_TRACKS.CID])

        if (fld.DISC_NO.CID in df) and (fld.TOTAL_DISCS.CID in df):
            df[fld.DISC_NO_TUPLE.CID] = tuple(zip(
                df[fld.DISC_NO.CID], df[fld.TOTAL_DISCS.CID]))

            if drop_components:
                df = df.drop(columns=[fld.DISC_NO.CID, fld.TOTAL_DISCS.CID])

        return df

    @classmethod
    def sort_metadata(cls, df):
        """Given a metadata dataframe, sort the dataframe.

        """
        df = df.sort_values(
            [fld.ALBUM_ARTIST.CID, fld.YEAR.CID, fld.ALBUM.CID,
             fld.DISC_NO.CID, fld.TRACK_NO.CID, fld.TITLE.CID])

        excess_cols = [c for c in df if c not in fld.BASE_METADATA_COLS]
        cols = fld.BASE_METADATA_COLS + excess_cols
        df = df[cols]
        return df
