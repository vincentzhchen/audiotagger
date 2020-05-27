# SPDX-License-Identifier: GPL-3.0-or-later

# pylint: disable=missing-module-docstring
# pylint: disable=redefined-outer-name
# pylint: disable=line-too-long
# pylint: disable=invalid-name
import os
import pathlib

import pytest

from audiotagger.data import fields as fld, loader, processing
from audiotagger.util import audiotagger_logger

logger = audiotagger_logger.get_logger(name="test_audiotagger.log")


@pytest.fixture
def loaded_m4a_data():
    """Raw m4a data before any processing.

    """
    test_dir = pathlib.Path(__file__).parent.parent
    src = os.path.join(test_dir, "sample_data")
    ldr = loader.AudioTaggerMetadataLoader(src=src, logger=logger)
    # pylint: disable=protected-access
    df = ldr._load_all_m4a_files_into_df_from_path()
    return df


def test_process_loaded_m4a_data(loaded_m4a_data):
    processor = processing.RawDataProcessor(logger)
    metadata = processor.process_loaded_m4a_data(loaded_m4a_data)
    assert set(fld.BASE_METADATA_COLS).difference(metadata) == set()
