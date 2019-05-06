# STANDARD LIB
import os

# PROJECT LIB
from audiotagger.data import fields
from audiotagger.settings import settings as at_settings
from audiotagger.util import file_util as futil

# ALIAS
fld = fields.Fields


class CopyFile(object):
    def __init__(self, input_data, logger, options):
        self.input_data = input_data
        self.log = logger
        self.options = options

    def execute(self):
        metadata = self.input_data.get_metadata()

        base_dir = self.options.dst
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
        if base_dir is not None:
            base_dst_dir = base_dir
        else:
            base_dst_dir = at_settings.AUDIO_DIRECTORY

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

            path = os.path.join(base_dst_dir,
                                album_artist,
                                year + " " + album,
                                disc + "." + track + " " + title + file_ext)
            return path

        df[fld.PATH_DST.CID] = tuple(zip(
            df[fld.ALBUM_ARTIST.CID],
            df[fld.YEAR.CID],
            df[fld.ALBUM.CID],
            df[fld.DISC_NO.CID].astype(str),
            df[fld.TRACK_NO.CID].astype(
                str).str.pad(2, side="left", fillchar="0"),
            df[fld.TITLE.CID],
            df[fld.PATH_SRC.CID].apply(futil.get_file_extension)))
        df[fld.PATH_DST.CID] = df[fld.PATH_DST.CID].apply(join_metadata_path)
        df = df.sort_values(fld.PATH_DST.CID)
        return df
