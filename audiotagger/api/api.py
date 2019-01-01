import os

import pandasdateutils as pdu
from audiotagger.core.audiotagger import AudioTagger
from audiotagger.core.clear_tags import ClearTags
from audiotagger.core.create_playlist import CreatePlaylist
from audiotagger.core.rename_file import RenameFile
from audiotagger.data.input import AudioTaggerInput
from audiotagger.data.output import AudioTaggerOutput
from audiotagger.settings import settings as settings
from audiotagger.util.input_output_util import InputOutputUtil


class AudioTaggerAPI(object):
    def __init__(self, logger, options, **kwargs):
        self.log = logger
        self.options = options
        self.input_data = AudioTaggerInput(src=options.src, logger=self.log)

        if self.options.write_to_excel:
            base_dir = settings.LOG_DIRECTORY
            file_path = os.path.join(
                base_dir, f"input_{pdu.now(as_string=True)}.xlsx")
            InputOutputUtil.write_to_excel(df=self.input_data.get_metadata(),
                                           file_path=file_path)

    def run(self):
        if self.input_data.get_metadata().empty:
            self.log.warn("METADATA dataframe is empty... EXITING PROCESS.")
            return

        if self.options.tag_file:
            # Given a metadata dataframe, tag the audio files listed
            # by the paths in the dataframe.
            metadata = AudioTagger(input_data=self.input_data,
                                   logger=self.log,
                                   options=self.options).execute()

            out = AudioTaggerOutput(metadata=metadata,
                                    logger=self.log,
                                    options=self.options)
            out.save()

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

        if self.options.clear_tags:
            # Deletes tags from audio files by overwriting with blank tags.
            metadata = ClearTags(input_data=self.input_data,
                                 logger=self.log,
                                 options=self.options).execute()

            out = AudioTaggerOutput(metadata=metadata,
                                    logger=self.log,
                                    options=self.options)
            out.save()

        if self.options.generate_playlist:
            cp = CreatePlaylist(playlist_dst_dir=self.options.output_dst,
                                logger=self.log, input_data=self.input_data)
            cp.create_playlist()
