#!/usr/bin/env python
# -*- coding: utf-8 -*-

import optparse
import os
import sys
# from audiotagger.settings import settings as at_settings
from audiotagger.core.generate_config import generate_config
from audiotagger.core.clear_tags import ClearTags
from audiotagger.core.excel_tagger import ExcelTagger
from audiotagger.core.paths import audiotagger_config_path
from audiotagger.data.input import AudioTaggerInput
from audiotagger.core.rename_file import RenameFile
from customlogging import CustomLogging as cl


def get_options():
    parser = optparse.OptionParser()
    parser.add_option(
        "-s",
        action="store",
        dest="src",
        help="Source directory or path for all audio files."
    )

    parser.add_option(
        "-x",
        action="store_true",
        dest="write_to_excel",
        help="Write data to Excel."
    )

    parser.add_option(
        "-t",
        "--tag_file",
        action="store_true",
        dest="tag_file",
        help="Writes tags to the audio file."
    )

    parser.add_option(
        "-l",
        action="store",
        dest="log_dir",
        help="Set log directory."
    )

    parser.add_option(
        "-c",
        "--clear_tags",
        action="store_true",
        dest="is_clear_tags",
        help="Clears the tags for a given directory."
    )

    parser.add_option(
        "-r",
        "--rename_file",
        action="store_true",
        dest="rename_file",
        help="Renames the audio file path."
    )

    parser.add_option(
        "-d",
        "--rename_dst",
        action="store_true",
        dest="rename_dst",
        help="Base destination directory for file rename."
    )

    parser.add_option(
        "--xl_in",
        action="store",
        dest="xl_input_file",
        help="Specially formatted Excel file to read tags from."
    )

    parser.add_option(
        "--xl_out",
        action="store",
        dest="xl_output_file",
        help="Output file to write tags to."
    )

    parser.add_option(
        "--generate-config",
        action="store_true",
        dest="generate_config",
        help="Create configuration file for the application."
    )

    return parser


class AudioTagger(object):
    def __init__(self, logger, options, **kwargs):
        self.log = logger
        self.src = options.src
        self.options = options
        self.input = AudioTaggerInput(src=self.src, logger=self.log,
                                      xl_input_file=options.xl_input_file)

    def main(self):
        # all_songs = self.input.get_all_audio()
        # all_songs = all_songs.drop(["COVER", "LYRICS", "SONG"], axis=1)
        # self.input.write_to_csv(
        #     filepath=os.path.join(at_settings.DEBUGGING_DIRECTORY, "input",
        #                           "input_{}.txt".format(
        #                               datetime.datetime.now().strftime(
        #                                   "%Y%m%d_%H%M%S"))))
        # self.log.log_dataframe(all_songs)
        pass


if __name__ == "__main__":
    options, args = get_options().parse_args()

    # Get app configurations.
    if options.generate_config:
        generate_config()
        sys.exit(0)

    # Setup constants.
    log_dir = options.log_dir
    rename_dst = options.rename_dst
    if os.path.exists(audiotagger_config_path()):
        import importlib.util
        spec = importlib.util.spec_from_file_location("audiotagger",
                                                      audiotagger_config_path())
        c = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(c)

        log_dir = c.LOG_DIRECTORY
        rename_dst = c.AUDIO_DIRECTORY

    # Setup logging.
    logger = cl(log_dir=log_dir, name="audiotagger.log")
    logger.info(options)

    input_data = AudioTaggerInput(src=options.src, logger=logger,
                                  xl_input_file=options.xl_input_file)
    et = ExcelTagger(logger=logger, input_data=input_data)

    if options.tag_file:
        et.save_tags_to_audio_files()

    if options.rename_file:
        rf = RenameFile(base_dst_dir=rename_dst, logger=logger,
                        input_data=input_data)
        rf.rename_file()

    if options.is_clear_tags:
        ct = ClearTags(root=options.src, logger=logger)
        ct.clear_tags()

    if options.write_to_excel:
        input_data.write_to_excel(options.xl_output_file)
