import os
import pandas as pd

from audiotagger.data.fields import Fields as fld
from audiotagger.settings import settings
import pandasdateutils as pdu


def generate_metadata_template(dst_dir=None):
    if dst_dir is None:
        dst_dir = settings.LOG_DIRECTORY

    if os.path.isdir(dst_dir):
        now = pdu.now(as_string=True)
        dst = os.path.join(dst_dir, f"metadata_{now}.xlsx")
        print(f"Generating metadata file at {dst} ... ", end="")

        df = pd.DataFrame(columns=fld.BASE_METADATA_COLS)
        df.to_excel(dst, sheet_name="metadata", index=False)
        print("done.")
    else:
        raise Exception(f"{dst_dir} does not exist.")
