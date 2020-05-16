"""Handles all deletion of tags.

"""

# PROJECT LIB
from audiotagger.data import fields as fld
from audiotagger.util import audiotagger_logger


class ClearTags():
    """Remove tags from audio files.

    The implementation overwrites existing tags with a tag metadata dataframe.

    """
    def __init__(self, input_data, logger=None):
        """This class requires an input data to operate on.

        """
        self.input_data = input_data
        self.logger = logger if (
            logger is not None) else audiotagger_logger.get_logger()

    def execute(self, clear_type):
        """The caller chooses how class method gets executed.

        Args:
            clear_type (str): `all` will delete all tags and `excess` will
                delete all tags not part of the base set of desired metadata.

        Returns:
            metadata (pd.DataFrame): Returns metadata df.
        """
        metadata = self.input_data.get_metadata()

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
            df (pd.DataFrame): Returns metadata df with no tag columns.
        """
        df = df.loc[:, fld.PATH_COLS]
        self.logger.info("ALL TAGS are cleared.")
        return df

    def clear_excess_tags(self, df):
        """Clear all tags not part of the base set of desired metadata.

        Args:
            df (pd.DataFrame): Metadata dataframe.

        Returns:
            df (pd.DataFrame): Returns metadata df with base tag columns.
        """
        df = df.loc[:, fld.BASE_METADATA_COLS]
        self.logger.info("ALL TAGS except base metadata are cleared.")
        return df
