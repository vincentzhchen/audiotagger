# PROJECT LIB
from audiotagger.data import fields

# ALIAS
fld = fields.Fields()


class ClearTags(object):
    """Remove tags from audio files.

    The implementation overwrites existing tags with a tag metadata dataframe.

    """

    def __init__(self, input_data, logger, options):
        self.input_data = input_data
        self.log = logger
        self.options = options

    def execute(self):
        metadata = self.input_data.get_metadata()
        clear_type = self.options.clear_tags

        if clear_type == "all":
            metadata = self.clear_all_tags(df=metadata)

        elif clear_type == "excess":
            metadata = self.clear_excess_tags(df=metadata)

        return metadata

    def clear_all_tags(self, df):
        """Clear all tags.

        Args:
            df (pd.DataFrame): Metadata dataframe.

        Returns:
            metadata (pd.DataFrame): Returns metadata df with
                no tag columns.
        """
        df = df.loc[:, fld.PATH_COLS]
        self.log.info("ALL TAGS are cleared.")
        return df

    def clear_excess_tags(self, df):
        """Clear all tags not part of the base set of desired metadata.

        Args:
            df (pd.DataFrame): Metadata dataframe.

        Returns:
            metadata (pd.DataFrame): Returns metadata df with base
                tag columns.
        """
        df = df.loc[:, fld.BASE_METADATA_COLS]
        self.log.info("ALL TAGS except base metadata are cleared.")
        return df
