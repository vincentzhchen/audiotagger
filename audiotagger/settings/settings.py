import importlib.util
import os
import sys

from audiotagger.core.paths import audiotagger_config_path

if os.path.exists(audiotagger_config_path()):
    spec = importlib.util.spec_from_file_location("audiotagger",
                                                  audiotagger_config_path())
    c = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(c)

    # Setup constants.
    LOG_DIRECTORY = c.LOG_DIRECTORY
    AUDIO_DIRECTORY = c.AUDIO_DIRECTORY
else:
    print("No configuration file found... exiting process...")
    sys.exit(1)
