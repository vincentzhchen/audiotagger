import os
from mutagen.mp4 import MP4Tags
from audiotagger.data.fields import Fields as fld
from audiotagger.utils.utils import AudioTaggerUtils


class ClearTags(object):
    def __init__(self, logger, input_data):
        self.log = logger
        self.input_data = input_data
        self.utils = AudioTaggerUtils()

    def clear_all_tags(self):
        tags = MP4Tags()
        for path in self.input_data.get_all_audio_file_paths():
            self.log.info(f"Cleared tag for {path}")
            tags.save(path)

    def clear_non_main_tags(self):
        metadata = self.input_data.get_metadata()
        metadata = metadata[fld.MAIN_FIELDS]
        tag_dict = self.utils.metadata_to_tags(df_metadata=metadata)
        for k in tag_dict:
            self.log.info(f"Saving {tag_dict[k]} to {k}")
            tag_dict[k].save(k)
