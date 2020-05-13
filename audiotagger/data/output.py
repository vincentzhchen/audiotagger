# STANDARD LIB
import copy
import os
import shutil

# PROJECT LIB
from audiotagger.data import fields as fld
from audiotagger.util import (audiotagger_logger, file_util as futil, tag_util
                              as tutil, input_output_util as ioutil)


class AudioTaggerOutput(object):
    def __init__(self, metadata, logger=None, to_excel=False):
        self.metadata = metadata
        self.logger = logger if (
            logger is not None) else audiotagger_logger.get_logger()

        if to_excel:
            file_path = ioutil.generate_excel_path("audiotagger_output")
            ioutil.write_to_excel(df=metadata, file_path=file_path)
            self.logger.info(f"Saved output metadata to {file_path}")

        # at this point, handle cover art
        self.metadata = tutil.generate_cover_art_path(df=self.metadata)
        self.metadata = tutil.construct_cover_object(df=self.metadata)

    def save(self, to_file=False):
        if to_file:
            self.save_tags_to_audio_files()
        else:
            self.logger.info("DRY RUN -- no files were modified.")

    def save_tags_to_audio_files(self):
        metadata = self.metadata
        tag_dict = tutil.metadata_to_tags(df=metadata)
        for k in tag_dict:
            dict_for_log = copy.deepcopy(tag_dict[k])
            dict_for_log.pop(fld.COVER.ID3, None)
            self.logger.info(f"Saving {dict_for_log} to {k}")
            tag_dict[k].save(k)

    def copy(self, to_file):
        # TODO: this does not belong here; move to copy class
        if to_file:
            self.copy_files()
        else:
            self.logger.info("DRY RUN -- no files were created.")

    def copy_files(self):
        # TODO: this does not belong here; move to copy class
        df = self.metadata

        # check to see if there is enough space to copy files
        df["ROOT"] = df[fld.PATH_DST.CID].apply(futil.get_mount_point)
        df["FREE_SPACE"] = df["ROOT"].apply(futil.get_free_space)
        df["FILE_SIZE"] = df[fld.PATH_SRC.CID].apply(futil.get_file_size)

        gb = df.groupby("ROOT")
        no_space = (gb["FILE_SIZE"].sum() > gb["FREE_SPACE"].max())
        if not no_space.loc[no_space == True].empty:
            raise Exception(f"The following file systems do not have enough "
                            f"free space for copying: \n"
                            f"{no_space.loc[no_space == True].index.tolist()}")

        # BEGIN copy process
        pairs = list(zip(df[fld.PATH_SRC.CID], df[fld.PATH_DST.CID]))

        # copy cover art as well
        pairs.extend(
            list(set(zip(df[fld.COVER_SRC.CID], df[fld.COVER_DST.CID]))))
        pairs = sorted(pairs)

        for old, new in pairs:
            if old == new:
                continue

            # check if the new destination dir exists, if not then create it
            new_dir = os.path.dirname(new)
            if not os.path.isdir(new_dir):
                self.logger.info(f"{new_dir} does not exist, creating it...")
                os.makedirs(new_dir)

            # copy the file to the destination
            self.logger.info(f"Copying {old} to {new}")
            shutil.copy2(old, new)

            # If the old file is in the same directory as the new file,
            # delete the old file (this prevents duplicates).  A common use
            # case is when a song title has changed and the copy takes place
            # in the same directory.
            old_dir = os.path.dirname(old)
            if old_dir == new_dir:
                os.remove(old)
