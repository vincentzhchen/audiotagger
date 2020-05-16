"""General setup methods.

"""
import os
import shutil

import pandas as pd

from audiotagger.core import paths
from audiotagger.data import fields as fld
from audiotagger.util import audiotagger_logger


def generate_config():
    """Generates application config file in HOME directory.

    """
    # there is no log directory at this point (config is assumed to not exist)
    logger = audiotagger_logger.get_logger()

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
            f.write(f"AUDIO_DIRECTORY=None"
                    '\n'
                    f"DATA_DIRECTORY='{paths.audiotagger_data_dir()}'\n")
        logger.info("Generated config at %s", paths.audiotagger_config_path())
    else:
        logger.info("No configuration was generated.")


def generate_metadata_template(dst_dir=None):
    """Generates blank metadata template.

    Args:
        dst_dir (str, default None): If a destination directory is passed,
            the file will be generated in the given directory, otherwise,
            it will be generated in the default data directory.

    """
    logger = audiotagger_logger.get_logger(paths.audiotagger_log_dir())

    if dst_dir is None:
        dst_dir = paths.audiotagger_data_dir()

    if os.path.isdir(dst_dir):
        now = pd.to_datetime("today").strftime("%Y%m%d_%H%M%S")
        dst = os.path.join(dst_dir, f"metadata_{now}.xlsx")
        logger.info("Generating metadata file at %s", dst)

        df = pd.DataFrame(columns=fld.BASE_METADATA_COLS)
        df.to_excel(dst, sheet_name="metadata", index=False)
    else:
        raise Exception(f"{dst_dir} does not exist.")
