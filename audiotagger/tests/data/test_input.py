# STANDARD LIB
import os
import unittest

# DEPENDENCIES
import customlogging as cl

# PROJECT LIB
from audiotagger.core import paths
from audiotagger.data import fields
from audiotagger.data import input as at_in

# ALIAS
fld = fields.Fields()

logger = cl.initialize_logger(paths.audiotagger_log_dir(),
                              "test_audiotagger_input.log")


class TestAudioTaggerInput(unittest.TestCase):
    def setUp(self):
        self.test_dir = os.path.join(
            paths.audiotagger_test_dir(), "test_files")

    def test_get_metadata_001(self):
        """Test getting metadata from audio files."""
        input_data = at_in.AudioTaggerInput(self.test_dir, logger)
        metadata = input_data.get_metadata()
        self.assertTrue(set(fld.BASE_METADATA_COLS).difference(
            metadata.columns.tolist()) == set())

    def test_get_metadata_002(self):
        """Test getting metadata from audio files, with Excel writing."""
        input_data = at_in.AudioTaggerInput(self.test_dir, logger,
                                            to_excel=True)
        metadata = input_data.get_metadata()
        self.assertTrue(set(fld.BASE_METADATA_COLS).difference(
            metadata.columns.tolist()) == set())
