#!/usr/bin/env python
# -*- coding: utf-8 -*-

import optparse
import os
import sys
# from audiotagger.settings import settings as at_settings
from audiotagger.core.generate_config import generate_config
from audiotagger.core.paths import audiotagger_config_path
from audiotagger.data.input import AudioTaggerInput
from customlogging import CustomLogging as cl


def get_options():
    parser = optparse.OptionParser()
    parser.add_option(
        "-r",
        action="store",
        dest="root",
        help="Root directory for all audio files."
    )

    parser.add_option(
        "-x",
        action="store_true",
        dest="write_to_excel",
        help="Write data to Excel."
    )

    parser.add_option(
        "-l",
        action="store",
        dest="log_dir",
        help="Set log directory."
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
        self.input = AudioTaggerInput(root=self.root, logger=self.log)

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

    # need a root directory to run the program
    if options.root is None:
        logger.error("Must include root directory containing audio files.")
        sys.exit(1)
    else:
        if not os.path.isdir(options.root):
            logger.error("{} does not exist".format(options.root))
            sys.exit(1)

    at = AudioTagger(logger=logger, options=options)
    print(at)