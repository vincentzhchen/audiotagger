# PROJECT LIB
from audiotagger.core import (audiotagger, clear_tags, copy_file,
                              create_playlist)
from audiotagger.data import input as at_in, output as at_out


class AudioTaggerAPI(object):
    def __init__(self, logger, options, **kwargs):
        self.log = logger
        self.options = options

        input_data = at_in.AudioTaggerInput(logger=self.log)
        # load data -- singleton to be modified continuously as needed.
        input_data.load_metadata(src=self.options.src)

        if self.options.write_to_excel:
            input_data.write_to_excel()

        self.input_data = input_data

    def run(self):
        if self.input_data.get_metadata().empty:
            self.log.warn("METADATA dataframe is empty... EXITING PROCESS.")
            return

        if self.options.clear_tags:
            # Deletes tags from audio files by overwriting with blank tags.
            metadata = clear_tags.ClearTags(
                input_data=self.input_data,
                logger=self.log,
                options=self.options).execute()

            out = at_out.AudioTaggerOutput(
                metadata=metadata,
                logger=self.log,
                options=self.options)
            out.save()

        if self.options.tag_file:
            # Given a metadata dataframe, tag the audio files listed
            # by the paths in the dataframe.
            metadata = audiotagger.AudioTagger(
                input_data=self.input_data,
                logger=self.log,
                options=self.options).execute()

            out = at_out.AudioTaggerOutput(
                metadata=metadata,
                logger=self.log,
                options=self.options)
            out.save()

        if self.options.copy_file:
            # Renames the audio file path using a pre-defined format.
            # If a destination directory is passed, the renamed file
            # will be saved into the destination, leaving the original
            # file untouched.
            metadata = copy_file.CopyFile(
                input_data=self.input_data,
                logger=self.log,
                options=self.options).execute()

            out = at_out.AudioTaggerOutput(
                metadata=metadata,
                logger=self.log,
                options=self.options)
            out.copy()

        if self.options.playlist_query:
            # Creates a playlist from the source directory using the given
            # query and writes the files into the destination directory.
            metadata = create_playlist.CreatePlaylist(
                input_data=self.input_data,
                logger=self.log,
                options=self.options).execute()

            out = at_out.AudioTaggerOutput(
                metadata=metadata,
                logger=self.log,
                options=self.options)
            out.copy()
