import os
from shutil import copy2
from audiotagger.data.fields import Fields as fld


class RenameFile(object):
    def __init__(self, base_dst_dir, logger, input_data, dry_run=True):
        """

        Args:
            base_dst_dir (str): The base directory for the output.  This
                is typically the folder where all music is stored at the
                artist level.
            input_data (AudioTaggerInput): Holds all needed input data.
        """
        self.base_dst_dir = base_dst_dir
        self.log = logger
        self.metadata = input_data.get_metadata()
        self.dry_run = dry_run

    def _join_metadata_path(self, metadata_tuple):
        artist, year, album, disc, track, title, ext = metadata_tuple
        return os.path.join(self.base_dst_dir,
                            artist,
                            year + " " + album,
                            disc + "." + track + " " + title + ext)

    def generate_new_file_path_from_metadata(self, df_metadata):
        df_metadata["NEW_PATH"] = list(zip(
            df_metadata[fld.ALBUM_ARTIST],
            df_metadata[fld.YEAR],
            df_metadata[fld.ALBUM],
            df_metadata["DISC_NO"].astype(str),
            df_metadata["TRACK_NO"].astype(str).str.pad(2, side="left",
                                                        fillchar="0"),
            df_metadata[fld.TITLE],
            df_metadata["PATH"].apply(lambda x: os.path.splitext(x)[1])
        ))
        df_metadata["NEW_PATH"] = df_metadata["NEW_PATH"].apply(
            self._join_metadata_path)
        df_metadata = df_metadata.sort_values("NEW_PATH")
        return df_metadata

    def rename_file(self):
        df = self.generate_new_file_path_from_metadata(self.metadata)
        pairs = list(zip(df["PATH"], df["NEW_PATH"]))
        for old, new in pairs:
            new_dir = os.path.dirname(new)
            if not os.path.isdir(new_dir):
                self.log.info(f"{new_dir} does not exist, creating it...")
                os.makedirs(new_dir)
            self.log.info(f"Renaming {old} to {new}")
            copy2(old, new)