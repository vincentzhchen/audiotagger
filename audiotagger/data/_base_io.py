"""Base structure for input / output.

"""

# STANDARD LIB
import abc
import pandas as pd

# PROJECT LIB
from audiotagger.data import fields
from audiotagger.util import audiotagger_logger

# ALIAS
fld = fields.Fields


class AudioTaggerBaseInputOutput(abc.ABC):
    """Contains all the methods that an input / output would need to implement.

    """
    def __init__(self, logger):
        self.logger = logger if (
            logger is not None) else audiotagger_logger.get_logger()

        self.metadata = pd.DataFrame()

    @abc.abstractmethod
    def write_to_excel(self):
        """All IO classes should allow to write to an Excel file.

        """
        raise NotImplementedError

    @abc.abstractmethod
    def write_to_csv(self):
        """All IO classes should allow to write to a csv file.

        """
        raise NotImplementedError

    @abc.abstractmethod
    def set_metadata(self, df):
        """Use a setter to enforce the metadata dataframe structure.

        """
        cols = set(fld.BASE_METADATA_COLS).difference(df.columns)
        if cols == set():
            self.metadata = df
        else:
            raise ValueError(f"FAILED to set metadata df, missing {cols}.")
