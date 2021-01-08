# SPDX-License-Identifier: GPL-3.0-or-later
"""API into audiotagger.

"""
from audiotagger.core import (audiotagger, clear_tags, copy_file,
                              create_playlist)
from audiotagger.data import at_input as at_in, at_output as at_out
from audiotagger.util import audiotagger_logger


class AudioTaggerAPI():
    """Main API to load up metadata and delegate tasks to appropriate classes.

    """

    def __init__(self, src, input_to_excel=False, logger=None):
        if logger is not None:
            self.logger = logger
        else:
            self.logger = audiotagger_logger.get_logger()

        input_data = at_in.AudioTaggerInput(logger=self.logger)
        # load data -- singleton to be modified continuously as needed.
        input_data.load_metadata(src=src)

        if input_to_excel:
            input_data.write_to_excel()

        self.input_data = input_data

    def run(self,
            delete_tags=None,
            modify_tags=False,
            rename_and_copy=False,
            playlist_query=None,
            save_tags=False,
            output_to_excel=False,
            dst_dir=None):
        """Delegate here to the class that will handle the action.

        Args:
          delete_tags (str, default None): A method to delete tags.  If
            None, no tags will be deleted.
          modify_tags (bool, default False): If True, modify the metadata.
          save_tags (bool, default False): If True, write tags to audio file.
          output_to_excel(bool, default False): If True, write metadata
            to Excel file.

        """
        if self.input_data.get_metadata().empty:
            self.logger.warning(
                "METADATA dataframe is empty... EXITING PROCESS.")
            return

        if delete_tags is not None:
            # Deletes tags from audio files by overwriting with blank tags.
            metadata = clear_tags.ClearTags(
                self.input_data).execute(delete_tags)

            out = at_out.AudioTaggerOutput()
            out.set_metadata(metadata)
            out.save(to_excel=output_to_excel, save_tags=save_tags)

        if modify_tags:
            # Given a metadata dataframe, tag the audio files listed
            # by the paths in the dataframe.
            metadata = audiotagger.AudioTagger(self.input_data).execute()

            out = at_out.AudioTaggerOutput()
            out.set_metadata(metadata)
            out.save(to_excel=output_to_excel, save_tags=save_tags)

        if rename_and_copy:
            # Renames the audio file path using a pre-defined format.
            # If a destination directory is passed, the renamed file
            # will be saved into the destination, leaving the original
            # file untouched.
            metadata = copy_file.CopyFile(self.input_data).execute(dst_dir)

            out = at_out.AudioTaggerOutput()
            out.set_metadata(metadata)
            out.copy()

        if playlist_query is not None:
            # Creates a playlist from the source directory using the given
            # query and writes the files into the destination directory.
            metadata = create_playlist.CreatePlaylist(
                self.input_data).execute(playlist_query)

            out = at_out.AudioTaggerOutput()
            out.set_metadata(metadata)
            out.copy()
