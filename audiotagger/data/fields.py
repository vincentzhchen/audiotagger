# TODO: remove the class Fields, it is not necessary


class Field():
    id3_to_field = {}
    field_to_id3 = {}

    def __init__(self, id3, cid, input_type, output_type):
        self._id3 = id3
        self._cid = cid
        self._input_type = input_type
        self._output_type = output_type

        # cache
        self.id3_to_field[self.ID3] = self.CID
        self.field_to_id3[self.CID] = self.ID3

    @property
    def ID3(self):
        return self._id3

    @property
    def CID(self):
        return self._cid

    @property
    def INPUT_TYPE(self):
        return self._input_type

    @property
    def OUTPUT_TYPE(self):
        return self._output_type

    @staticmethod
    def ID3_to_field():
        # TODO: deprecate
        return Field.TO_FIELD()

    @staticmethod
    def Field_to_ID3():
        # TODO: deprecate
        return Field.TO_ID3()

    @staticmethod
    def TO_ID3():
        return Field.field_to_id3

    @staticmethod
    def TO_FIELD():
        return Field.id3_to_field


class Fields(object):

    # ADDITIONAL METADATA COLS
    COMPOSER = type("COMPOSER", (), {
        "ID3": "\xa9wrt",
        "CID": "COMPOSER",
        "INPUT_TYPE": str,
        "OUTPUT_TYPE": str
    })

    COMMENT = type("COMMENT", (), {
        "ID3": "\xa9cmt",
        "CID": "COMMENT",
        "INPUT_TYPE": str,
        "OUTPUT_TYPE": str
    })

    WORK = type("WORK", (), {
        "ID3": "\xa9wrk",
        "CID": "WORK",
        "INPUT_TYPE": str,
        "OUTPUT_TYPE": str
    })

    MOVEMENT = type("MOVEMENT", (), {
        "ID3": "\xa9mvn",
        "CID": "MOVEMENT",
        "INPUT_TYPE": str,
        "OUTPUT_TYPE": str
    })

    ADDED_TIMESTAMP = type(
        "ADDED_TIMESTAMP", (), {
            "ID3": "----:com.apple.iTunes:added_timestamp",
            "CID": "ADDED_TIMESTAMP",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": "utf-8"
        })

    FIRST_PLAYED_TIMESTAMP = type(
        "FIRST_PLAYED_TIMESTAMP", (), {
            "ID3": "----:com.apple.iTunes:first_played_timestamp",
            "CID": "FIRST_PLAYED_TIMESTAMP",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": "utf-8"
        })

    LAST_PLAYED_TIMESTAMP = type(
        "LAST_PLAYED_TIMESTAMP", (), {
            "ID3": "----:com.apple.iTunes:last_played_timestamp",
            "CID": "LAST_PLAYED_TIMESTAMP",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": "utf-8"
        })

    PLAY_COUNT = type(
        "PLAY_COUNT", (), {
            "ID3": "----:com.apple.iTunes:play_count",
            "CID": "PLAY_COUNT",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": "utf-8"
        })

    REPLAYGAIN_ALBUM_GAIN = type(
        "REPLAYGAIN_ALBUM_GAIN", (), {
            "ID3": "----:com.apple.iTunes:replaygain_album_gain",
            "CID": "REPLAYGAIN_ALBUM_GAIN",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": "utf-8"
        })

    REPLAYGAIN_ALBUM_PEAK = type(
        "REPLAYGAIN_ALBUM_PEAK", (), {
            "ID3": "----:com.apple.iTunes:replaygain_album_peak",
            "CID": "REPLAYGAIN_ALBUM_PEAK",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": "utf-8"
        })

    REPLAYGAIN_TRACK_GAIN = type(
        "REPLAYGAIN_TRACK_GAIN", (), {
            "ID3": "----:com.apple.iTunes:replaygain_track_gain",
            "CID": "REPLAYGAIN_TRACK_GAIN",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": "utf-8"
        })

    REPLAYGAIN_TRACK_PEAK = type(
        "REPLAYGAIN_TRACK_PEAK", (), {
            "ID3": "----:com.apple.iTunes:replaygain_track_peak",
            "CID": "REPLAYGAIN_TRACK_PEAK",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": "utf-8"
        })

    ACCURATE_RIP_DISC_ID = type(
        "ACCURATE_RIP_DISC_ID", (), {
            "ID3": "----:com.apple.iTunes:AccurateRipDiscID",
            "CID": "ACCURATE_RIP_DISC_ID",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": "utf-8"
        })

    ACCURATE_RIP_RESULT = type(
        "ACCURATE_RIP_RESULT", (), {
            "ID3": "----:com.apple.iTunes:AccurateRipResult",
            "CID": "ACCURATE_RIP_RESULT",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": "utf-8"
        })

    ENCODER_SETTINGS = type(
        "ENCODER_SETTINGS", (), {
            "ID3": "----:com.apple.iTunes:Encoder Settings",
            "CID": "ENCODER_SETTINGS",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": "utf-8"
        })

    ENCODED_BY = type(
        "ENCODED_BY", (), {
            "ID3": "\xa9too",
            "CID": "ENCODED_BY",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": str
        })

    ENCODER_APPLE = type(
        "ENCODER_APPLE", (), {
            "ID3": "----:com.apple.iTunes:Encoder",
            "CID": "ENCODER_APPLE",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": "utf-8"
        })

    # TODO: should the CID be ENCODED_BY?
    ENCODER_ID3 = type(
        "ENCODER_ID3", (), {
            "ID3": "\xa9enc",
            "CID": "ENCODER_ID3",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": str
        })

    SOURCE = type(
        "SOURCE", (), {
            "ID3": "----:com.apple.iTunes:Source",
            "CID": "SOURCE",
            "INPUT_TYPE": str,
            "OUTPUT_TYPE": "utf-8"
        })


