from audiotagger.data.fields import Fields as fld
from audiotagger.util.tag_util import TagUtil


class ClearTags(object):
    """Remove tags from audio files.

    The implementation overwrites existing tags with a tag metadata dataframe.

    """
    def __init__(self, logger, input_data):
        self.log = logger
        self.input_data = input_data

    def clear_all_tags(self):
        """Clear all tags.

        """
        metadata = self.input_data.get_metadata()
        metadata = metadata.loc[:, [fld.PATH.CID]]
        TagUtil.save_tags_to_file(df_metadata=metadata)
        self.log.info("ALL TAGS are cleared.")

    def clear_excess_tags(self):
        """Clear all tags not part of the base set of desired metadata.

        """
        metadata = self.input_data.get_metadata()
        metadata = metadata.loc[:, fld.BASE_METADATA_COLS]
        TagUtil.save_tags_to_file(df_metadata=metadata)
        self.log.info("ALL TAGS except base metadata are cleared.")
