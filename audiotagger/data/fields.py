"""Tag name support switching between human-readable names and tag names.

"""


class Field():
    """A field describes an audio tag.

    Fields are more than just tag names, they also contain information
    about any ID3 keys, the data type of the tag, etc.

    """
    id3_to_field = {}
    field_to_id3 = {}

    def __init__(self, tag_key, cid, input_type, output_type):
        self._tag_key = tag_key
        self._cid = cid
        self._input_type = input_type
        self._output_type = output_type

        # cache
        self.id3_to_field[self.ID3] = self.CID
        self.field_to_id3[self.CID] = self.ID3

    @property
    def ID3(self):  # pylint: disable=invalid-name
        return self._tag_key

    @property
    def CID(self):  # pylint: disable=invalid-name
        return self._cid

    @property
    def INPUT_TYPE(self):  # pylint: disable=invalid-name
        return self._input_type

    @property
    def OUTPUT_TYPE(self):  # pylint: disable=invalid-name
        return self._output_type

    @staticmethod
    def ID3_to_field():  # pylint: disable=invalid-name
        # TODO: deprecate
        return Field.TO_FIELD()

    @staticmethod
    def Field_to_ID3():  # pylint: disable=invalid-name
        # TODO: deprecate
        return Field.TO_ID3()

    @staticmethod
    def TO_ID3():  # pylint: disable=invalid-name
        return Field.field_to_id3

    @staticmethod
    def TO_FIELD():  # pylint: disable=invalid-name
        return Field.id3_to_field


# PATH COLS
PATH_SRC = Field(tag_key="PATH_SRC",
                 cid="PATH_SRC",
                 input_type=str,
                 output_type=str)

PATH_DST = Field(tag_key="PATH_DST",
                 cid="PATH_DST",
                 input_type=str,
                 output_type=str)

PATH_COLS = [PATH_SRC.CID, PATH_DST.CID]

# COVER COLS
COVER_SRC = Field(tag_key="COVER_SRC",
                  cid="COVER_SRC",
                  input_type=str,
                  output_type=str)

COVER_DST = Field(tag_key="COVER_DST",
                  cid="COVER_DST",
                  input_type=str,
                  output_type=str)

COVER = Field(tag_key="covr", cid="COVER", input_type=str, output_type=None)

COVER_COLS = [COVER_SRC.CID, COVER_DST.CID, COVER.CID]

# BASE METADATA COLS
TITLE = Field(tag_key="\xa9nam", cid="TITLE", input_type=str, output_type=str)

# custom field for easier editing
TRACK_NO = Field(tag_key="TRACK_NO",
                 cid="TRACK_NO",
                 input_type=int,
                 output_type=int)

# custom field for easier editing
TOTAL_TRACKS = Field(tag_key="TOTAL_TRACKS",
                     cid="TOTAL_TRACKS",
                     input_type=int,
                     output_type=int)

# this field is the one going into the audio file
TRACK_NO_TUPLE = Field(
    tag_key="trkn",
    cid="TRACK_NO_TUPLE",
    input_type=tuple,  # tuple of integer
    output_type=tuple)  # tuple of integer

# custom field for easier editing
DISC_NO = Field(tag_key="DISC_NO",
                cid="DISC_NO",
                input_type=int,
                output_type=int)

# custom field for easier editing
TOTAL_DISCS = Field(tag_key="TOTAL_DISCS",
                    cid="TOTAL_DISCS",
                    input_type=int,
                    output_type=int)

# this field is the one going into the audio file
DISC_NO_TUPLE = Field(
    tag_key="disk",
    cid="DISC_NO_TUPLE",
    input_type=tuple,  # tuple of integer
    output_type=tuple)  # tuple of integer

ARTIST = Field(tag_key="\xa9ART",
               cid="ARTIST",
               input_type=str,
               output_type=str)

ALBUM_ARTIST = Field(tag_key="aART",
                     cid="ALBUM_ARTIST",
                     input_type=str,
                     output_type=str)

YEAR = Field(tag_key="\xa9day", cid="YEAR", input_type=str, output_type=str)

