class Fields(object):
    # PATH COLS
    PATH_SRC = type(
        "PATH_SRC", (),
        {
            "ID3": "PATH_SRC",
            "CID": "PATH_SRC",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": str
        }
    )

    PATH_DST = type(
        "PATH_DST", (),
        {
            "ID3": "PATH_DST",
            "CID": "PATH_DST",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": str
        }
    )

    PATH_COLS = [PATH_SRC.CID, PATH_DST.CID]

    # COVER COLS
    COVER_SRC = type(
        "COVER_SRC", (),
        {
            "ID3": "COVER_SRC",
            "CID": "COVER_SRC",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": str
        }
    )

    COVER_DST = type(
        "COVER_DST", (),
        {
            "ID3": "COVER_DST",
            "CID": "COVER_DST",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": str
        }
    )

    COVER = type(
        "COVER", (),
        {
            "ID3": "covr",
            "CID": "COVER",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": None
        }
    )

    COVER_COLS = [COVER_SRC.CID, COVER_DST.CID, COVER.CID]

    # BASE METADATA COLS
    TITLE = type(
        "TITLE", (),
        {
            "ID3": "\xa9nam",
            "CID": "TITLE",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": str
        }
    )

    # custom field for easier editing
    TRACK_NO = type(
        "TRACK_NO", (),
        {
            "ID3": "TRACK_NO",
            "CID": "TRACK_NO",
            "INPUT_TYPE": int,
            "OUTPUT_TYPE": int
        }
    )

    # custom field for easier editing
    TOTAL_TRACKS = type(
        "TOTAL_TRACKS", (),
        {
            "ID3": "TOTAL_TRACKS",
            "CID": "TOTAL_TRACKS",
            "INPUT_TYPE": int,
            "OUTPUT_TYPE": int
        }
    )

    # this field is the one going into the audio file
    TRACK_NO_TUPLE = type(
        "TRACK_NO_TUPLE", (),
        {
            "ID3": "trkn",
            "CID": "TRACK_NO_TUPLE",
            "INPUT_TYPE": tuple,  # tuple of integer
            "OUTPUT_TYPE": tuple  # tuple of integer
        }
    )

    # custom field for easier editing
    DISC_NO = type(
        "DISC_NO", (),
        {
            "ID3": "DISC_NO",
            "CID": "DISC_NO",
            "INPUT_TYPE": int,
            "OUTPUT_TYPE": int
        }
    )

    # custom field for easier editing
    TOTAL_DISCS = type(
        "TOTAL_DISCS", (),
        {
            "ID3": "TOTAL_DISCS",
            "CID": "TOTAL_DISCS",
            "INPUT_TYPE": int,
            "OUTPUT_TYPE": int
        }
    )

    # this field is the one going into the audio file
    DISC_NO_TUPLE = type(
        "DISC_NO_TUPLE", (),
        {
            "ID3": "disk",
            "CID": "DISC_NO_TUPLE",
            "INPUT_TYPE": tuple,  # tuple of integer
            "OUTPUT_TYPE": tuple  # tuple of integer
        }
    )

    ARTIST = type(
        "ARTIST", (),
        {
            "ID3": "\xa9ART",
            "CID": "ARTIST",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": str
        }
    )

    ALBUM_ARTIST = type(
        "ALBUM_ARTIST", (),
        {
            "ID3": "aART",
            "CID": "ALBUM_ARTIST",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": str
        }
    )

    YEAR = type(
        "YEAR", (), {
            "ID3": "\xa9day",
            "CID": "YEAR",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": str
        }
    )

    ALBUM = type(
        "ALBUM", (),
        {
            "ID3": "\xa9alb",
            "CID": "ALBUM",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": str
        }
    )

    GENRE = type(
        "GENRE", (),
        {
            "ID3": "\xa9gen",
            "CID": "GENRE",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": str
        }
    )

    RATING = type(
        "RATING", (),
        {
            "ID3": "----:com.apple.iTunes:rating",
            "CID": "RATING",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": "utf-8"
        }
    )

    BASE_METADATA_COLS = PATH_COLS + [
        TITLE.CID, TRACK_NO.CID, TOTAL_TRACKS.CID,
        DISC_NO.CID, TOTAL_DISCS.CID, ARTIST.CID, ALBUM_ARTIST.CID,
        YEAR.CID, ALBUM.CID, GENRE.CID, RATING.CID]

    # ADDITIONAL METADATA COLS
    COMPOSER = type(
        "COMPOSER", (),
        {
            "ID3": "\xa9wrt",
            "CID": "COMPOSER",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": str
        }
    )

    COMMENT = type(
        "COMMENT", (),
        {
            "ID3": "\xa9cmt",
            "CID": "COMMENT",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": str
        }
    )

    WORK = type(
        "WORK", (),
        {
            "ID3": "\xa9wrk",
            "CID": "WORK",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": str
        }
    )

    MOVEMENT = type(
        "MOVEMENT", (),
        {
            "ID3": "\xa9mvn",
            "CID": "MOVEMENT",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": str
        }
    )

    ADDED_TIMESTAMP = type(
        "ADDED_TIMESTAMP", (),
        {
            "ID3": "----:com.apple.iTunes:added_timestamp",
            "CID": "ADDED_TIMESTAMP",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": "utf-8"
        }
    )

    FIRST_PLAYED_TIMESTAMP = type(
        "FIRST_PLAYED_TIMESTAMP", (),
        {
            "ID3": "----:com.apple.iTunes:first_played_timestamp",
            "CID": "FIRST_PLAYED_TIMESTAMP",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": "utf-8"
        }
    )

    LAST_PLAYED_TIMESTAMP = type(
        "LAST_PLAYED_TIMESTAMP", (),
        {
            "ID3": "----:com.apple.iTunes:last_played_timestamp",
            "CID": "LAST_PLAYED_TIMESTAMP",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": "utf-8"
        }
    )

    PLAY_COUNT = type(
        "PLAY_COUNT", (),
        {
            "ID3": "----:com.apple.iTunes:play_count",
            "CID": "PLAY_COUNT",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": "utf-8"
        }
    )

    REPLAYGAIN_ALBUM_GAIN = type(
        "REPLAYGAIN_ALBUM_GAIN", (),
        {
            "ID3": "----:com.apple.iTunes:replaygain_album_gain",
            "CID": "REPLAYGAIN_ALBUM_GAIN",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": "utf-8"
        }
    )

    REPLAYGAIN_ALBUM_PEAK = type(
        "REPLAYGAIN_ALBUM_PEAK", (),
        {
            "ID3": "----:com.apple.iTunes:replaygain_album_peak",
            "CID": "REPLAYGAIN_ALBUM_PEAK",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": "utf-8"
        }
    )

    REPLAYGAIN_TRACK_GAIN = type(
        "REPLAYGAIN_TRACK_GAIN", (),
        {
            "ID3": "----:com.apple.iTunes:replaygain_track_gain",
            "CID": "REPLAYGAIN_TRACK_GAIN",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": "utf-8"
        }
    )

    REPLAYGAIN_TRACK_PEAK = type(
        "REPLAYGAIN_TRACK_PEAK", (),
        {
            "ID3": "----:com.apple.iTunes:replaygain_track_peak",
            "CID": "REPLAYGAIN_TRACK_PEAK",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": "utf-8"
        }
    )

    ACCURATE_RIP_DISC_ID = type(
        "ACCURATE_RIP_DISC_ID", (),
        {
            "ID3": "----:com.apple.iTunes:AccurateRipDiscID",
            "CID": "ACCURATE_RIP_DISC_ID",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": "utf-8"
        }
    )

    ACCURATE_RIP_RESULT = type(
        "ACCURATE_RIP_RESULT", (),
        {
            "ID3": "----:com.apple.iTunes:AccurateRipResult",
            "CID": "ACCURATE_RIP_RESULT",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": "utf-8"
        }
    )

    ENCODER_SETTINGS = type(
        "ENCODER_SETTINGS", (),
        {
            "ID3": "----:com.apple.iTunes:Encoder Settings",
            "CID": "ENCODER_SETTINGS",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": "utf-8"
        }
    )

    ENCODED_BY = type(
        "ENCODED_BY", (),
        {
            "ID3": "\xa9too",
            "CID": "ENCODED_BY",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": str
        }
    )

    ENCODER_APPLE = type(
        "ENCODER_APPLE", (),
        {
            "ID3": "----:com.apple.iTunes:Encoder",
            "CID": "ENCODER_APPLE",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": "utf-8"
        }
    )

    # TODO: should the CID be ENCODED_BY?
    ENCODER_ID3 = type(
        "ENCODER_ID3", (),
        {
            "ID3": "\xa9enc",
            "CID": "ENCODER_ID3",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": str
        }
    )

    SOURCE = type(
        "SOURCE", (),
        {
            "ID3": "----:com.apple.iTunes:Source",
            "CID": "SOURCE",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": "utf-8"
        }
    )

    # CUSTOM COLS (non-metadata)
    CUSTOM_COLS = [TRACK_NO.CID, TOTAL_TRACKS.CID, COVER_SRC.CID, COVER_DST.CID,
                   DISC_NO.CID, TOTAL_DISCS.CID] + PATH_COLS

    # MAPS (initialize to empty dicts)
    ID3_to_field = {}
    field_to_ID3 = {}


# MAPS
#   Generate maps after the class has been made and set
#   them back as attributes.
ID3_to_field = {eval(f"Fields.{f}.ID3"): eval(f"Fields.{f}.CID")
                for f in dir(Fields) if
                (not eval(f"Fields.{f}.__class__") != type) and ("__" not in f)}
setattr(Fields, "ID3_to_field", ID3_to_field)

field_to_ID3 = {eval(f"Fields.{f}.CID"): eval(f"Fields.{f}.ID3")
                for f in dir(Fields) if
                (not eval(f"Fields.{f}.__class__") != type) and ("__" not in f)}
setattr(Fields, "field_to_ID3", field_to_ID3)