# PATH COLS
PATH_SRC = Field(id3="PATH_SRC",
                 cid="PATH_SRC",
                 input_type=str,
                 output_type=str)

PATH_DST = Field(id3="PATH_DST",
                 cid="PATH_DST",
                 input_type=str,
                 output_type=str)

PATH_COLS = [PATH_SRC.CID, PATH_DST.CID]

# COVER COLS
COVER_SRC = Field(id3="COVER_SRC",
                  cid="COVER_SRC",
                  input_type=str,
                  output_type=str)

COVER_DST = Field(id3="COVER_DST",
                  cid="COVER_DST",
                  input_type=str,
                  output_type=str)

COVER = Field(id3="covr", cid="COVER", input_type=str, output_type=None)

COVER_COLS = [COVER_SRC.CID, COVER_DST.CID, COVER.CID]

# BASE METADATA COLS
TITLE = Field(id3="\xa9nam", cid="TITLE", input_type=str, output_type=str)

# custom field for easier editing
TRACK_NO = Field(id3="TRACK_NO",
                 cid="TRACK_NO",
                 input_type=int,
                 output_type=int)

# custom field for easier editing
TOTAL_TRACKS = Field(id3="TOTAL_TRACKS",
                     cid="TOTAL_TRACKS",
                     input_type=int,
                     output_type=int)

# this field is the one going into the audio file
TRACK_NO_TUPLE = Field(
    id3="trkn",
    cid="TRACK_NO_TUPLE",
    input_type=tuple,  # tuple of integer
    output_type=tuple)  # tuple of integer

# custom field for easier editing
DISC_NO = Field(id3="DISC_NO", cid="DISC_NO", input_type=int, output_type=int)

# custom field for easier editing
TOTAL_DISCS = Field(id3="TOTAL_DISCS",
                    cid="TOTAL_DISCS",
                    input_type=int,
                    output_type=int)

# this field is the one going into the audio file
DISC_NO_TUPLE = Field(
    id3="disk",
    cid="DISC_NO_TUPLE",
    input_type=tuple,  # tuple of integer
    output_type=tuple)  # tuple of integer

ARTIST = Field(id3="\xa9ART", cid="ARTIST", input_type=str, output_type=str)

ALBUM_ARTIST = Field(id3="aART",
                     cid="ALBUM_ARTIST",
                     input_type=str,
                     output_type=str)

YEAR = Field(id3="\xa9day", cid="YEAR", input_type=str, output_type=str)

ALBUM = Field(id3="\xa9alb", cid="ALBUM", input_type=str, output_type=str)

GENRE = Field(id3="\xa9gen", cid="GENRE", input_type=str, output_type=str)

RATING = Field(id3="----:com.apple.iTunes:rating",
               cid="RATING",
               input_type=str,
               output_type="utf-8")

BASE_METADATA_COLS = PATH_COLS + [
    TITLE.CID, TRACK_NO.CID, TOTAL_TRACKS.CID, DISC_NO.CID, TOTAL_DISCS.CID,
    ARTIST.CID, ALBUM_ARTIST.CID, YEAR.CID, ALBUM.CID, GENRE.CID, RATING.CID
]

# CUSTOM COLS (non-metadata)
CUSTOM_COLS = [
    TRACK_NO.CID, TOTAL_TRACKS.CID, COVER_SRC.CID, COVER_DST.CID, DISC_NO.CID,
    TOTAL_DISCS.CID
] + PATH_COLS

# MAPS
ID3_to_field = Field.ID3_to_field()
field_to_ID3 = Field.Field_to_ID3()
