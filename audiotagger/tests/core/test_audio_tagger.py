# pylint: disable=missing-module-docstring
# pylint: disable=redefined-outer-name
# pylint: disable=line-too-long
# pylint: disable=invalid-name
import os
import pathlib

import pandas as pd
import pytest

from audiotagger.core import audiotagger
from audiotagger.data import at_input as at_in, loader
from audiotagger.util import audiotagger_logger

logger = audiotagger_logger.get_logger(name="test_audiotagger.log")


@pytest.fixture
def input_object():
    """Returns an input instance with metadata structure.

    """
    test_dir = pathlib.Path(__file__).parent.parent
    src = os.path.join(test_dir, "sample_data/test_metadata.xlsx")
    ldr = loader.AudioTaggerMetadataLoader(src)
    metadata = ldr.load_metadata_df()

    input_obj = at_in.AudioTaggerInput()
    input_obj.set_metadata(metadata)
    return input_obj


def test_audiotagger(input_object):
    at = audiotagger.AudioTagger(input_object, logger=logger)
    df = at.execute()

    reference = input_object.get_metadata()
    assert df.equals(reference)
