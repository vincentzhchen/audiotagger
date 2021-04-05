# SPDX-License-Identifier: GPL-3.0-or-later
"""Handles all file copying and moving.

TODO: need better module name.

"""

import os
import shutil

from audiotagger.data import fields as fld
from audiotagger.util import audiotagger_logger, file_util as futil


class CopyFile():
    """All copying of files take place here.

    """

    def __init__(self, input_data, logger=None):
        self.input_data = input_data
        self.logger = logger if (
            logger is not None) else audiotagger_logger.get_logger()

    def execute(self, dst_dir=None, rename=True, to_file=False):
        metadata = self.input_data.get_metadata()

        if rename:
            metadata = futil.generate_new_file_path_from_metadata(
                metadata, dst_dir)

        # filter out only new paths
        metadata = metadata.loc[
            metadata[fld.PATH_SRC.CID] != metadata[fld.PATH_DST.CID]]

        self.logger.info("Number of files to copy: %s", len(metadata))
        self.copy(metadata, to_file)

    def copy(self, metadata, to_file=False):
        if to_file:
            self.copy_files(metadata)
        else:
            self.logger.info("DRY RUN -- no files were created.")

    def copy_files(self, metadata):
        df = metadata

        # check to see if there is enough space to copy files
        df["ROOT"] = df[fld.PATH_DST.CID].apply(futil.get_mount_point)
        df["FREE_SPACE"] = df["ROOT"].apply(futil.get_free_space)
        df["FILE_SIZE"] = df[fld.PATH_SRC.CID].apply(futil.get_file_size)

        gb = df.groupby("ROOT")
        no_space = (gb["FILE_SIZE"].sum() > gb["FREE_SPACE"].max())
        if not no_space.loc[no_space].empty:
            raise Exception(f"The following file systems do not have enough "
                            f"free space for copying: \n"
                            f"{no_space.loc[no_space].index.tolist()}")

        # build src, dst pairs for all audio files
        pairs = list(zip(df[fld.PATH_SRC.CID], df[fld.PATH_DST.CID]))

        # copy cover art as well; also build the cover art src, dst
        if fld.COVER_SRC.CID in df:
            pairs.extend(
                list(set(zip(df[fld.COVER_SRC.CID], df[fld.COVER_DST.CID]))))
        pairs = sorted(pairs)

        num_copied = 0
        # BEGIN copy process
        for old, new in pairs:
            if old == new:
                continue

            # check if the new destination dir exists, if not then create it
            new_dir = os.path.dirname(new)
            if not os.path.isdir(new_dir):
                self.logger.info("%s does not exist, creating it...", new_dir)
                os.makedirs(new_dir)

            # copy the file to the destination
            self.logger.info("Copying %s to %s", old, new)
            shutil.copy2(old, new)

            # If the old file is in the same directory as the new file,
            # delete the old file (this prevents duplicates).  A common use
            # case is when a song title has changed and the copy takes place
            # in the same directory.
            old_dir = os.path.dirname(old)
            if old_dir == new_dir:
                os.remove(old)

            num_copied += 1

        self.logger.info("Done, number of files copied: %s", num_copied)
