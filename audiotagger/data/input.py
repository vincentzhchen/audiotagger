import os
import pandas as pd

from audiotagger.util.file_util import FileUtil
from audiotagger.util.tag_util import TagUtil


class AudioTaggerInput(object):
    def __init__(self, src, logger):
        if src is None:
            raise Exception("INVALID SOURCE")
        else:
            self.src = src

        self.log = logger

        # for Excel metadata files
        if FileUtil.is_xlsx(self.src):
            if not os.path.exists(self.src):
                raise ValueError(f"{self.src} does not exist.")

            # load inputs
            self._load_all_m4a_files_into_df_from_excel()

        # for directory of audio files or a single audio file
        elif os.path.isdir(self.src) or os.path.isfile(self.src):
            if not os.path.exists(self.src):
                raise ValueError(f"{self.src} does not exist.")

            # load inputs
            self._load_all_m4a_files_into_df_from_path()

        else:
            raise Exception("INVALID SOURCE")

        self.metadata = TagUtil.sort_metadata(self.metadata)

    def _load_all_m4a_files_into_df_from_excel(self):
        metadata = pd.read_excel(self.src, sheet_name="metadata", dtype=str)
        metadata = TagUtil.enforce_dtypes(df=metadata,
                                          io_type="INPUT_FROM_METADATA_FILE")
        self.metadata = metadata

    def _load_all_m4a_files_into_df_from_path(self):
        """Load metadata from m4a files into a dataframe.

        """
        self.log.info("Loading all m4a file paths")
        m4a_file_paths = FileUtil.traverse_directory(self.src, "m4a")
        self.log.info(f"LOADED {len(m4a_file_paths)} file paths.")

        # The file path is used to create an MP4 object and is stored
        # as a (file_path, MP4 obj) tuple.
        self.log.info("Loading all m4a objects...")
        m4a_obj = FileUtil.convert_to_mp4_obj(m4a_file_paths)
        self.log.info(f"LOADED {len(m4a_obj)} m4a objects.")

        self.log.info("Loading all audio file metadata into dataframe...")
        m4a_obj = [dict(song.tags, **{"PATH": [song.filename]})
                   for song in m4a_obj]
        metadata = pd.DataFrame(m4a_obj)

        # mutagen stores all tags in lists; flatten them
        metadata = TagUtil.flatten_list_values(metadata)
        metadata = TagUtil.clean_metadata(df_metadata=metadata)
        metadata = TagUtil.enforce_dtypes(df=metadata,
                                          io_type="INPUT_FROM_AUDIO_FILE")
        self.metadata = metadata

    def get_metadata(self):
        df = self.metadata
        return df
