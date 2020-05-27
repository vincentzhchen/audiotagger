# SPDX-License-Identifier: GPL-3.0-or-later
import os
import sqlite3

import pandas as pd

from audiotagger.data import fields as fld
from audiotagger.util import audiotagger_logger, file_util as futil


class CreatePlaylist():
    def __init__(self, input_data, logger=None):
        self.input_data = input_data
        self.logger = logger if (
            logger is not None) else audiotagger_logger.get_logger()

    def execute(self, playlist_query, base_dir=None):
        metadata = self.input_data.get_metadata()
        metadata[fld.PATH_DST.CID] = base_dir

        # create in-memory DB to run SQL queries against
        connection = sqlite3.connect(":memory:")
        metadata.to_sql("METADATA", con=connection)

        # get query
        if os.path.exists(playlist_query):
            query = futil.parse_sql_query(playlist_query)
        else:
            query = playlist_query
        self.logger.info("Execute the following query: \n" + query)

        # query dataframe
        metadata = pd.read_sql_query(query, con=connection)

        return metadata

    def get_playlist_file_size(self, df):
        # TODO: rename the "ADD" column in the code and the input file
        return df.loc[df["ADD"] == 1, "FILE_SIZE"].sum()

    def _determine_file_size(self, df_metadata):
        df_metadata["FILE_SIZE"] = df_metadata[fld.PATH_SRC.CID].apply(
            self.get_file_size)
        return df_metadata
