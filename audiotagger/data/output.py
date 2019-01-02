import os
from shutil import copy2

import pandasdateutils as pdu
from audiotagger.data.fields import Fields as fld
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
            self.log.info(f"Saved output metadata to {file_path}")

    def save(self):
        if self.options.dry_run:
            self.log.info("DRY RUN -- no files were modified.")
        else:
            self.save_tags_to_audio_files()

    def save_tags_to_audio_files(self):
        metadata = self.metadata
        tag_dict = TagUtil.metadata_to_tags(df=metadata)
        for k in tag_dict:
            self.log.info(f"Saving {tag_dict[k]} to {k}")
            tag_dict[k].save(k)

    def copy(self):
        if self.options.dry_run:
            self.log.info("DRY RUN -- no files were created.")
        else:
            self.copy_files()

    def copy_files(self):
        df = self.metadata
        pairs = list(zip(df[fld.PATH_SRC.CID], df[fld.PATH_DST.CID]))
        for old, new in pairs:
            # check if the new destination dir exists, if not then create it
            new_dir = os.path.dirname(new)
            if not os.path.isdir(new_dir):
                self.log.info(f"{new_dir} does not exist, creating it...")
                os.makedirs(new_dir)

            # copy the file to the destination
            self.log.info(f"Copying {old} to {new}")
            copy2(old, new)
