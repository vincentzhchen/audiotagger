# SPDX-License-Identifier: GPL-3.0-or-later

# pylint: disable=missing-module-docstring
# pylint: disable=redefined-outer-name
# pylint: disable=line-too-long
# pylint: disable=invalid-name
import os
import pathlib

import pytest

from audiotagger.core import clear_tags
from audiotagger.data import at_input as at_in, fields as fld, loader
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


def test_clear_all_tags(input_object):
    ct = clear_tags.ClearTags(input_data=input_object, logger=logger)
    df = ct.execute(clear_type="all")

    reference = input_object.get_metadata()[fld.PATH_COLS]
    assert df.equals(reference)


def test_clear_excess_tags(input_object):
    ct = clear_tags.ClearTags(input_data=input_object, logger=logger)
    df = ct.execute(clear_type="excess")

    reference = input_object.get_metadata()[fld.BASE_METADATA_COLS]
    assert df.equals(reference)
