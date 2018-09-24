import pandas as pd
from mutagen.mp4 import MP4Tags
from audiotagger.data.fields import Fields as fld
from audiotagger.utils.utils import AudioTaggerUtils


class ExcelTagger(object):
    def __init__(self, logger, input_data):
        self.log = logger
        self.metadata = input_data.get_metadata()
        self.utils = AudioTaggerUtils()

    def get_audio_files(self):
        paths = self.metadata["PATH"].tolist()
        m4a_obj = self.utils.convert_to_mp4_obj(paths)
        return m4a_obj

    def save_tags_to_audio_files(self):
        metadata = self.metadata
        tag_dict = self.utils.metadata_to_tags(df_metadata=metadata)
        for k in tag_dict:
            self.log.info(f"Saving {tag_dict[k]} to {k}")
            tag_dict[k].save(k)
