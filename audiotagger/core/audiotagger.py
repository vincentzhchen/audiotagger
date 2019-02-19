from audiotagger.data.fields import Fields as fld
from audiotagger.modifier.audiotagger_modifier import AudioTaggerModifier as atm


class AudioTagger(object):
    def __init__(self, input_data, logger, options):
        self.log = logger
        self.input_data = input_data
        self.options = options

    def execute(self):
        metadata = self.input_data.get_metadata()
        modifier = self.options.modifier

        # never modify paths
        cols = [c for c in metadata if c not in fld.PATH_COLS]

        # modify str cols only
        str_cols = [c for c in cols if eval(f"fld.{c}.INPUT_TYPE") == str]

        # apply standard modifiers
        metadata.loc[:, str_cols] = atm.strip_str(metadata.loc[:, str_cols])
        metadata.loc[:, str_cols] = atm.create_spacing_for_characters(
            metadata.loc[:, str_cols])

        # do this last after all the space insertions above
        metadata.loc[:, str_cols] = atm.remove_multiple_whitespace(
            metadata.loc[:, str_cols])

        # return metadata as is if there are no modifiers specified
        if modifier is None:
            return metadata

        if self.options.modifier:
            # TODO: apply modifiers here
            pass

        return metadata
