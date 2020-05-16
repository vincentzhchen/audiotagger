# pylint: disable=missing-module-docstring
# pylint: disable=redefined-outer-name
# pylint: disable=line-too-long
# pylint: disable=invalid-name
import pandas as pd
import pytest

from audiotagger.core import audiotagger
from audiotagger.data import input as at_in
from audiotagger.util import audiotagger_logger

logger = audiotagger_logger.get_logger(name="test_audiotagger.log")


@pytest.fixture
def input_object():
    """Returns an input instance with metadata structure.

    The metadata structure is correct, but there is no data.

    """
    input_obj = at_in.AudioTaggerInput(logger)
    df = pd.read_json(
        '{"PATH_SRC":{"0":"\\/path\\/to\\/file\\/1.m4a","1":"\\/path\\/to\\/file\\/2.m4a","2":"\\/path\\/to\\/file\\/3.m4a","3":"\\/path\\/to\\/file\\/4.m4a","4":"\\/path\\/to\\/file\\/5.m4a"},"PATH_DST":{"0":"\\/path\\/to\\/file\\/1.m4a","1":"\\/path\\/to\\/file\\/2.m4a","2":"\\/path\\/to\\/file\\/3.m4a","3":"\\/path\\/to\\/file\\/4.m4a","4":"\\/path\\/to\\/file\\/5.m4a"},"TITLE":{"0":"title1","1":"title2","2":"title3","3":"title4","4":"title5"},"TRACK_NO":{"0":1,"1":2,"2":3,"3":4,"4":5},"TOTAL_TRACKS":{"0":5,"1":5,"2":5,"3":5,"4":5},"DISC_NO":{"0":1,"1":1,"2":1,"3":1,"4":1},"TOTAL_DISCS":{"0":1,"1":1,"2":1,"3":1,"4":1},"ARTIST":{"0":"test_artist","1":"test_artist","2":"test_artist","3":"test_artist","4":"test_artist"},"ALBUM_ARTIST":{"0":"test_artist","1":"test_artist","2":"test_artist","3":"test_artist","4":"test_artist"},"YEAR":{"0":2020,"1":2020,"2":2020,"3":2020,"4":2020},"ALBUM":{"0":"test_album","1":"test_album","2":"test_album","3":"test_album","4":"test_album"},"GENRE":{"0":"test_genre","1":"test_genre","2":"test_genre","3":"test_genre","4":"test_genre"},"RATING":{"0":1,"1":1,"2":1,"3":1,"4":1},"ACCURATE_RIP_DISC_ID":{"0":"abcdefghijklmnopqrstuvwxyz-1","1":"abcdefghijklmnopqrstuvwxyz-2","2":"abcdefghijklmnopqrstuvwxyz-3","3":"abcdefghijklmnopqrstuvwxyz-4","4":"abcdefghijklmnopqrstuvwxyz-5"},"ACCURATE_RIP_RESULT":{"0":"AccurateRip: Accurate (confidence 10)","1":"AccurateRip: Accurate (confidence 10)","2":"AccurateRip: Accurate (confidence 10)","3":"AccurateRip: Accurate (confidence 10)","4":"AccurateRip: Accurate (confidence 10)"}}'
    )

    # TODO: the test should work with doing this; fix
    df["YEAR"] = df["YEAR"].astype(str)
    df["RATING"] = df["RATING"].astype(str)
    input_obj.set_metadata(df)
    return input_obj


def test_audiotagger(input_object):
    at = audiotagger.AudioTagger(input_object, logger=logger)
    df = at.execute()

    reference = input_object.get_metadata()
    assert df.equals(reference)
