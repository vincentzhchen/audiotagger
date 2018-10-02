import os
from shutil import copy2


class CreatePlaylist(object):
    def __init__(self, playlist_dst_dir, logger, input_data, query=None):
        self.log = logger
        self.playlist_dst_dir = playlist_dst_dir
        self.metadata = input_data.get_metadata()
        self.metadata = self._determine_file_size(df_metadata=self.metadata)

    def get_file_size(self, path, unit="GB"):
        if unit.upper() == "GB":
            return os.path.getsize(path) / 1e9
        else:
            raise ValueError(f"UNIT {unit} is not supported.")

    def get_playlist_file_size(self):
        # TODO: rename the "ADD" column in the code and the input file
        return self.metadata.loc[self.metadata["ADD"] == 1, "FILE_SIZE"].sum()

    def _determine_file_size(self, df_metadata):
        df_metadata["FILE_SIZE"] = df_metadata["PATH"].apply(self.get_file_size)
        return df_metadata

    def _rename_file(self, df):
        pairs = list(zip(df["PATH"], df["NEW_PATH"]))
        for old, new in pairs:
            new_dir = os.path.dirname(new)
            if not os.path.isdir(new_dir):
                self.log.info(f"{new_dir} does not exist, creating it...")
                os.makedirs(new_dir)
            self.log.info(f"Renaming {old} to {new}")
            copy2(old, new)

    def create_playlist(self):
        playlist = self.metadata.loc[self.metadata["ADD"] == 1]
        playlist["PATH_LIST"] = playlist["PATH"].apply(lambda x: x.split("/"))
        playlist["NEW_PATH"] = playlist["PATH_LIST"].apply(
            lambda x: os.path.join(self.playlist_dst_dir, x[-3], x[-2], x[-1]))
        self._rename_file(df=playlist)