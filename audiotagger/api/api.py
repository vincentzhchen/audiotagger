from audiotagger.core.audiotagger import AudioTagger
from audiotagger.core.clear_tags import ClearTags
from audiotagger.core.create_playlist import CreatePlaylist
from audiotagger.core.copy_file import CopyFile
from audiotagger.data.input import AudioTaggerInput
from audiotagger.data.output import AudioTaggerOutput


class AudioTaggerAPI(object):
    def __init__(self, logger, options, **kwargs):
        self.log = logger
        self.options = options
        self.input_data = AudioTaggerInput(src=self.options.src,
                                           logger=self.log,
                                           options=self.options)

    def run(self):
        if self.input_data.get_metadata().empty:
            self.log.warn("METADATA dataframe is empty... EXITING PROCESS.")
            return

        if self.options.clear_tags:
            # Deletes tags from audio files by overwriting with blank tags.
            metadata = ClearTags(input_data=self.input_data,
                                 logger=self.log,
                                 options=self.options).execute()

            out = AudioTaggerOutput(metadata=metadata,
                                    logger=self.log,
                                    options=self.options)
            out.save()

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

        if self.options.copy_file:
            # Renames the audio file path using a pre-defined format.
            # If a destination directory is passed, the renamed file
            # will be saved into the destination, leaving the original
            # file untouched.
            metadata = CopyFile(input_data=self.input_data,
                                logger=self.log,
                                options=self.options).execute()

            out = AudioTaggerOutput(metadata=metadata,
                                    logger=self.log,
                                    options=self.options)
            out.copy()

        if self.options.playlist_query:
            # TODO: fix this to match above structure
            # The CreatePlaylist should just return a metadata df with the
            # desired playlist.  The PATH_DST should have the location to
            # save the playlist.  Output object should just copy.
            metadata = CreatePlaylist(input_data=self.input_data,
                                      logger=self.log,
                                      options=self.options).execute()

            out = AudioTaggerOutput(metadata=metadata,
                                    logger=self.log,
                                    options=self.options)
            out.copy()

            # out = AudioTaggerOutput(metadata=metadata,
            #                         logger=self.log,
            #                         options=self.options)
            # out.copy()
