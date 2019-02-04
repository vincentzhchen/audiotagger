import os
from copy import deepcopy
from shutil import copy2

import pandasdateutils as pdu
from audiotagger.data.fields import Fields as fld
from audiotagger.settings import settings
from audiotagger.util.file_util import FileUtil
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
            # NULL COVER when not writing to audio file
            metadata = self.metadata.eval("COVER = None")
            InputOutputUtil.write_to_excel(df=metadata,
                                           file_path=file_path)
            self.log.info(f"Saved output metadata to {file_path}")

    def save(self):
        if self.options.write_to_file:
            self.save_tags_to_audio_files()
        else:
            self.log.info("DRY RUN -- no files were modified.")

    def save_tags_to_audio_files(self):
        metadata = self.metadata
        tag_dict = TagUtil.metadata_to_tags(df=metadata)
        for k in tag_dict:
            dict_for_log = deepcopy(tag_dict[k])
            dict_for_log.pop(fld.COVER.ID3)
            self.log.info(f"Saving {dict_for_log} to {k}")
            tag_dict[k].save(k)

    def copy(self):
        if self.options.write_to_file:
            self.copy_files()
        else:
            self.log.info("DRY RUN -- no files were created.")

    def copy_files(self):
        df = self.metadata

        # check to see if there is enough space to copy files
        df["ROOT"] = df[fld.PATH_DST.CID].apply(FileUtil.get_mount_point)
        df["FREE_SPACE"] = df["ROOT"].apply(FileUtil.get_free_space)
        df["FILE_SIZE"] = df[fld.PATH_SRC.CID].apply(FileUtil.get_file_size)

        gb = df.groupby("ROOT")
        no_space = (gb["FILE_SIZE"].sum() > gb["FREE_SPACE"].max())
        if not no_space.loc[no_space == True].empty:
            raise Exception(f"The following file systems do not have enough "
                            f"free space for copying: \n"
                            f"{no_space.loc[no_space == True].index.tolist()}")

        # BEGIN copy process
        pairs = list(zip(df[fld.PATH_SRC.CID], df[fld.PATH_DST.CID]))

        # copy cover art as well
        df["COVER_ART_DST"] = tuple(zip(
            df[fld.PATH_DST.CID].apply(os.path.dirname),
            df[fld.PATH_COVER.CID].apply(os.path.basename)))
        df["COVER_ART_DST"] = df["COVER_ART_DST"].apply(
            lambda x: os.path.join(x[0], x[1]))
        cover = df[[fld.PATH_COVER.CID, "COVER_ART_DST"]].drop_duplicates()
        pairs.extend(list(zip(cover[fld.PATH_COVER.CID],
                              cover["COVER_ART_DST"])))
        pairs = sorted(pairs)

        for old, new in pairs:
            # check if the new destination dir exists, if not then create it
            new_dir = os.path.dirname(new)
            if not os.path.isdir(new_dir):
                self.log.info(f"{new_dir} does not exist, creating it...")
                os.makedirs(new_dir)

            # copy the file to the destination
            self.log.info(f"Copying {old} to {new}")
            copy2(old, new)
