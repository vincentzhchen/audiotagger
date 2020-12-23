# SPDX-License-Identifier: GPL-3.0-or-later
"""Loaders for various sources.

"""
import os

import pandas as pd

# PROJECT LIB
from audiotagger.data import fields as fld, processing
from audiotagger.util import (audiotagger_logger, file_util as futil)


class AudioTaggerMetadataLoader():
  """Loads all metadata from source.

  This should be separated from AudioTaggerInput
  since it is getting complicated.  The loader
  always returns a loaded data set, and the input
  would set as needed.

  """

  def __init__(self, src, logger=None):
    if not isinstance(src, str):
      raise Exception("INVALID SOURCE")

    self.src = src
    self.logger = logger if (
        logger is not None) else audiotagger_logger.get_logger()

  def load_metadata_df(self):
    """Loads metadata dataframe.

    This routes the source to the correct underlying loader.

    Returns:
      metadata (pd.DataFrame): Returns a metadata dataframe.
    """

    # for Excel metadata files
    if futil.is_xlsx(self.src):
      if not os.path.exists(self.src):
        raise ValueError(f"{self.src} does not exist.")

      # load metadata
      metadata = self._load_all_m4a_files_into_df_from_excel()

      # let external processor figure out how to clean the data and
      # get it into the correct form
      processor = processing.RawDataProcessor(self.logger)
      metadata = processor.process_loaded_metadatafile_data(metadata)

    # for directory of audio files or a single audio file
    elif os.path.isdir(self.src) or os.path.isfile(self.src):
      if not os.path.exists(self.src):
        raise ValueError(f"{self.src} does not exist.")

      # load metadata
      metadata = self._load_all_m4a_files_into_df_from_path()

      # let external processor figure out how to clean the data and
      # get it into the correct form
      processor = processing.RawDataProcessor(self.logger)
      metadata = processor.process_loaded_m4a_data(metadata)

    else:
      raise Exception("INVALID SOURCE")

    return metadata

  def _load_all_m4a_files_into_df_from_excel(self):
    """Load metadata from a metadata file into a dataframe.

    Returns:
      metadata (pd.DataFrame): Returns a metadata dataframe.
    """
    metadata = pd.read_excel(self.src,
                             sheet_name="metadata",
                             dtype=str,
                             engine="openpyxl")
    return metadata

  def _load_all_m4a_files_into_df_from_path(self):
    """Load metadata from m4a files into a dataframe.

    Returns:
      metadata (pd.DataFrame): Returns a metadata dataframe.
    """
    m4a_file_paths = futil.traverse_directory(self.src, "m4a")
    self.logger.info("LOADED %s file paths.", len(m4a_file_paths))
    if not m4a_file_paths:
      raise Exception("No m4a files found, exiting program.")

    metadata_records = futil.generate_metadata_records(m4a_file_paths)
    self.logger.info("LOADED %s records.", len(metadata_records))

    metadata = pd.DataFrame(metadata_records)
    metadata = metadata.rename(columns={
        "PATH_SRC": fld.PATH_SRC.CID,
        "PATH_DST": fld.PATH_DST.CID,
    })
    self.logger.info("LOADED raw metadata df, shape: %s.", metadata.shape)

    return metadata
