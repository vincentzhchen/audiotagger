# SPDX-License-Identifier: GPL-3.0-or-later
"""Tag name support switching between human-readable names and tag names.

"""


class Field():
  """A field describes an audio tag.

  Fields are more than just tag names, they also contain information
  about any ID3 keys, the data type of the tag, etc.

  """
  id3_to_field = {}  # cache this
  field_to_id3 = {}  # cache this

  def __init__(self, tag_key, tag_name, input_type, output_type):
    self._tag_key = tag_key
    self._tag_name = tag_name
    self._input_type = input_type
    self._output_type = output_type

    # cache
    self.id3_to_field[self.KEY] = self.CID
    self.field_to_id3[self.CID] = self.KEY

  @property
  def KEY(self):  # pylint: disable=invalid-name
    """Original key for the tag field.

    Examples:
      Field: Title
      KEY: "\u00a9nam"

      Field: Album Artist
      KEY: "aART"

      Field: Rating
      KEY: "----:com.apple.iTunes:rating"

    """
    return self._tag_key

  @property
  def CID(self):  # pylint: disable=invalid-name
    """Column ID for the system.

    The value of this is a human-readable name for the tag field.

    Example:
      Field: Title
      CID: "TITLE"

      Field: Album Artist
      CID: "ALBUM_ARTIST"

      Field: Rating
      CID: "RATING"

    """
    return self._tag_name

  @property
  def INPUT_TYPE(self):  # pylint: disable=invalid-name
    """The data type needed for application input.

    This is how the application treats the tag data type, regardless
    of the actual data type of the tag.  For example,
    "----:com.apple.iTunes:replaygain_track_gain" is loaded from the
    file as a MP4FreeForm object with utf-8 encoding, but the
    audiotagger reads and treats it as a string.

    """
    return self._input_type

  @property
  def OUTPUT_TYPE(self):  # pylint: disable=invalid-name
    """The data type needed by the tag for the audio file.

    This is tag data type stored in the audio file.  For example,
    "----:com.apple.iTunes:replaygain_track_gain" was modified
    as a string type inside of audiotagger, but when storing the
    value back into the m4a file it needs to be utf-8.

    """
    return self._output_type


# PATH COLS
PATH_SRC = Field(tag_key="PATH_SRC",
                 tag_name="PATH_SRC",
                 input_type=str,
                 output_type=str)

PATH_DST = Field(tag_key="PATH_DST",
                 tag_name="PATH_DST",
                 input_type=str,
                 output_type=str)

PATH_COLS = [PATH_SRC.CID, PATH_DST.CID]

# COVER COLS
COVER_SRC = Field(tag_key="COVER_SRC",
                  tag_name="COVER_SRC",
                  input_type=str,
                  output_type=str)

COVER_DST = Field(tag_key="COVER_DST",
                  tag_name="COVER_DST",
                  input_type=str,
                  output_type=str)

COVER = Field(tag_key="covr",
              tag_name="COVER",
              input_type=str,
              output_type=None)

COVER_COLS = [COVER_SRC.CID, COVER_DST.CID, COVER.CID]

# BASE METADATA COLS
TITLE = Field(tag_key="\xa9nam",
              tag_name="TITLE",
              input_type=str,
              output_type=str)

# custom field for easier editing
TRACK_NO = Field(tag_key="TRACK_NO",
                 tag_name="TRACK_NO",
                 input_type=int,
                 output_type=int)

# custom field for easier editing
TOTAL_TRACKS = Field(tag_key="TOTAL_TRACKS",
                     tag_name="TOTAL_TRACKS",
                     input_type=int,
                     output_type=int)

# this field is the one going into the audio file
TRACK_NO_TUPLE = Field(
    tag_key="trkn",
    tag_name="TRACK_NO_TUPLE",
    input_type=tuple,  # tuple of integer
    output_type=tuple)  # tuple of integer

# custom field for easier editing
DISC_NO = Field(tag_key="DISC_NO",
                tag_name="DISC_NO",
                input_type=int,
                output_type=int)

# custom field for easier editing
TOTAL_DISCS = Field(tag_key="TOTAL_DISCS",
                    tag_name="TOTAL_DISCS",
                    input_type=int,
                    output_type=int)

# this field is the one going into the audio file
DISC_NO_TUPLE = Field(
    tag_key="disk",
    tag_name="DISC_NO_TUPLE",
    input_type=tuple,  # tuple of integer
    output_type=tuple)  # tuple of integer

ARTIST = Field(tag_key="\xa9ART",
               tag_name="ARTIST",
               input_type=str,
               output_type=str)

