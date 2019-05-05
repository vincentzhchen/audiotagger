# STANDARD LIB
import os
import pandas as pd
import shutil

# DEPENDENCIES
import pandasdateutils as pdu

# PROJECT LIB
from audiotagger.core import paths
from audiotagger.data import fields

# ALIAS
fld = fields.Fields()


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


def generate_metadata_template(dst_dir=None):
    if dst_dir is None:
        dst_dir = paths.audiotagger_data_dir()

    if os.path.isdir(dst_dir):
        now = pdu.now(as_string=True)
        dst = os.path.join(dst_dir, f"metadata_{now}.xlsx")
        print(f"Generating metadata file at {dst} ... ", end="")

        df = pd.DataFrame(columns=fld.BASE_METADATA_COLS)
        df.to_excel(dst, sheet_name="metadata", index=False)
        print("done.")
    else:
        raise Exception(f"{dst_dir} does not exist.")
