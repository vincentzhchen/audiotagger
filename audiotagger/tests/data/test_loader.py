# pylint: disable=missing-module-docstring
# pylint: disable=redefined-outer-name
# pylint: disable=line-too-long
# pylint: disable=invalid-name
from unittest import mock
import os
import pathlib

import pytest

from audiotagger.core import paths
from audiotagger.data import loader
from audiotagger.util import audiotagger_logger

logger = audiotagger_logger.get_logger(name="test_audiotagger_loader.log")


@pytest.fixture
def src_files():
    """Returns an Excel file path.

    """
    return os.path.join(paths.audiotagger_test_dir(), "test_files")


def test_loading_metadata_from_invalid_src():
    with pytest.raises(Exception):
        ldr = loader.AudioTaggerMetadataLoader(src=None, logger=logger)
        ldr.load_metadata_df()


def test_loading_metadata_from_nonexistent_dir():
    with pytest.raises(Exception):
        src = "/foo"
        ldr = loader.AudioTaggerMetadataLoader(src=src, logger=logger)
        ldr.load_metadata_df()


def test_loading_metadata_from_nonexistent_xl_file():
    with pytest.raises(ValueError):
        src = "file.xlsx"
        ldr = loader.AudioTaggerMetadataLoader(src=src, logger=logger)
        ldr.load_metadata_df()


def test_loading_metadata_from_nonexistent_audio_file():
    with pytest.raises(Exception):
        src = "file.m4a"
        ldr = loader.AudioTaggerMetadataLoader(src=src, logger=logger)
        ldr.load_metadata_df()


def mock_m4a_processing(df):
    """Don't process raw loaded data.

    """
    return df


@mock.patch(
    "audiotagger.data.processing.RawDataProcessor.process_loaded_m4a_data")
def test_loading_metadata_from_m4a_file(mocker):
    test_dir = pathlib.Path(__file__).parent.parent
    src = os.path.join(test_dir, "sample_data/Better Days.m4a")

    mocker.side_effect = mock_m4a_processing

    ldr = loader.AudioTaggerMetadataLoader(src=src, logger=logger)
    out = ldr.load_metadata_df()
    assert "\u00a9nam" in out


@mock.patch(
    "audiotagger.data.processing.RawDataProcessor.process_loaded_m4a_data")
def test_loading_metadata_from_dir_of_m4a_files(mocker):
    test_dir = pathlib.Path(__file__).parent.parent
    src = os.path.join(test_dir, "sample_data")

    mocker.side_effect = mock_m4a_processing

    ldr = loader.AudioTaggerMetadataLoader(src=src, logger=logger)
    out = ldr.load_metadata_df()
    assert "\u00a9nam" in out