ALBUM_ARTIST = Field(tag_key="aART",
                     tag_name="ALBUM_ARTIST",
                     input_type=str,
                     output_type=str)

YEAR = Field(tag_key="\xa9day",
             tag_name="YEAR",
             input_type=str,
             output_type=str)

ALBUM = Field(tag_key="\xa9alb",
              tag_name="ALBUM",
              input_type=str,
              output_type=str)

GENRE = Field(tag_key="\xa9gen",
              tag_name="GENRE",
              input_type=str,
              output_type=str)

RATING = Field(tag_key="----:com.apple.iTunes:rating",
               tag_name="RATING",
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
                 tag_name="COMPOSER",
                 input_type=str,
                 output_type=str)

COMMENT = Field(tag_key="\xa9cmt",
                tag_name="COMMENT",
                input_type=str,
                output_type=str)

WORK = Field(tag_key="\xa9wrk",
             tag_name="WORK",
             input_type=str,
             output_type=str)

MOVEMENT = Field(tag_key="\xa9mvn",
                 tag_name="MOVEMENT",
                 input_type=str,
                 output_type=str)

ADDED_TIMESTAMP = Field(tag_key="----:com.apple.iTunes:added_timestamp",
                        tag_name="ADDED_TIMESTAMP",
                        input_type=str,
                        output_type="utf-8")

FIRST_PLAYED_TIMESTAMP = Field(
    tag_key="----:com.apple.iTunes:first_played_timestamp",
    tag_name="FIRST_PLAYED_TIMESTAMP",
    input_type=str,
    output_type="utf-8")

LAST_PLAYED_TIMESTAMP = Field(
    tag_key="----:com.apple.iTunes:last_played_timestamp",
    tag_name="LAST_PLAYED_TIMESTAMP",
    input_type=str,
    output_type="utf-8")

PLAY_COUNT = Field(tag_key="----:com.apple.iTunes:play_count",
                   tag_name="PLAY_COUNT",
                   input_type=str,
                   output_type="utf-8")

REPLAYGAIN_ALBUM_GAIN = Field(
    tag_key="----:com.apple.iTunes:replaygain_album_gain",
    tag_name="REPLAYGAIN_ALBUM_GAIN",
    input_type=str,
    output_type="utf-8")

REPLAYGAIN_ALBUM_PEAK = Field(
    tag_key="----:com.apple.iTunes:replaygain_album_peak",
    tag_name="REPLAYGAIN_ALBUM_PEAK",
    input_type=str,
    output_type="utf-8")

REPLAYGAIN_TRACK_GAIN = Field(
    tag_key="----:com.apple.iTunes:replaygain_track_gain",
    tag_name="REPLAYGAIN_TRACK_GAIN",
    input_type=str,
    output_type="utf-8")

REPLAYGAIN_TRACK_PEAK = Field(
    tag_key="----:com.apple.iTunes:replaygain_track_peak",
    tag_name="REPLAYGAIN_TRACK_PEAK",
    input_type=str,
    output_type="utf-8")

ACCURATE_RIP_DISC_ID = Field(tag_key="----:com.apple.iTunes:AccurateRipDiscID",
                             tag_name="ACCURATE_RIP_DISC_ID",
                             input_type=str,
                             output_type="utf-8")

ACCURATE_RIP_RESULT = Field(tag_key="----:com.apple.iTunes:AccurateRipResult",
                            tag_name="ACCURATE_RIP_RESULT",
                            input_type=str,
                            output_type="utf-8")

ENCODER_SETTINGS = Field(tag_key="----:com.apple.iTunes:Encoder Settings",
                         tag_name="ENCODER_SETTINGS",
                         input_type=str,
                         output_type="utf-8")

ENCODED_BY = Field(tag_key="\xa9too",
                   tag_name="ENCODED_BY",
                   input_type=str,
                   output_type=str)

ENCODER_APPLE = Field(tag_key="----:com.apple.iTunes:Encoder",
                      tag_name="ENCODER_APPLE",
                      input_type=str,
                      output_type="utf-8")

ENCODER_ID3 = Field(
    tag_key="\xa9enc",
    tag_name="ENCODER_ID3",  # TODO: should the CID be ENCODED_BY?
    input_type=str,
    output_type=str)

SOURCE = Field(tag_key="----:com.apple.iTunes:Source",
               tag_name="SOURCE",
               input_type=str,
               output_type="utf-8")

# MAPS
TO_FIELD = Field.id3_to_field
TO_ID3 = Field.field_to_id3
