import pandas as pd


def write_to_excel(df, file_path, sheet_name="metadata"):
    """Write dataframe to Excel file.

    This is expected to be used for writing metadata dataframes.

    Args:
        df (dataframe): Input dataframe.
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
