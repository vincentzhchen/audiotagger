import os
import pandasdateutils as pdu

from audiotagger.core.clear_tags import ClearTags
from audiotagger.core.audiotagger import AudioTagger
from audiotagger.core.paths import audiotagger_log_dir
from audiotagger.core.rename_file import RenameFile
from audiotagger.core.create_playlist import CreatePlaylist
from audiotagger.data.input import AudioTaggerInput
from audiotagger.settings import settings as settings


class AudioTaggerAPI(object):
    def __init__(self, logger, options, **kwargs):
        self.log = logger
        self.options = options
        self.input_data = AudioTaggerInput(src=options.src,
                                           logger=self.log,
                                           is_dry_run=options.dry_run)

        if self.options.write_to_excel:
            # write input data to Excel for debugging
            base_dir = audiotagger_log_dir()
            file_path = os.path.join(
                base_dir, f"input_{pdu.now(as_string=True)}.xlsx")
            self.input_data.write_to_excel(file_path)

    def run(self):
        if self.input_data.get_metadata().empty:
            self.log.warn("METADATA dataframe is empty... EXITING PROCESS.")
            return

        if self.options.tag_file:
            # Given a metadata dataframe, tag the audio files listed
            # by the paths in the dataframe.
            at = AudioTagger(logger=self.log, input_data=self.input_data)
            at.save_tags_to_audio_files()

        if self.options.rename_file:
            # Renames the audio file path using a pre-defined format.
            # If a destination directory is passed, the renamed file
            # will be saved into the destination, leaving the original
            # file untouched.
            if self.options.dst is not None:
                rename_dst = self.options.dst
            else:
                # TODO: for now, always save to the audio directory.
                rename_dst = settings.AUDIO_DIRECTORY

            rf = RenameFile(base_dst_dir=rename_dst, logger=self.log,
                            input_data=self.input_data)
            rf.rename_file()

        if self.options.clear_tags == "all":
            # Deletes all tags from audio files.
            ct = ClearTags(logger=self.log, input_data=self.input_data)
            ct.clear_all_tags()
        elif self.options.clear_tags == "excess":
            # Deletes all tags not part of the base set of desired metadata.
            ct = ClearTags(logger=self.log, input_data=self.input_data)
            ct.clear_excess_tags()

        if self.options.generate_playlist:
            cp = CreatePlaylist(playlist_dst_dir=self.options.output_dst,
                                logger=self.log, input_data=self.input_data)
            cp.create_playlist()
