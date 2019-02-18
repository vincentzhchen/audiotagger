import os
import warnings
from mutagen.mp4 import MP4Tags, MP4Cover

from audiotagger.data.fields import Fields as fld


def enforce_dtypes(df, io_type):
    """Enforces the field type from input metadata dataframe.

    This implementation assumes that the column name is the same as
    the field variable name.

    """
    if io_type == "INPUT_FROM_AUDIO_FILE":
        missing_fields = [c for c in df if c not in fld.field_to_ID3.keys()]
        if len(missing_fields) > 0:
            warnings.warn(f"THESE FIELDS do not exist... {missing_fields} "
                          f"... removing them to continue.")
            cols = [c for c in df if c not in fld.field_to_ID3.keys()]
            df = df.drop(columns=cols)

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
            elif t is None:
                continue
            else:
                df[col] = df[col].astype(t)

    return df


def remove_non_metadata_fields_from_metadata_dict(metadata_dict):
    """Removes custom fields from a metadata dict.

    The metadata dict is of the form {metadata_field: [value], ...}

    """
    for col in fld.CUSTOM_COLS:
        metadata_dict.pop(col, None)
    return metadata_dict


def dict_to_mp4tag(d):
    """Convert python dictionary to MP4Tag object.

    """
    tags = MP4Tags()
    tags.update(d)
    return tags


def metadata_to_tags(df):
    # only want to have tuples right before building the tag object
    df = build_track_and_disc_tuples(df=df)

    # convert to correct output data type
    df = enforce_dtypes(df=df, io_type="OUTPUT_TYPE")

    # put all values into a list for MP4Tags
    df = df.applymap(lambda x: [x])

    # convert all fields to ID3 values for MP4Tags
    df = df.rename(columns=fld.field_to_ID3)

    tag_dict = {}
    # generate the metadata tag dictionaries
    metadata_dicts = df.to_dict(orient="records")
    for d in metadata_dicts:
        # TODO: remove empty covers
        if d.get(fld.COVER.ID3, None)[0] is None:
            d.pop(fld.COVER.ID3, None)
        path_src = d[fld.PATH_SRC.CID][0]
        d = remove_non_metadata_fields_from_metadata_dict(d)
        d = dict_to_mp4tag(d)
        tag_dict.update({path_src: d})
    return tag_dict


def split_track_and_disc_tuples(df, drop_original=True):
    """Given a metadata dataframe, split any track / disc tuples.

    """
    part = lambda x: x[0] if isinstance(x, tuple) else x
    total = lambda x: x[1] if isinstance(x, tuple) else x

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


def build_track_and_disc_tuples(df, drop_components=True):
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


def sort_metadata(df):
    """Given a metadata dataframe, sort the dataframe.

    """
    df = df.sort_values(
        [fld.ALBUM_ARTIST.CID, fld.YEAR.CID, fld.ALBUM.CID,
         fld.DISC_NO.CID, fld.TRACK_NO.CID, fld.TITLE.CID])

    excess_cols = [c for c in df if c not in fld.BASE_METADATA_COLS]
    cols = fld.BASE_METADATA_COLS + excess_cols
    df = df[cols]
    return df


def generate_cover_art_path(df):
    """Generate cover art file paths.

    Notes:
        The paths are generated assuming that all albums have a "cover.jpg"
        file in the same directory level as the audio files.  Invalid paths
        will be generated if the image file does not exist.

    Args:
        df (dataframe): Metadata dataframe.

    Returns:
        anonymous (dataframe): Returns dataframe with cover art paths.
    """
    def _generate_album_art_path(path):
        dir = os.path.dirname(path)
        jpg_path = os.path.join(dir, "cover.jpg")
        return jpg_path

    df[fld.COVER_SRC.CID] = df[fld.PATH_SRC.CID].apply(
        _generate_album_art_path)

    df[fld.COVER_DST.CID] = df[fld.PATH_DST.CID].apply(
        _generate_album_art_path)

    return df


def construct_cover_object(df):
    """Construct all MP4Cover objects.

    Notes:
        If the cover source column exists but there is no valid source,
        the cover object column will be NULL.

    Args:
        df (dataframe): Metadata dataframe.

    Returns:
        anonymous (dataframe): Returns a dataframe with potentially
            constructed cover object.
    """
    def construct_mutagen_mp4_cover(path):
        # return None if there is no path or the path doesnt exist
        if path is "" or not os.path.exists(path):
            return None

        with open(path, "rb") as f:
            cover_byte_str = f.read()
        return MP4Cover(cover_byte_str)

    # make a temporary column to decide what to use
    df["TMP_COVER"] = df[fld.COVER_SRC.CID].apply(construct_mutagen_mp4_cover)

    # if cover tag exists, and there is no cover file, keep original metadata
    # otherwise take potential cover from cover file
    if fld.COVER.CID in df:
        df[fld.COVER.CID] = df["TMP_COVER"].where(
            df["TMP_COVER"].notnull(), df[fld.COVER.CID])
    else:
        df[fld.COVER.CID] = df["TMP_COVER"]

    df = df.drop(columns="TMP_COVER")
    return df
