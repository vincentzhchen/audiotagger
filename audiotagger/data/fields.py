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

# ADDITIONAL METADATA COLS
COMPOSER = Field(id3="\xa9wrt",
                 cid="COMPOSER",
                 input_type=str,
                 output_type=str)

COMMENT = Field(id3="\xa9cmt", cid="COMMENT", input_type=str, output_type=str)

WORK = Field(id3="\xa9wrk", cid="WORK", input_type=str, output_type=str)

MOVEMENT = Field(id3="\xa9mvn",
                 cid="MOVEMENT",
                 input_type=str,
                 output_type=str)

ADDED_TIMESTAMP = Field(id3="----:com.apple.iTunes:added_timestamp",
                        cid="ADDED_TIMESTAMP",
                        input_type=str,
                        output_type="utf-8")

FIRST_PLAYED_TIMESTAMP = Field(
    id3="----:com.apple.iTunes:first_played_timestamp",
    cid="FIRST_PLAYED_TIMESTAMP",
    input_type=str,
    output_type="utf-8")

LAST_PLAYED_TIMESTAMP = Field(
    id3="----:com.apple.iTunes:last_played_timestamp",
    cid="LAST_PLAYED_TIMESTAMP",
    input_type=str,
    output_type="utf-8")

PLAY_COUNT = Field(id3="----:com.apple.iTunes:play_count",
                   cid="PLAY_COUNT",
                   input_type=str,
                   output_type="utf-8")

REPLAYGAIN_ALBUM_GAIN = Field(
    id3="----:com.apple.iTunes:replaygain_album_gain",
    cid="REPLAYGAIN_ALBUM_GAIN",
    input_type=str,
    output_type="utf-8")

REPLAYGAIN_ALBUM_PEAK = Field(
    id3="----:com.apple.iTunes:replaygain_album_peak",
    cid="REPLAYGAIN_ALBUM_PEAK",
    input_type=str,
    output_type="utf-8")

REPLAYGAIN_TRACK_GAIN = Field(
    id3="----:com.apple.iTunes:replaygain_track_gain",
    cid="REPLAYGAIN_TRACK_GAIN",
    input_type=str,
    output_type="utf-8")

REPLAYGAIN_TRACK_PEAK = Field(
    id3="----:com.apple.iTunes:replaygain_track_peak",
    cid="REPLAYGAIN_TRACK_PEAK",
    input_type=str,
    output_type="utf-8")

ACCURATE_RIP_DISC_ID = Field(id3="----:com.apple.iTunes:AccurateRipDiscID",
                             cid="ACCURATE_RIP_DISC_ID",
                             input_type=str,
                             output_type="utf-8")

ACCURATE_RIP_RESULT = Field(id3="----:com.apple.iTunes:AccurateRipResult",
                            cid="ACCURATE_RIP_RESULT",
                            input_type=str,
                            output_type="utf-8")

ENCODER_SETTINGS = Field(id3="----:com.apple.iTunes:Encoder Settings",
                         cid="ENCODER_SETTINGS",
                         input_type=str,
                         output_type="utf-8")

ENCODED_BY = Field(id3="\xa9too",
                   cid="ENCODED_BY",
                   input_type=str,
                   output_type=str)

ENCODER_APPLE = Field(id3="----:com.apple.iTunes:Encoder",
                      cid="ENCODER_APPLE",
                      input_type=str,
                      output_type="utf-8")

ENCODER_ID3 = Field(
    id3="\xa9enc",
    cid="ENCODER_ID3",  # TODO: should the CID be ENCODED_BY?
    input_type=str,
    output_type=str)

SOURCE = Field(id3="----:com.apple.iTunes:Source",
               cid="SOURCE",
               input_type=str,
               output_type="utf-8")

# MAPS
ID3_to_field = Field.ID3_to_field()
field_to_ID3 = Field.Field_to_ID3()
