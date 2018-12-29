from mutagen.mp4 import MP4Tags
from audiotagger.data.fields import Fields as fld
from audiotagger.util.file_util import FileUtil
from audiotagger.util.tag_util import TagUtil


class ClearTags(object):
    def __init__(self, logger, input_data):
        self.log = logger
        self.input_data = input_data
        self.utils = FileUtil()

    def clear_all_tags(self):
        """Clear all tags.

        """
        for path in self.input_data.get_all_audio_file_paths():
            self.log.info(f"Cleared tag for {path}")
            MP4Tags().save(path)

    def clear_excess_tags(self):
        """Clear all tags not part of the base set of desired metadata.

        """
        metadata = self.input_data.get_metadata()
        metadata = metadata[fld.BASE_METADATA_COLS]
        tag_dict = TagUtil.metadata_to_tags(df_metadata=metadata)
        for k in tag_dict:
            self.log.info(f"Saving {tag_dict[k]} to {k}")
            tag_dict[k].save(k)
