import os

from audiotagger.data.fields import Fields as fld
from audiotagger.settings import settings
from audiotagger.util import file_util as futil
from audiotagger.util import tag_util as tutil


class CopyFile(object):
    def __init__(self, input_data, logger, options):
        self.input_data = input_data
        self.log = logger
        self.options = options

        self.generate_base_dst_dir()

    def execute(self):
        metadata = self.input_data.get_metadata()
        metadata = self.generate_new_file_path_from_metadata(df=metadata)

        # filter out only new paths
        metadata = metadata.loc[
            metadata[fld.PATH_SRC.CID] != metadata[fld.PATH_DST.CID]]
        return metadata

    def generate_base_dst_dir(self):
        if self.options.dst is not None:
            self.base_dst_dir = self.options.dst
        else:
            # TODO: for now, always save to the audio directory.
            self.base_dst_dir = settings.AUDIO_DIRECTORY

    def _join_metadata_path(self, metadata_tuple):
        album_artist, year, album, disc, track, title, file_ext = metadata_tuple
        album_artist = futil.replace_invalid_characters(album_artist)
        album = futil.replace_invalid_characters(album)
        title = futil.replace_invalid_characters(title)
        return os.path.join(self.base_dst_dir,
                            album_artist,
                            year + " " + album,
                            disc + "." + track + " " + title + file_ext)

    def generate_new_file_path_from_metadata(self, df):
        """Create new destination path from metadata.

        Args:
            df (dataframe): Metadata dataframe.

        Returns:
            anonymous (str): Returns a destination path for the file.
        """
        df[fld.PATH_DST.CID] = tuple(zip(
            df[fld.ALBUM_ARTIST.CID],
            df[fld.YEAR.CID],
            df[fld.ALBUM.CID],
            df[fld.DISC_NO.CID].astype(str),
            df[fld.TRACK_NO.CID].astype(
                str).str.pad(2, side="left", fillchar="0"),
            df[fld.TITLE.CID],
            df[fld.PATH_SRC.CID].apply(futil.get_file_extension)))
        df[fld.PATH_DST.CID] = df[fld.PATH_DST.CID].apply(
            self._join_metadata_path)
        df = df.sort_values(fld.PATH_DST.CID)

        # since album art destination changes as the destination path changes,
        # generate the album art paths again
        df = tutil.generate_album_art_path(df=df)
        return df
