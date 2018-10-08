import os
import pandas as pd
from audiotagger.core.paths import audiotagger_config_dir
from audiotagger.data.fields import Fields as fld


def generate_metadata_template(dst_dir=None):
    if dst_dir is None:
        dst_dir = audiotagger_config_dir()

    if os.path.isdir(dst_dir):
        dst = os.path.join(dst_dir, "metadata.xlsx")
        print(f"Generating metadata file at {dst} ... ", end="")

        df = pd.DataFrame(columns=[fld.PATH] + fld.BASE_METADATA_COLS)
        df.to_excel(dst, index=False)
        print("done.")
    else:
        raise Exception(f"{dst_dir} does not exist.")
