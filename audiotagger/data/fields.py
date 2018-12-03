class Fields(object):
    PATH = type(
        "PATH", (),
        {
            "ID3": "PATH",
            "CID": "PATH",
            "TYPE": str
        }
    )

    # BASE METADATA COLS
    TITLE = type(
        "TITLE", (),
        {
            "ID3": "\xa9nam",
            "CID": "TITLE",
            "TYPE": str
        }
    )

    TRACK_NO = type(
        "TRACK_NO", (),
        {
            "ID3": "TRACK_NO",
            "CID": "TRACK_NO",
            "TYPE": int
        }
    )

    TOTAL_TRACKS = type(
        "TOTAL_TRACKS", (),
        {
            "ID3": "TOTAL_TRACKS",
            "CID": "TOTAL_TRACKS",
            "TYPE": int
        }
    )

    TRACK_NUMBER = type(
        "TRACK_NUMBER", (),
        {
            "ID3": "trkn",
            "CID": "TRACK_NUMBER",
            "TYPE": tuple  # tuple of integer
        }
    )

    DISC_NO = type(
        "DISC_NO", (),
        {
            "ID3": "DISC_NO",
            "CID": "DISC_NO",
            "TYPE": int
        }
    )

    TOTAL_DISCS = type(
        "TOTAL_DISCS", (),
        {
            "ID3": "TOTAL_DISCS",
            "CID": "TOTAL_DISCS",
            "TYPE": int
        }
    )

    DISC_NUMBER = type(
        "DISC_NUMBER", (),
        {
            "ID3": "disk",
            "CID": "DISC_NUMBER",
            "TYPE": tuple  # tuple of integer
        }
    )

    ARTIST = type(
        "ARTIST", (),
        {
            "ID3": "\xa9ART",
            "CID": "ARTIST",
            "TYPE": str
        }
    )

    ALBUM_ARTIST = type(
        "ALBUM_ARTIST", (),
        {
            "ID3": "aART",
            "CID": "ALBUM_ARTIST",
            "TYPE": str
        }
    )

    YEAR = type(
        "YEAR", (), {
            "ID3": "\xa9day",
            "CID": "YEAR",
            "TYPE": str
        }
    )

    ALBUM = type(
        "ALBUM", (),
        {
            "ID3": "\xa9alb",
            "CID": "ALBUM",
            "TYPE": str
        }
    )

    GENRE = type(
        "GENRE", (),
        {
            "ID3": "\xa9gen",
            "CID": "GENRE",
            "TYPE": str
        }
    )

    RATING = type(
        "RATING", (),
        {
            "ID3": "----:com.apple.iTunes:rating",
            "CID": "RATING",
            "TYPE": bytes
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
            "TYPE": str
        }
    )

    COMMENT = type(
        "COMMENT", (),
        {
            "ID3": "\xa9cmt",
            "CID": "COMMENT",
            "TYPE": str
        }
    )

    PLAY_COUNT = type(
        "PLAY_COUNT", (),
        {
            "ID3": "----:com.apple.iTunes:play_count",
            "CID": "PLAY_COUNT",
            "TYPE": str
        }
    )

    LYRICS = type(
        "LYRICS", (),
        {
            "ID3": "\xa9lyr",
            "CID": "LYRICS",
            "TYPE": str
        }
    )

    DESCRIPTION = type(
        "DESCRIPTION", (),
        {
            "ID3": "desc",
            "CID": "DESCRIPTION",
            "TYPE": str
        }
    )

    GROUPING = type(
        "GROUPING", (),
        {
            "ID3": "\xa9grp",
            "CID": "GROUPING",
            "TYPE": str
        }
    )

    ENCODED_BY = type(
        "ENCODED_BY", (),
        {
            "ID3": "\xa9too",
            "CID": "ENCODED_BY",
            "TYPE": str
        }
    )

    ENCODED_BY_ITUNES = type(
        "ENCODED_BY", (),
        {
            "ID3": "----:com.apple.iTunes:Encoder",
            "CID": "ENCODED_BY",
            "TYPE": str
        }
    )

    COPYRIGHT = type(
        "COPYRIGHT", (),
        {
            "ID3": "cprt",
            "CID": "COPYRIGHT",
            "TYPE": str
        }
    )

    ALBUM_SORT_ORDER = type(
        "ALBUM_SORT_ORDER", (),
        {
            "ID3": "soal",
            "CID": "ALBUM_SORT_ORDER",
            "TYPE": str
        }
    )

    ALBUM_ARTIST_SORT_ORDER = type(
        "ALBUM_ARTIST_SORT_ORDER", (),
        {
            "ID3": "soaa",
            "CID": "ALBUM_ARTIST_SORT_ORDER",
            "TYPE": str
        }
    )

    ARTIST_SORT_ORDER = type(
        "ARTIST_SORT_ORDER", (),
        {
            "ID3": "soar",
            "CID": "ARTIST_SORT_ORDER",
            "TYPE": str
        }
    )

    TITLE_SORT_ORDER = type(
        "TITLE_SORT_ORDER", (),
        {
            "ID3": "sonm",
            "CID": "TITLE_SORT_ORDER",
            "TYPE": str
        }
    )

    COMPOSER_SORT_ORDER = type(
        "COMPOSER_SORT_ORDER", (),
        {
            "ID3": "soco",
            "CID": "COMPOSER_SORT_ORDER",
            "TYPE": str
        }
    )

    WORK = type(
        "WORK", (),
        {
            "ID3": "\xa9wrk",
            "CID": "WORK",
            "TYPE": str
        }
    )

    MOVEMENT = type(
        "MOVEMENT", (),
        {
            "ID3": "\xa9mvn",
            "CID": "MOVEMENT",
            "TYPE": str
        }
    )

    ADDED_TIMESTAMP = type(
        "ADDED_TIMESTAMP", (),
        {
            "ID3": "----:com.apple.iTunes:added_timestamp",
            "CID": "ADDED_TIMESTAMP",
            "TYPE": str
        }
    )

    FIRST_PLAYED_TIMESTAMP = type(
        "FIRST_PLAYED_TIMESTAMP", (),
        {
            "ID3": "----:com.apple.iTunes:first_played_timestamp",
            "CID": "FIRST_PLAYED_TIMESTAMP",
            "TYPE": str
        }
    )

    LAST_PLAYED_TIMESTAMP = type(
        "LAST_PLAYED_TIMESTAMP", (),
        {
            "ID3": "----:com.apple.iTunes:last_played_timestamp",
            "CID": "LAST_PLAYED_TIMESTAMP",
            "TYPE": str
        }
    )

    DISC_CONFIDENCE = type(
        "DISC_CONFIDENCE", (),
        {
            "ID3": "----:com.apple.iTunes:CTDBDISCCONFIDENCE",
            "CID": "DISC_CONFIDENCE",
            "TYPE": str
        }
    )

    TRACK_CONFIDENCE = type(
        "TRACK_CONFIDENCE", (),
        {
            "ID3": "----:com.apple.iTunes:CTDBTRACKCONFIDENCE",
            "CID": "TRACK_CONFIDENCE",
            "TYPE": str
        }
    )

    REPLAYGAIN_ALBUM_GAIN = type(
        "REPLAYGAIN_ALBUM_GAIN", (),
        {
            "ID3": "----:com.apple.iTunes:replaygain_album_gain",
            "CID": "REPLAYGAIN_ALBUM_GAIN",
            "TYPE": str
        }
    )

    REPLAYGAIN_ALBUM_PEAK = type(
        "REPLAYGAIN_ALBUM_PEAK", (),
        {
            "ID3": "----:com.apple.iTunes:replaygain_album_peak",
            "CID": "REPLAYGAIN_ALBUM_PEAK",
            "TYPE": str
        }
    )

    REPLAYGAIN_TRACK_GAIN = type(
        "REPLAYGAIN_TRACK_GAIN", (),
        {
            "ID3": "----:com.apple.iTunes:replaygain_track_gain",
            "CID": "REPLAYGAIN_TRACK_GAIN",
            "TYPE": str
        }
    )

    REPLAYGAIN_TRACK_PEAK = type(
        "REPLAYGAIN_TRACK_PEAK", (),
        {
            "ID3": "----:com.apple.iTunes:replaygain_track_peak",
            "CID": "REPLAYGAIN_TRACK_PEAK",
            "TYPE": str
        }
    )

    ACCURATE_RIP_DISC_ID = type(
        "ACCURATE_RIP_DISC_ID", (),
        {
            "ID3": "----:com.apple.iTunes:AccurateRipDiscID",
            "CID": "ACCURATE_RIP_DISC_ID",
            "TYPE": str
        }
    )

    ACCURATE_RIP_RESULT = type(
        "ACCURATE_RIP_RESULT", (),
        {
            "ID3": "----:com.apple.iTunes:AccurateRipResult",
            "CID": "ACCURATE_RIP_RESULT",
            "TYPE": str
        }
    )

    CDDB_DISC_ID = type(
        "CDDB_DISC_ID", (),
        {
            "ID3": "----:com.apple.iTunes:CDDB Disc ID",
            "CID": "CDDB_DISC_ID",
            "TYPE": str
        }
    )

    DYNAMIC_RANGE_DR = type(
        "DYNAMIC_RANGE_DR", (),
        {
            "ID3": "----:com.apple.iTunes:Dynamic Range (DR)",
            "CID": "DYNAMIC_RANGE_DR",
            "TYPE": str
        }
    )

    DYNAMIC_RANGE_R128 = type(
        "DYNAMIC_RANGE_R128", (),
        {
            "ID3": "----:com.apple.iTunes:Dynamic Range (R128)",
            "CID": "DYNAMIC_RANGE_R128",
            "TYPE": str
        }
    )

    IS_COMPILATION = type(
        "IS_COMPILATION", (),
        {
            "ID3": "cpll",
            "CID": "IS_COMPILATION",
            "TYPE": bool
        }
    )

    IS_GAPLESS_ALBUM = type(
        "IS_GAPLESS_ALBUM", (),
        {
            "ID3": "pgap",
            "CID": "IS_GAPLESS_ALBUM",
            "TYPE": bool
        }
    )

    COVER = type(
        "COVER", (),
        {
            "ID3": "covr",
            "CID": "COVER",
            "TYPE": None
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
        ENCODED_BY_ITUNES.ID3: ENCODED_BY_ITUNES.CID,
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
        ENCODED_BY_ITUNES.CID: ENCODED_BY_ITUNES.ID3,
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
