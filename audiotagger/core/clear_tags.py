from audiotagger.data.fields import Fields as fld


class ClearTags(object):
    """Remove tags from audio files.

    The implementation overwrites existing tags with a tag metadata dataframe.

    """

    def __init__(self, input_data, logger, options):
        self.input_data = input_data
        self.log = logger
        self.options = options

    def execute(self):
        df = self.input_data.get_metadata()

        if self.options.clear_tags == "all":
            df = self.clear_all_tags()

        if self.options.clear_tags == "excess":
            df = self.clear_excess_tags()

        return df

    def clear_all_tags(self):
        """Clear all tags.

        Returns:
            metadata (dataframe): Returns metadata df with no tag columns.
        """
        metadata = self.input_data.get_metadata()
        metadata = metadata.loc[:, fld.PATH_COLS]
        self.log.info("ALL TAGS are cleared.")
        return metadata

    def clear_excess_tags(self):
        """Clear all tags not part of the base set of desired metadata.

        Returns:
            metadata (dataframe): Returns metadata df with base tag columns.
        """
        metadata = self.input_data.get_metadata()
        metadata = metadata.loc[:, fld.BASE_METADATA_COLS]
        self.log.info("ALL TAGS except base metadata are cleared.")
        return metadata
