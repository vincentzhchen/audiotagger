# SPDX-License-Identifier: GPL-3.0-or-later

# pylint: disable=missing-module-docstring
# pylint: disable=redefined-outer-name
# pylint: disable=line-too-long
# pylint: disable=invalid-name
import os
import pathlib

import pandas as pd
import pytest

from audiotagger.data import at_input as at_in, fields as fld, loader


@pytest.fixture
def raw_input_object():
    """Returns an unmodified input instance.

    This has no data in it.

    """
    return at_in.AudioTaggerInput()


def test_set_metadata_with_incorrect_metadata_df(raw_input_object):
    with pytest.raises(ValueError):
        df = pd.DataFrame()
        raw_input_object.set_metadata(df)


def test_set_metadata_with_correct_metadata_df(raw_input_object):
    df = pd.DataFrame(columns=fld.BASE_METADATA_COLS)
    raw_input_object.set_metadata(df)
    assert set(fld.BASE_METADATA_COLS).difference(df.columns) == set()


def test_get_metadata_raises_if_metadata_not_set():
    with pytest.raises(AttributeError):
        input_obj = at_in.AudioTaggerInput()
        input_obj.get_metadata()


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


def test_get_metadata_can_retrieve_data(input_object):
    out = input_object.get_metadata()
    assert set(fld.BASE_METADATA_COLS).difference(out.columns) == set()
