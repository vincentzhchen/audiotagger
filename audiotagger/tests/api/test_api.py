# pylint: disable=missing-module-docstring
# pylint: disable=redefined-outer-name
# pylint: disable=line-too-long
# pylint: disable=invalid-name
import os
import pathlib

import pytest

from audiotagger.api import api
from audiotagger.util import audiotagger_logger

logger = audiotagger_logger.get_logger(name="test_audiotagger.log")


@pytest.fixture
def api_instance():
    """API instance initialized with dummy metadata file.

    This cannot save to audio file.

    """
    test_dir = pathlib.Path(__file__).parent.parent
    src = os.path.join(test_dir, "sample_data/test_metadata.xlsx")
    at = api.AudioTaggerAPI(src=src)
    return at


def test_default_run(api_instance):
    api_instance.run()


def test_modify_tags(api_instance):
    api_instance.run(modify_tags=True)


def test_modify_tags_output_to_excel(api_instance):
    api_instance.run(modify_tags=True, output_to_excel=True)
