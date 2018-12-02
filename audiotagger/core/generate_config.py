import os
import shutil

from audiotagger.core.paths import (audiotagger_config_dir,
                                    audiotagger_config_path,
                                    audiotagger_log_dir)


def generate_config():
    """Generates application config file in HOME directory.

    """

    # If config directory exists, ask if user wants to start over.
    start_over = "y"
    if os.path.exists(audiotagger_config_dir()):
        start_over = input("A previous configuration already exists. Would "
                           "you like to start over?  NOTE: this deletes all "
                           "logs and input/output data files. [y/N] \n")

        if start_over.lower() == "y":
            shutil.rmtree(audiotagger_config_dir())

    if start_over.lower() == "y":
        os.makedirs(audiotagger_config_dir())
        os.makedirs(audiotagger_log_dir())

        config_file = audiotagger_config_path()
        with open(config_file, "w") as f:
            f.write(f"LOG_DIRECTORY='{audiotagger_log_dir()}'\n"
                    f"AUDIO_DIRECTORY=None"'\n')
        print(f"Generated config at {audiotagger_config_path()}")
    else:
        print("No configuration was generated.")
