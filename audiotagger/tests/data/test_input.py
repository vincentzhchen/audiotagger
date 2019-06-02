# STANDARD LIB
import pandas as pd
import pytest

# DEPENDENCIES
import redquill as rq

# PROJECT LIB
from audiotagger.core import paths
from audiotagger.data import fields
from audiotagger.data import input as at_in

# ALIAS
fld = fields.Fields()

logger = rq.initialize_logger(paths.audiotagger_log_dir(),
                              "test_audiotagger_input.log")


@pytest.fixture
def raw_input_object():
    """Returns an unmodified input instance."""
    return at_in.AudioTaggerInput(logger)


def test_set_metadata_with_incorrect_metadata_df(raw_input_object):
    with pytest.raises(ValueError):
        df = pd.DataFrame()
        raw_input_object.set_metadata(df)


def test_set_metadata_with_correct_metadata_df(raw_input_object):
    df = pd.DataFrame(columns=fld.BASE_METADATA_COLS)
    raw_input_object.set_metadata(df)
    assert set(fld.BASE_METADATA_COLS).difference(df.columns) == set()


@pytest.fixture
def input_object():
    """Returns an input instance with metadata."""
    input_obj = at_in.AudioTaggerInput(logger)
    df = pd.DataFrame(columns=fld.BASE_METADATA_COLS)
    input_obj.set_metadata(df)
    return input_obj


def test_get_metadata_raises_if_metadata_not_set():
    with pytest.raises(ValueError):
        input_obj = at_in.AudioTaggerInput(logger)
        input_obj.get_metadata()


def test_get_metadata_can_retrieve_data(input_object):
    out = input_object.get_metadata()
    assert set(fld.BASE_METADATA_COLS).difference(out.columns) == set()
