# SPDX-License-Identifier: GPL-3.0-or-later
"""All tagging takes place here.

"""
from audiotagger.data import fields as fld
from audiotagger.modifier import audiotagger_modifier as atm
from audiotagger.util import audiotagger_logger


class AudioTagger():
    """Main tagging class.

    """

    def __init__(self, input_data, logger=None):
        self.logger = logger if (
            logger is not None) else audiotagger_logger.get_logger()
        self.input_data = input_data

    def execute(self, modifier=None):
        """Implementation.

        Args:
          modifier (str, default None): modifier type to apply.

        Returns:
          metadata (pd.DataFrame): Returns metadata df.
        """
        metadata = self.input_data.get_metadata()

        # never modify paths or special columns (e.g. cover art)
        cols = [c for c in metadata if c not in fld.PATH_COLS + fld.COVER_COLS]

        # modify str cols only
        str_cols = [c for c in cols if getattr(fld, c).INPUT_TYPE == str]

        metadata = self._apply_standard_modifiers(metadata, str_cols)

        if modifier is not None:
            # apply other modifier methods here
            raise NotImplementedError

        return metadata

    def _apply_standard_modifiers(self, metadata, str_cols):
        """Standard tag modifications done here.

        """
        # apply standard modifiers
        self.logger.info("Stripping whitespaces from string cols.")
        metadata.loc[:, str_cols] = atm.strip_str(metadata.loc[:, str_cols])

        self.logger.info("Add spacing for brackets and other special chars.")
        metadata.loc[:, str_cols] = atm.create_spacing_for_characters(
            metadata.loc[:, str_cols])

        # do this last after all the space insertions above
        self.logger.info("Remove extra spaces between words.")
        metadata.loc[:, str_cols] = atm.remove_multiple_whitespace(
            metadata.loc[:, str_cols])

        return metadata
