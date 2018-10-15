import os
import pandas as pd
import pandasdateutils as pdu
from audiotagger.core.paths import audiotagger_config_dir
from audiotagger.data.fields import Fields as fld


def generate_metadata_template(dst_dir=None):
    if dst_dir is None:
        dst_dir = audiotagger_config_dir()

    if os.path.isdir(dst_dir):
        now = pdu.now(as_string=True)
        dst = os.path.join(dst_dir, f"metadata_{now}.xlsx")
        print(f"Generating metadata file at {dst} ... ", end="")

        df = pd.DataFrame(columns=[fld.PATH] + fld.BASE_METADATA_COLS)
        df.to_excel(dst, sheet_name="metadata", index=False)
        print("done.")
    else:
        raise Exception(f"{dst_dir} does not exist.")