ALBUM = Field(tag_key="\xa9alb", cid="ALBUM", input_type=str, output_type=str)

GENRE = Field(tag_key="\xa9gen", cid="GENRE", input_type=str, output_type=str)

RATING = Field(tag_key="----:com.apple.iTunes:rating",
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
COMPOSER = Field(tag_key="\xa9wrt",
                 cid="COMPOSER",
                 input_type=str,
                 output_type=str)

COMMENT = Field(tag_key="\xa9cmt",
                cid="COMMENT",
                input_type=str,
                output_type=str)

WORK = Field(tag_key="\xa9wrk", cid="WORK", input_type=str, output_type=str)

MOVEMENT = Field(tag_key="\xa9mvn",
                 cid="MOVEMENT",
                 input_type=str,
                 output_type=str)

ADDED_TIMESTAMP = Field(tag_key="----:com.apple.iTunes:added_timestamp",
                        cid="ADDED_TIMESTAMP",
                        input_type=str,
                        output_type="utf-8")

FIRST_PLAYED_TIMESTAMP = Field(
    tag_key="----:com.apple.iTunes:first_played_timestamp",
    cid="FIRST_PLAYED_TIMESTAMP",
    input_type=str,
    output_type="utf-8")

LAST_PLAYED_TIMESTAMP = Field(
    tag_key="----:com.apple.iTunes:last_played_timestamp",
    cid="LAST_PLAYED_TIMESTAMP",
    input_type=str,
    output_type="utf-8")

PLAY_COUNT = Field(tag_key="----:com.apple.iTunes:play_count",
                   cid="PLAY_COUNT",
                   input_type=str,
                   output_type="utf-8")

REPLAYGAIN_ALBUM_GAIN = Field(
    tag_key="----:com.apple.iTunes:replaygain_album_gain",
    cid="REPLAYGAIN_ALBUM_GAIN",
    input_type=str,
    output_type="utf-8")

REPLAYGAIN_ALBUM_PEAK = Field(
    tag_key="----:com.apple.iTunes:replaygain_album_peak",
    cid="REPLAYGAIN_ALBUM_PEAK",
    input_type=str,
    output_type="utf-8")

REPLAYGAIN_TRACK_GAIN = Field(
    tag_key="----:com.apple.iTunes:replaygain_track_gain",
    cid="REPLAYGAIN_TRACK_GAIN",
    input_type=str,
    output_type="utf-8")

REPLAYGAIN_TRACK_PEAK = Field(
    tag_key="----:com.apple.iTunes:replaygain_track_peak",
    cid="REPLAYGAIN_TRACK_PEAK",
    input_type=str,
    output_type="utf-8")

ACCURATE_RIP_DISC_ID = Field(tag_key="----:com.apple.iTunes:AccurateRipDiscID",
                             cid="ACCURATE_RIP_DISC_ID",
                             input_type=str,
                             output_type="utf-8")

ACCURATE_RIP_RESULT = Field(tag_key="----:com.apple.iTunes:AccurateRipResult",
                            cid="ACCURATE_RIP_RESULT",
                            input_type=str,
                            output_type="utf-8")

ENCODER_SETTINGS = Field(tag_key="----:com.apple.iTunes:Encoder Settings",
                         cid="ENCODER_SETTINGS",
                         input_type=str,
                         output_type="utf-8")

ENCODED_BY = Field(tag_key="\xa9too",
                   cid="ENCODED_BY",
                   input_type=str,
                   output_type=str)

ENCODER_APPLE = Field(tag_key="----:com.apple.iTunes:Encoder",
                      cid="ENCODER_APPLE",
                      input_type=str,
                      output_type="utf-8")

ENCODER_ID3 = Field(
    tag_key="\xa9enc",
    cid="ENCODER_ID3",  # TODO: should the CID be ENCODED_BY?
    input_type=str,
    output_type=str)

SOURCE = Field(tag_key="----:com.apple.iTunes:Source",
               cid="SOURCE",
               input_type=str,
               output_type="utf-8")

# MAPS
ID3_to_field = Field.ID3_to_field()
field_to_ID3 = Field.Field_to_ID3()
