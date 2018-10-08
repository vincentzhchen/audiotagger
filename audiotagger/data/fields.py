class Fields(object):
    # STRING
    TITLE                                      = "TITLE"
    ALBUM                                      = "ALBUM"
    ARTIST                                     = "ARTIST"
    ALBUM_ARTIST                               = "ALBUM_ARTIST"
    COMPOSER                                   = "COMPOSER"
    YEAR                                       = "YEAR"
    COMMENT                                    = "COMMENT"
    DESCRIPTION                                = "DESCRIPTION"
    GROUPING                                   = "GROUPING"
    GENRE                                      = "GENRE"
    LYRICS                                     = "LYRICS"
    ENCODED_BY                                 = "ENCODED_BY"
    COPYRIGHT                                  = "COPYRIGHT"
    ALBUM_SORT_ORDER                           = "ALBUM_SORT_ORDER"
    ALBUM_ARTIST_SORT_ORDER                    = "ALBUM_ARTIST_SORT_ORDER"
    ARTIST_SORT_ORDER                          = "ARTIST_SORT_ORDER"
    TITLE_SORT_ORDER                           = "TITLE_SORT_ORDER"
    COMPOSER_SORT_ORDER                        = "COMPOSER_SORT_ORDER"
    WORK                                       = "WORK"
    MOVEMENT                                   = "MOVEMENT"

    # BOOLEAN
    IS_COMPILATION                             = "IS_COMPILATION"
    IS_GAPLESS_ALBUM                           = "IS_GAPLESS_ALBUM"

    # TUPLES OF INTEGERS
    TRACK_NUMBER                               = "TRACK_NUMBER"
    DISC_NUMBER                                = "DISC_NUMBER"

    # OTHER
    COVER                                      = "COVER"
    DISC_CONFIDENCE                            = "DISC_CONFIDENCE"
    TRACK_CONFIDENCE                           = "TRACK_CONFIDENCE"
    ADDED_TIMESTAMP                            = "ADDED_TIMESTAMP"
    RATING                                     = "RATING"
    REPLAYGAIN_ALBUM_GAIN                      = "REPLAYGAIN_ALBUM_GAIN"
    REPLAYGAIN_ALBUM_PEAK                      = "REPLAYGAIN_ALBUM_PEAK"
    REPLAYGAIN_TRACK_GAIN                      = "REPLAYGAIN_TRACK_GAIN"
    REPLAYGAIN_TRACK_PEAK                      = "REPLAYGAIN_TRACK_PEAK"
    ACCURATE_RIP_DISC_ID                       = "ACCURATE_RIP_DISC_ID"
    ACCURATE_RIP_RESULT                        = "ACCURATE_RIP_RESULT"
    CDDB_DISC_ID                               = "CDDB_DISC_ID"
    DYNAMIC_RANGE_DR                           = "DYNAMIC_RANGE_DR"
    DYNAMIC_RANGE_R128                         = "DYNAMIC_RANGE_R128"

    # CUSTOM
    TRACK_NO                                   = "TRACK_NO"
    TOTAL_TRACKS                               = "TOTAL_TRACKS"
    DISC_NO                                    = "DISC_NO"
    TOTAL_DISCS                                = "TOTAL_DISCS"
    PATH                                       = "PATH"

    BASE_METADATA_COLS = [TITLE, TRACK_NO, TOTAL_TRACKS, DISC_NO, TOTAL_DISCS,
                          ARTIST, ALBUM_ARTIST, YEAR, ALBUM, GENRE, RATING]

    ID3_to_field = {
        "\xa9nam": TITLE,
        "\xa9alb": ALBUM,
        "\xa9ART": ARTIST,
        "aART": ALBUM_ARTIST,
        "\xa9wrt": COMPOSER,
        "\xa9day": YEAR,
        "\xa9cmt": COMMENT,
        "desc": DESCRIPTION,
        "\xa9grp": GROUPING,
        "\xa9gen": GENRE,
        "\xa9lyr": LYRICS,
        "\xa9too": ENCODED_BY,
        "cprt": COPYRIGHT,
        "soal": ALBUM_SORT_ORDER,
        "soaa": ALBUM_ARTIST_SORT_ORDER,
        "soar": ARTIST_SORT_ORDER,
        "sonm": TITLE_SORT_ORDER,
        "soco": COMPOSER_SORT_ORDER,
        "\xa9wrk": WORK,
        "\xa9mvn": MOVEMENT,
        "cpll": IS_COMPILATION,
        "pgap": IS_GAPLESS_ALBUM,
        "trkn": TRACK_NUMBER,
        "disk": DISC_NUMBER,
        "covr": COVER,
        "----:com.apple.iTunes:CTDBDISCCONFIDENCE": DISC_CONFIDENCE,
        "----:com.apple.iTunes:CTDBTRACKCONFIDENCE": TRACK_CONFIDENCE,
        "----:com.apple.iTunes:added_timestamp": ADDED_TIMESTAMP,
        "----:com.apple.iTunes:rating": RATING,
        "----:com.apple.iTunes:replaygain_album_gain": REPLAYGAIN_ALBUM_GAIN,
        "----:com.apple.iTunes:replaygain_album_peak": REPLAYGAIN_ALBUM_PEAK,
        "----:com.apple.iTunes:replaygain_track_gain": REPLAYGAIN_TRACK_GAIN,
        "----:com.apple.iTunes:replaygain_track_peak": REPLAYGAIN_TRACK_PEAK,
        "----:com.apple.iTunes:AccurateRipDiscID": ACCURATE_RIP_DISC_ID,
        "----:com.apple.iTunes:AccurateRipResult": ACCURATE_RIP_RESULT,
        "----:com.apple.iTunes:CDDB Disc ID": CDDB_DISC_ID,
        "----:com.apple.iTunes:Dynamic Range (DR)": DYNAMIC_RANGE_DR,
        "----:com.apple.iTunes:Dynamic Range (R128)": DYNAMIC_RANGE_R128,
        "----:com.apple.iTunes:Encoder": ENCODED_BY,
    }

    field_to_ID3 = {
        TITLE: "\xa9nam",
        ALBUM: "\xa9alb",
        ARTIST: "\xa9ART",
        ALBUM_ARTIST: "aART",
        COMPOSER: "\xa9wrt",
        YEAR: "\xa9day",
        COMMENT: "\xa9cmt",
        DESCRIPTION: "desc",
        GROUPING: "\xa9grp",
        GENRE: "\xa9gen",
        LYRICS: "\xa9lyr",
        ENCODED_BY: "\xa9too",
        COPYRIGHT: "cprt",
        ALBUM_SORT_ORDER: "soal",
        ALBUM_ARTIST_SORT_ORDER: "soaa",
        ARTIST_SORT_ORDER: "soar",
        TITLE_SORT_ORDER: "sonm",
        COMPOSER_SORT_ORDER: "soco",
        WORK: "\xa9wrk",
        MOVEMENT: "\xa9mvn",
        IS_COMPILATION: "cpll",
        IS_GAPLESS_ALBUM: "pgap",
        TRACK_NUMBER: "trkn",
        DISC_NUMBER: "disk",
        COVER: "covr",
        # "----:com.apple.iTunes:CTDBDISCCONFIDENCE": DISC_CONFIDENCE,
        # "----:com.apple.iTunes:CTDBTRACKCONFIDENCE": TRACK_CONFIDENCE,
        # "----:com.apple.iTunes:added_timestamp": ADDED_TIMESTAMP,
        # "----:com.apple.iTunes:rating": RATING,
        # "----:com.apple.iTunes:replaygain_album_gain": REPLAYGAIN_ALBUM_GAIN,
        # "----:com.apple.iTunes:replaygain_album_peak": REPLAYGAIN_ALBUM_PEAK,
        # "----:com.apple.iTunes:replaygain_track_gain": REPLAYGAIN_TRACK_GAIN,
        # "----:com.apple.iTunes:replaygain_track_peak": REPLAYGAIN_TRACK_PEAK,
        # "----:com.apple.iTunes:AccurateRipDiscID": ACCURATE_RIP_DISC_ID,
        # "----:com.apple.iTunes:AccurateRipResult": ACCURATE_RIP_RESULT,
        # "----:com.apple.iTunes:CDDB Disc ID": CDDB_DISC_ID,
        # "----:com.apple.iTunes:Dynamic Range (DR)": DYNAMIC_RANGE_DR,
        # "----:com.apple.iTunes:Dynamic Range (R128)": DYNAMIC_RANGE_R128,
        # "----:com.apple.iTunes:Encoder": ENCODED_BY,
    }