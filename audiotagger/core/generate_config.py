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
            f.write("LOG_DIRECTORY = '{}'".format(audiotagger_config_dir()))
        print("Generated config at {}".format(audiotagger_config_dir()))
