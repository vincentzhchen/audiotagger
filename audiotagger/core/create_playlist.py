import os
import pandas as pd
import sqlite3

from audiotagger.data.fields import Fields as fld
from audiotagger.util import file_util as futil


class CreatePlaylist(object):
    def __init__(self, input_data, logger, options):
        self.input_data = input_data
        self.log = logger
        self.options = options

    def execute(self):
        metadata = self.input_data.get_metadata()
        metadata[fld.PATH_DST.CID] = self.options.dst

        # create in-memory DB to run SQL queries against
        connection = sqlite3.connect(":memory:")
        metadata.to_sql("METADATA", con=connection)

        # get query
        if os.path.exists(self.options.playlist_query):
            query = futil.parse_sql_query(self.options.playlist_query)
        else:
            query = self.options.playlist_query
        self.log.info("Execute the following query: \n" + query)

        # query dataframe
        metadata = pd.read_sql_query(query, con=connection)

        return metadata

    def get_playlist_file_size(self, df):
        # TODO: rename the "ADD" column in the code and the input file
        return df.loc[df["ADD"] == 1, "FILE_SIZE"].sum()

    def _determine_file_size(self, df_metadata):
        df_metadata["FILE_SIZE"] = df_metadata[
            fld.PATH_SRC.CID].apply(self.get_file_size)
        return df_metadata
