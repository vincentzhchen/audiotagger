# SPDX-License-Identifier: GPL-3.0-or-later
import copy
import os
import shutil

from audiotagger.data import _base_io, fields as fld
from audiotagger.util import (file_util as futil, tag_util as tutil,
                              input_output_util as ioutil)


class AudioTaggerOutput(_base_io.AudioTaggerBaseInputOutput):

  def write_to_excel(self):
    file_path = ioutil.generate_excel_path("audiotagger_output")
    ioutil.write_metadata_to_excel(self.metadata, file_path=file_path)
    self.logger.info("Saved output metadata to %s", file_path)

  def write_to_csv(self):
    raise NotImplementedError

  def set_metadata(self, df):
    self.logger.info("Setting metadata in input object.")
    super().set_metadata(df)

  def save(self, to_excel=False, save_tags=False):
    # at this point, handle cover art
    self.metadata = tutil.generate_cover_art_path(df=self.metadata)
    self.metadata = tutil.construct_cover_object(df=self.metadata)

    if to_excel:
      self.write_to_excel()

    if save_tags:
      self.save_tags_to_audio_files()
    else:
      self.logger.info("DRY RUN -- no audio files were modified.")

  def save_tags_to_audio_files(self):
    metadata = self.metadata
    tag_dict = tutil.metadata_to_tags(df=metadata)
    for k in tag_dict:
      dict_for_log = copy.deepcopy(tag_dict[k])
      dict_for_log.pop(fld.COVER.KEY, None)
      self.logger.info("Saving %s to %s", dict_for_log, k)
      tag_dict[k].save(k)

  def copy(self, to_file=False):
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
    if not no_space.loc[no_space].empty:
      raise Exception(f"The following file systems do not have enough "
                      f"free space for copying: \n"
                      f"{no_space.loc[no_space].index.tolist()}")

    # BEGIN copy process
    pairs = list(zip(df[fld.PATH_SRC.CID], df[fld.PATH_DST.CID]))

    # copy cover art as well
    pairs.extend(list(set(zip(df[fld.COVER_SRC.CID], df[fld.COVER_DST.CID]))))
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
