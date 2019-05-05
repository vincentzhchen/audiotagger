# STANDARD LIB
import importlib.util
import os
import sys

# PROJECT LIB
from audiotagger.core import paths

config_path = paths.audiotagger_config_path()
if os.path.exists(config_path):
    spec = importlib.util.spec_from_file_location("audiotagger", config_path)
    c = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(c)

    # Setup constants.
    AUDIO_DIRECTORY = c.AUDIO_DIRECTORY
    DATA_DIRECTORY = c.DATA_DIRECTORY
else:
    print("No configuration file found... exiting process...")
    sys.exit(1)
