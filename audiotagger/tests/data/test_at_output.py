# SPDX-License-Identifier: GPL-3.0-or-later

# pylint: disable=missing-module-docstring
# pylint: disable=redefined-outer-name
# pylint: disable=line-too-long
# pylint: disable=invalid-name
import os
import pathlib

import pytest

from audiotagger.data import at_output as at_out, loader


@pytest.fixture
def output_object():
    """Output instance.

    """
    test_dir = pathlib.Path(__file__).parent.parent
    src = os.path.join(test_dir, "sample_data/test_metadata.xlsx")
    ldr = loader.AudioTaggerMetadataLoader(src)
    metadata = ldr.load_metadata_df()
    out = at_out.AudioTaggerOutput()
    out.set_metadata(metadata)
    return out


def test_save_dry_run(output_object):
    output_object.save()
