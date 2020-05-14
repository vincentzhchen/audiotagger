# STANDARD LIB
import os
import pandas as pd
import pathlib
import pytest

# PROJECT LIB
from audiotagger.api import api
from audiotagger.data import fields as fld, input as at_in
from audiotagger.util import audiotagger_logger

logger = audiotagger_logger.get_logger(name="test_audiotagger_api.log")


@pytest.fixture
def api_instance():
    test_dir = pathlib.Path(__file__).parent.parent
    src = os.path.join(test_dir, "sample_data/test_metadata.xlsx")
    at = api.AudioTaggerAPI(src=src)
    return at


def test_api_instantiation(api_instance):
    api_instance.run()
