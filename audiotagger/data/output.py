import os

import pandasdateutils as pdu
from audiotagger.settings import settings
from audiotagger.util.tag_util import TagUtil
from audiotagger.util.input_output_util import InputOutputUtil


class AudioTaggerOutput(object):
    def __init__(self, metadata, logger, options):
        self.metadata = metadata
        self.log = logger
        self.options = options

        if self.options.write_to_excel:
            base_dir = settings.LOG_DIRECTORY
            file_path = os.path.join(
                base_dir, f"output_{pdu.now(as_string=True)}.xlsx")
            InputOutputUtil.write_to_excel(df=self.metadata,
                                           file_path=file_path)

    def save(self):
        if self.options.dry_run:
            self.log.info("DRY RUN -- do not modify audio files.")
        else:
            self.save_tags_to_audio_files()

    def save_tags_to_audio_files(self):
        metadata = self.metadata
        tag_dict = TagUtil.metadata_to_tags(df_metadata=metadata)
        for k in tag_dict:
            self.log.info(f"Saving {tag_dict[k]} to {k}")
            tag_dict[k].save(k)
