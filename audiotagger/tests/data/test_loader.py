# STANDARD LIB
import os
import pytest

# DEPENDENCIES
import redquill as rq

# PROJECT LIB
from audiotagger.core import paths
from audiotagger.data import fields, loader

# ALIAS
fld = fields.Fields
logger = rq.initialize_logger(paths.audiotagger_log_dir(),
                              "test_audiotagger_loader.log")


@pytest.fixture
def src_files():
    """Returns an Excel file path."""
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


def test_loading_metadata_from_files(src_files):
    ldr = loader.AudioTaggerMetadataLoader(src=src_files, logger=logger)
    out = ldr.load_metadata_df()
    assert set(fld.BASE_METADATA_COLS).difference(out.columns) == set()
