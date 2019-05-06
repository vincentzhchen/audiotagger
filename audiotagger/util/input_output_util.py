# STANDARD LIB
import os
import pandas as pd

# DEPENDENCIES
import pandasdateutils as pdu

# PROJECT LIB
from audiotagger.core import paths
from audiotagger.data import fields

# ALIAS
fld = fields.Fields()


def generate_excel_path(context):
    base_dir = paths.audiotagger_data_dir()
    context += f"_{pdu.now(as_string=True)}.xlsx"
    file_path = os.path.join(base_dir, context)
    return file_path


def write_to_excel(df, file_path, sheet_name="metadata"):
    """Write dataframe to Excel file.

    Args:
        df (pd.DataFrame): Input dataframe.
        file_path (str): Output file path to write the data to.
        sheet_name (str): Name of the dataframe.

    Returns:
        void
    """
    writer = pd.ExcelWriter(file_path,
                            date_format="YYYY-MM-DD",
                            datetime_format="YYYY-MM-DD")

    df.to_excel(writer, sheet_name=sheet_name,
                index=False, encoding="utf-8")

    writer.save()


def write_metadata_to_excel(df, file_path, ignore_cover=True):
    """Write metadata dataframe to Excel file.

    Args:
        df (pd.DataFrame): Metadata dataframe.
        file_path (str): Output file path to write data to.
        ignore_cover (bool): If True, do not write the cover column,
            which contains a bit stream value.

    Returns:
        void
    """
    if ignore_cover:
        df = df.drop(columns=fld.COVER.CID, errors="ignore")

    return write_to_excel(df=df, file_path=file_path, sheet_name="metadata")
