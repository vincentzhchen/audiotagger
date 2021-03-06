# SPDX-License-Identifier: GPL-3.0-or-later
"""Handles all file copying and moving.

TODO: need better module name.

"""

import os

from audiotagger.data import fields as fld
from audiotagger.util import audiotagger_logger, file_util as futil


class CopyFile():

    def __init__(self, input_data, logger=None):
        self.input_data = input_data
        self.logger = logger if (
            logger is not None) else audiotagger_logger.get_logger()

    def execute(self, base_dir):
        metadata = self.input_data.get_metadata()

        metadata = self.generate_new_file_path_from_metadata(metadata, base_dir)

        # filter out only new paths
        metadata = metadata.loc[
            metadata[fld.PATH_SRC.CID] != metadata[fld.PATH_DST.CID]]
        return metadata

    def generate_new_file_path_from_metadata(self, df, base_dir):
        """Create new destination path from metadata.

        Args:
          df (pd.DataFrame): Metadata dataframe.
            base_dir (str): The base directory of the output audio file.

        Returns:
          anonymous (str): Returns a destination path for the file.
        """

        def join_metadata_path(metadata_tuple):
            """Helper function to create a path.

            Args:
              metadata_tuple (tuple of str): A tuple in the form
                (album_artist, year, album, disc, track, title, file_ext)

            Returns:
              path (str): Returns output audio file path.
            """
            # this is the default structure
            album_artist, year, album, disc, track, title, file_ext = metadata_tuple

            # fix invalid characters
            album_artist = futil.replace_invalid_characters(album_artist)
            album = futil.replace_invalid_characters(album)
            title = futil.replace_invalid_characters(title)

            path = os.path.join(base_dir, album_artist, year + " " + album,
                                disc + "." + track + " " + title + file_ext)
            return path

        df[fld.PATH_DST.CID] = tuple(
            zip(
                df[fld.ALBUM_ARTIST.CID], df[fld.YEAR.CID], df[fld.ALBUM.CID],
                df[fld.DISC_NO.CID].astype(str),
                df[fld.TRACK_NO.CID].astype(str).str.pad(2,
                                                         side="left",
                                                         fillchar="0"),
                df[fld.TITLE.CID],
                df[fld.PATH_SRC.CID].apply(futil.get_file_extension)))
        df[fld.PATH_DST.CID] = df[fld.PATH_DST.CID].apply(join_metadata_path)
        df = df.sort_values(fld.PATH_DST.CID)
        return df
