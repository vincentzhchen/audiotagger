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
from customlogging import CustomLogging as cl


def get_options():
    parser = optparse.OptionParser()
    parser.add_option(
        "-p",
        action="store",
        dest="root",
        help="Root directory or path for all audio files."
    )

    parser.add_option(
        "-x",
        action="store_true",
        dest="write_to_excel",
        help="Write data to Excel."
    )

    parser.add_option(
        "-t",
        "--tag",
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
        "--rename_path",
        action="store_true",
        dest="rename_path",
        help="Renames the path to the audio file."
    )

    parser.add_option(
        "--xl",
        action="store",
        dest="xl_input_file",
        help="Read tags from specially formatted Excel file."
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
        self.root = options.root
        self.options = options
        self.input = AudioTaggerInput(root=self.root, logger=self.log,
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

    # Setup logging.
    log_dir = options.log_dir
    if os.path.exists(audiotagger_config_path()):
        import importlib.util
        spec = importlib.util.spec_from_file_location("audiotagger",
                                                      audiotagger_config_path())
        c = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(c)
        log_dir = c.LOG_DIRECTORY

    logger = cl(log_dir=log_dir, name="audiotagger.log")
    logger.info(options)

    if options.xl_input_file is not None:
        et = ExcelTagger(logger=logger, xl_input_file=options.xl_input_file)
        if options.tag_file:
            et.tag_audio_files()

        if options.rename_path:
            et.rename_file()
        sys.exit(0)

    # need a root directory to run the program
    if options.root is None:
        logger.error("Must include root directory containing audio files.")
        sys.exit(1)
    else:
        if not os.path.isdir(options.root):
            logger.error("{} does not exist".format(options.root))
            sys.exit(1)

        if options.is_clear_tags:
            ct = ClearTags(root=options.root, logger=logger)
            ct.clear_tags()
            sys.exit(1)

        at = AudioTaggerInput(root=options.root, logger=logger)
        print(at.get_metadata())