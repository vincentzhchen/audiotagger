# SPDX-License-Identifier: GPL-3.0-or-later

# pylint: disable=missing-module-docstring
# pylint: disable=redefined-outer-name
# pylint: disable=line-too-long
# pylint: disable=invalid-name
import os
import pathlib

import pytest

from audiotagger.core import copy_file
from audiotagger.data import at_input as at_in, loader
from audiotagger.util import audiotagger_logger

logger = audiotagger_logger.get_logger(name="test_audiotagger.log")


@pytest.fixture
def input_object():
    """Returns an input instance with metadata structure.

    """
    test_dir = pathlib.Path(__file__).parent.parent
    src = os.path.join(test_dir, "sample_data")
    ldr = loader.AudioTaggerMetadataLoader(src)
    metadata = ldr.load_metadata_df()

    input_obj = at_in.AudioTaggerInput()
    input_obj.set_metadata(metadata)
    return input_obj


@pytest.fixture
def input_object2():
    """Returns an input instance with metadata structure.

    """
    test_dir = pathlib.Path(__file__).parent.parent
    src = os.path.join(test_dir, "sample_data2")
    ldr = loader.AudioTaggerMetadataLoader(src)
    metadata = ldr.load_metadata_df()

    input_obj = at_in.AudioTaggerInput()
    input_obj.set_metadata(metadata)
    return input_obj


def test_copy_file_dry_run(input_object):
    test_dir = pathlib.Path(__file__).parent.parent
    dst = os.path.join(test_dir, "sample_data2")

    cp = copy_file.CopyFile(input_object, logger=logger)
    cp.execute(dst_dir=dst)


def test_copy_file(input_object):
    test_dir = pathlib.Path(__file__).parent.parent
    dst = os.path.join(test_dir, "sample_data2")

    cp = copy_file.CopyFile(input_object, logger=logger)
    cp.execute(dst_dir=dst, to_file=True)


def test_copy_file_same_dst(input_object2):
    cp = copy_file.CopyFile(input_object2, logger=logger)
    cp.execute(to_file=True)
