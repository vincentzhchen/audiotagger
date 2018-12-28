class Fields(object):
    PATH = type(
        "PATH", (),
        {
            "ID3": "PATH",
            "CID": "PATH",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": str
        }
    )

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

    TRACK_NO = type(
        "TRACK_NO", (),
        {
            "ID3": "TRACK_NO",
            "CID": "TRACK_NO",
            "INPUT_TYPE": int,
            "OUTPUT_TYPE": int
        }
    )

    TOTAL_TRACKS = type(
        "TOTAL_TRACKS", (),
        {
            "ID3": "TOTAL_TRACKS",
            "CID": "TOTAL_TRACKS",
            "INPUT_TYPE": int,
            "OUTPUT_TYPE": int
        }
    )

    TRACK_NUMBER = type(
        "TRACK_NUMBER", (),
        {
            "ID3": "trkn",
            "CID": "TRACK_NUMBER",
            "INPUT_TYPE": tuple,  # tuple of integer
            "OUTPUT_TYPE": tuple  # tuple of integer
        }
    )

    DISC_NO = type(
        "DISC_NO", (),
        {
            "ID3": "DISC_NO",
            "CID": "DISC_NO",
            "INPUT_TYPE": int,
            "OUTPUT_TYPE": int
        }
    )

    TOTAL_DISCS = type(
        "TOTAL_DISCS", (),
        {
            "ID3": "TOTAL_DISCS",
            "CID": "TOTAL_DISCS",
            "INPUT_TYPE": int,
            "OUTPUT_TYPE": int
        }
    )

    DISC_NUMBER = type(
        "DISC_NUMBER", (),
        {
            "ID3": "disk",
            "CID": "DISC_NUMBER",
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

    BASE_METADATA_COLS = [
        TITLE.CID, TRACK_NO.CID, TOTAL_TRACKS.CID, DISC_NO.CID,
        TOTAL_DISCS.CID, ARTIST.CID, ALBUM_ARTIST.CID, YEAR.CID,
        ALBUM.CID, GENRE.CID, RATING.CID]

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

    PLAY_COUNT = type(
        "PLAY_COUNT", (),
        {
            "ID3": "----:com.apple.iTunes:play_count",
            "CID": "PLAY_COUNT",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": "utf-8"
        }
    )

    LYRICS = type(
        "LYRICS", (),
        {
            "ID3": "\xa9lyr",
            "CID": "LYRICS",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": str
        }
    )

    DESCRIPTION = type(
        "DESCRIPTION", (),
        {
            "ID3": "desc",
            "CID": "DESCRIPTION",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": str
        }
    )

    GROUPING = type(
        "GROUPING", (),
        {
            "ID3": "\xa9grp",
            "CID": "GROUPING",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": str
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

    ENCODER_ID3 = type(
        "ENCODER_ID3", (),
        {
            "ID3": "\xa9enc",
            "CID": "ENCODER_ID3",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": str
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

    SOURCE = type(
        "SOURCE", (),
        {
            "ID3": "----:com.apple.iTunes:Source",
            "CID": "SOURCE",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": "utf-8"
        }
    )

    COPYRIGHT = type(
        "COPYRIGHT", (),
        {
            "ID3": "cprt",
            "CID": "COPYRIGHT",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": str
        }
    )

    ALBUM_SORT_ORDER = type(
        "ALBUM_SORT_ORDER", (),
        {
            "ID3": "soal",
            "CID": "ALBUM_SORT_ORDER",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": str
        }
    )

    ALBUM_ARTIST_SORT_ORDER = type(
        "ALBUM_ARTIST_SORT_ORDER", (),
        {
            "ID3": "soaa",
            "CID": "ALBUM_ARTIST_SORT_ORDER",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": str
        }
    )

    ARTIST_SORT_ORDER = type(
        "ARTIST_SORT_ORDER", (),
        {
            "ID3": "soar",
            "CID": "ARTIST_SORT_ORDER",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": str
        }
    )

    TITLE_SORT_ORDER = type(
        "TITLE_SORT_ORDER", (),
        {
            "ID3": "sonm",
            "CID": "TITLE_SORT_ORDER",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": str
        }
    )

    COMPOSER_SORT_ORDER = type(
        "COMPOSER_SORT_ORDER", (),
        {
            "ID3": "soco",
            "CID": "COMPOSER_SORT_ORDER",
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

    DISC_CONFIDENCE = type(
        "DISC_CONFIDENCE", (),
        {
            "ID3": "----:com.apple.iTunes:CTDBDISCCONFIDENCE",
            "CID": "DISC_CONFIDENCE",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": "utf-8"
        }
    )

    TRACK_CONFIDENCE = type(
        "TRACK_CONFIDENCE", (),
        {
            "ID3": "----:com.apple.iTunes:CTDBTRACKCONFIDENCE",
            "CID": "TRACK_CONFIDENCE",
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

    CDDB_DISC_ID = type(
        "CDDB_DISC_ID", (),
        {
            "ID3": "----:com.apple.iTunes:CDDB Disc ID",
            "CID": "CDDB_DISC_ID",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": "utf-8"
        }
    )

    DYNAMIC_RANGE_DR = type(
        "DYNAMIC_RANGE_DR", (),
        {
            "ID3": "----:com.apple.iTunes:Dynamic Range (DR)",
            "CID": "DYNAMIC_RANGE_DR",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": "utf-8"
        }
    )

    DYNAMIC_RANGE_R128 = type(
        "DYNAMIC_RANGE_R128", (),
        {
            "ID3": "----:com.apple.iTunes:Dynamic Range (R128)",
            "CID": "DYNAMIC_RANGE_R128",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": "utf-8"
        }
    )

    IS_COMPILATION = type(
        "IS_COMPILATION", (),
        {
            "ID3": "cpll",
            "CID": "IS_COMPILATION",
            "INPUT_TYPE": bool,
            "OUTPUT_TYPE": bool
        }
    )

    IS_GAPLESS_ALBUM = type(
        "IS_GAPLESS_ALBUM", (),
        {
            "ID3": "pgap",
            "CID": "IS_GAPLESS_ALBUM",
            "INPUT_TYPE": bool,
            "OUTPUT_TYPE": bool
        }
    )

    COVER = type(
        "COVER", (),
        {
            "ID3": "covr",
            "CID": "COVER",
            "INPUT_TYPE": None,
            "OUTPUT_TYPE": None
        }
    )

    # MAPS
    ID3_to_field = {
        PATH.ID3: PATH.CID,
        TITLE.ID3: TITLE.CID,
        TRACK_NO.ID3: TRACK_NO.CID,
        TOTAL_TRACKS.ID3: TOTAL_TRACKS.CID,
        TRACK_NUMBER.ID3: TRACK_NUMBER.CID,
        DISC_NO.ID3: DISC_NO.CID,
        TOTAL_DISCS.ID3: TOTAL_DISCS.CID,
        DISC_NUMBER.ID3: DISC_NUMBER.CID,
        ARTIST.ID3: ARTIST.CID,
        ALBUM_ARTIST.ID3: ALBUM_ARTIST.CID,
        YEAR.ID3: YEAR.CID,
        ALBUM.ID3: ALBUM.CID,
        GENRE.ID3: GENRE.CID,
        RATING.ID3: RATING.CID,
        COMPOSER.ID3: COMPOSER.CID,
        COMMENT.ID3: COMMENT.CID,
        PLAY_COUNT.ID3: PLAY_COUNT.CID,
        LYRICS.ID3: LYRICS.CID,
        DESCRIPTION.ID3: DESCRIPTION.CID,
        GROUPING.ID3: GROUPING.CID,
        ENCODED_BY.ID3: ENCODED_BY.CID,
        ENCODER_APPLE.ID3: ENCODER_APPLE.CID,
        ENCODER_ID3.ID3: ENCODER_ID3.CID,
        ENCODER_SETTINGS.ID3: ENCODER_SETTINGS.CID,
        SOURCE.ID3: SOURCE.CID,
        COPYRIGHT.ID3: COPYRIGHT.CID,
        ALBUM_SORT_ORDER.ID3: ALBUM_SORT_ORDER.CID,
        ALBUM_ARTIST_SORT_ORDER.ID3: ALBUM_ARTIST_SORT_ORDER.CID,
        ARTIST_SORT_ORDER.ID3: ARTIST_SORT_ORDER.CID,
        TITLE_SORT_ORDER.ID3: TITLE_SORT_ORDER.CID,
        COMPOSER_SORT_ORDER.ID3: COMPOSER_SORT_ORDER.CID,
        WORK.ID3: WORK.CID,
        MOVEMENT.ID3: MOVEMENT.CID,
        ADDED_TIMESTAMP.ID3: ADDED_TIMESTAMP.CID,
        FIRST_PLAYED_TIMESTAMP.ID3: FIRST_PLAYED_TIMESTAMP.CID,
        LAST_PLAYED_TIMESTAMP.ID3: LAST_PLAYED_TIMESTAMP.CID,
        DISC_CONFIDENCE.ID3: DISC_CONFIDENCE.CID,
        TRACK_CONFIDENCE.ID3: TRACK_CONFIDENCE.CID,
        REPLAYGAIN_ALBUM_GAIN.ID3: REPLAYGAIN_ALBUM_GAIN.CID,
        REPLAYGAIN_ALBUM_PEAK.ID3: REPLAYGAIN_ALBUM_PEAK.CID,
        REPLAYGAIN_TRACK_GAIN.ID3: REPLAYGAIN_TRACK_GAIN.CID,
        REPLAYGAIN_TRACK_PEAK.ID3: REPLAYGAIN_TRACK_PEAK.CID,
        ACCURATE_RIP_DISC_ID.ID3: ACCURATE_RIP_DISC_ID.CID,
        ACCURATE_RIP_RESULT.ID3: ACCURATE_RIP_RESULT.CID,
        CDDB_DISC_ID.ID3: CDDB_DISC_ID.CID,
        DYNAMIC_RANGE_DR.ID3: DYNAMIC_RANGE_DR.CID,
        DYNAMIC_RANGE_R128.ID3: DYNAMIC_RANGE_R128.CID,
        IS_COMPILATION.ID3: IS_COMPILATION.CID,
        IS_GAPLESS_ALBUM.ID3: IS_GAPLESS_ALBUM.CID,
        COVER.ID3: COVER.CID,
    }

    field_to_ID3 = {
        PATH.CID: PATH.ID3,
        TITLE.CID: TITLE.ID3,
        TRACK_NO.CID: TRACK_NO.ID3,
        TOTAL_TRACKS.CID: TOTAL_TRACKS.ID3,
        TRACK_NUMBER.CID: TRACK_NUMBER.ID3,
        DISC_NO.CID: DISC_NO.ID3,
        TOTAL_DISCS.CID: TOTAL_DISCS.ID3,
        DISC_NUMBER.CID: DISC_NUMBER.ID3,
        ARTIST.CID: ARTIST.ID3,
        ALBUM_ARTIST.CID: ALBUM_ARTIST.ID3,
        YEAR.CID: YEAR.ID3,
        ALBUM.CID: ALBUM.ID3,
        GENRE.CID: GENRE.ID3,
        RATING.CID: RATING.ID3,
        COMPOSER.CID: COMPOSER.ID3,
        COMMENT.CID: COMMENT.ID3,
        PLAY_COUNT.CID: PLAY_COUNT.ID3,
        LYRICS.CID: LYRICS.ID3,
        DESCRIPTION.CID: DESCRIPTION.ID3,
        GROUPING.CID: GROUPING.ID3,
        ENCODED_BY.CID: ENCODED_BY.ID3,
        ENCODER_APPLE.CID: ENCODER_APPLE.ID3,
        ENCODER_ID3.CID: ENCODER_ID3.ID3,
        ENCODER_SETTINGS.CID: ENCODER_SETTINGS.ID3,
        SOURCE.CID: SOURCE.ID3,
        COPYRIGHT.CID: COPYRIGHT.ID3,
        ALBUM_SORT_ORDER.CID: ALBUM_SORT_ORDER.ID3,
        ALBUM_ARTIST_SORT_ORDER.CID: ALBUM_ARTIST_SORT_ORDER.ID3,
        ARTIST_SORT_ORDER.CID: ARTIST_SORT_ORDER.ID3,
        TITLE_SORT_ORDER.CID: TITLE_SORT_ORDER.ID3,
        COMPOSER_SORT_ORDER.CID: COMPOSER_SORT_ORDER.ID3,
        WORK.CID: WORK.ID3,
        MOVEMENT.CID: MOVEMENT.ID3,
        ADDED_TIMESTAMP.CID: ADDED_TIMESTAMP.ID3,
        FIRST_PLAYED_TIMESTAMP.CID: FIRST_PLAYED_TIMESTAMP.ID3,
        LAST_PLAYED_TIMESTAMP.CID: LAST_PLAYED_TIMESTAMP.ID3,
        DISC_CONFIDENCE.CID: DISC_CONFIDENCE.ID3,
        TRACK_CONFIDENCE.CID: TRACK_CONFIDENCE.ID3,
        REPLAYGAIN_ALBUM_GAIN.CID: REPLAYGAIN_ALBUM_GAIN.ID3,
        REPLAYGAIN_ALBUM_PEAK.CID: REPLAYGAIN_ALBUM_PEAK.ID3,
        REPLAYGAIN_TRACK_GAIN.CID: REPLAYGAIN_TRACK_GAIN.ID3,
        REPLAYGAIN_TRACK_PEAK.CID: REPLAYGAIN_TRACK_PEAK.ID3,
        ACCURATE_RIP_DISC_ID.CID: ACCURATE_RIP_DISC_ID.ID3,
        ACCURATE_RIP_RESULT.CID: ACCURATE_RIP_RESULT.ID3,
        CDDB_DISC_ID.CID: CDDB_DISC_ID.ID3,
        DYNAMIC_RANGE_DR.CID: DYNAMIC_RANGE_DR.ID3,
        DYNAMIC_RANGE_R128.CID: DYNAMIC_RANGE_R128.ID3,
        IS_COMPILATION.CID: IS_COMPILATION.ID3,
        IS_GAPLESS_ALBUM.CID: IS_GAPLESS_ALBUM.ID3,
        COVER.CID: COVER.ID3,
    }
