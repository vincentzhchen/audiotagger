import os
from audiotagger.core.paths import audiotagger_config_dir, \
    audiotagger_config_path


def generate_config():
    """Generates application config file in HOME directory."""
    config_file = audiotagger_config_path()

    if not os.path.exists(audiotagger_config_dir()):
        os.makedirs(audiotagger_config_dir())

    overwrite = "Y"
    if os.path.exists(config_file):
        overwrite = input("Config already exists... overwrite? [Y/n] \n")

    if overwrite != "n":
        with open(config_file, "w") as f:
            f.write(f"LOG_DIRECTORY='{audiotagger_config_dir()}'\n"
                    f"AUDIO_DIRECTORY=None"'\n')
        print(f"Generated config at {audiotagger_config_dir()}")
