import os
import shutil

from audiotagger.core import paths


def generate_config():
    """Generates application config file in HOME directory.

    """

    # If config directory exists, ask if user wants to start over.
    start_over = "y"
    if os.path.exists(paths.audiotagger_config_dir()):
        start_over = input("A previous configuration already exists. Would "
                           "you like to start over?  NOTE: this deletes all "
                           "logs and input/output data files. [y/N] \n")

        if start_over.lower() == "y":
            shutil.rmtree(paths.audiotagger_config_dir())

    if start_over.lower() == "y":
        # default directories for audiotagger application
        os.makedirs(paths.audiotagger_config_dir())
        os.makedirs(paths.audiotagger_log_dir())
        os.makedirs(paths.audiotagger_data_dir())
        os.makedirs(paths.audiotagger_test_dir())

        config_file = paths.audiotagger_config_path()
        with open(config_file, "w") as f:
            f.write(f"AUDIO_DIRECTORY=None"'\n'
                    f"DATA_DIRECTORY='{paths.audiotagger_data_dir()}'\n")
        print(f"Generated config at {paths.audiotagger_config_path()}")
    else:
        print("No configuration was generated.")
