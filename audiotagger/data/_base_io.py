# SPDX-License-Identifier: GPL-3.0-or-later
"""Base structure for input / output.

"""
import abc

import pandas as pd

from audiotagger.data import fields as fld
from audiotagger.util import audiotagger_logger


class AudioTaggerBaseInputOutput(abc.ABC):
  """Contains all the methods that an input / output would need to implement.

  """

  def __init__(self, logger=None):
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
    cols = set(fld.BASE_METADATA_COLS).difference(df)
    if cols == set():
      self.metadata = df
    else:
      raise ValueError(f"FAILED to set metadata df, missing {cols}.")
