# STANDARD LIB
import abc

# PROJECT LIB
from audiotagger.data import fields

# ALIAS
fld = fields.Fields


class AudioTaggerBaseInputOutput(abc.ABC):
    def __init__(self, logger):
        self.log = logger

    @abc.abstractmethod
    def write_to_excel(self):
        """All IO classes should allow to write to an Excel file."""
        pass

    @abc.abstractmethod
    def write_to_csv(self):
        """All IO classes should allow to write to a csv file."""
        pass

    @abc.abstractmethod
    def set_metadata(self, df):
        """Use a setter to enforce the metadata dataframe structure."""
        cols = set(fld.BASE_METADATA_COLS).difference(df.columns)
        if cols == set():
            self.metadata = df
        else:
            raise ValueError(f"FAILED to set metadata df, missing {cols}.")
