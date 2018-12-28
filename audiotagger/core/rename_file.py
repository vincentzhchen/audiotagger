import os
from shutil import copy2

from audiotagger.data.fields import Fields as fld
from audiotagger.utils.utils import FileUtils


class RenameFile(object):
    def __init__(self, base_dst_dir, logger, input_data):
        """

        Args:
            base_dst_dir (str): The base directory for the output.  This
                is typically the folder where all music is stored at the
                artist level.
            input_data (AudioTaggerInput): Holds all needed input data.
        """
        self.base_dst_dir = base_dst_dir
        self.log = logger
        self.input_data = input_data

        self.metadata = input_data.get_metadata()
        self.modified_metadata = self.generate_new_file_path_from_metadata(
            df_metadata=self.metadata)

    def __str__(self):
        return "rename_file"

    def _join_metadata_path(self, metadata_tuple):
        """Helper function to create the new path.

        Args:
            metadata_tuple (tuple): A tuple of metadata fields to be included
                in the file path.

        Returns:
            anonymous (str): Returns a destination path for the file.
        """
        artist, year, album, disc, track, title, ext = metadata_tuple
        artist = FileUtils.replace_invalid_characters(artist)
        album = FileUtils.replace_invalid_characters(album)
        title = FileUtils.replace_invalid_characters(title)
        return os.path.join(self.base_dst_dir,
                            artist,
                            year + " " + album,
                            disc + "." + track + " " + title + ext)

    def generate_new_file_path_from_metadata(self, df_metadata):
        df_metadata["NEW_PATH"] = tuple(zip(
            df_metadata[fld.ALBUM_ARTIST.CID],
            df_metadata[fld.YEAR.CID],
            df_metadata[fld.ALBUM.CID],
            df_metadata[fld.DISC_NO.CID].astype(str),
            df_metadata[fld.TRACK_NO.CID].astype(str).str.pad(2, side="left",
                                                              fillchar="0"),
            df_metadata[fld.TITLE.CID],
            df_metadata["PATH"].apply(lambda x: os.path.splitext(x)[1])
        ))
        df_metadata["NEW_PATH"] = df_metadata["NEW_PATH"].apply(
            self._join_metadata_path)
        df_metadata = df_metadata.sort_values("NEW_PATH")
        return df_metadata[[fld.PATH.CID, "NEW_PATH"]]

    def _rename_file(self):
        df = self.modified_metadata
        pairs = list(zip(df[fld.PATH.CID], df["NEW_PATH"]))
        for old, new in pairs:
            new_dir = os.path.dirname(new)
            if not os.path.isdir(new_dir):
                self.log.info(f"{new_dir} does not exist, creating it...")
                os.makedirs(new_dir)
            self.log.info(f"Renaming {old} to {new}")
            copy2(old, new)

    def rename_file(self):
        if self.input_data.is_dry_run:
            self.log.info("Dry run... saving to {out_file}.")
            FileUtils.dry_run(df=self.modified_metadata,
                              prefix=self.__str__())
            self.log.info("Data saved to {out_file}")
            return
        else:
            self._rename_file()
