"""Output structure holding metadata and associated files.

"""
# SPDX-License-Identifier: GPL-3.0-or-later
import copy

from audiotagger.data import _base_io, fields as fld
from audiotagger.util import tag_util as tutil, input_output_util as ioutil


class AudioTaggerOutput(_base_io.AudioTaggerBaseInputOutput):
    """Holds metadata and associated files to be tagged.

    """

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
