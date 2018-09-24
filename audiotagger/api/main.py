#!/usr/bin/env python
# -*- coding: utf-8 -*-

import optparse
import sys
from audiotagger.core.generate_config import generate_config
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
        help="Write metadata to Excel."
    )

    parser.add_option(
        "-t",
        "--tag_file",
        action="store_true",
        dest="tag_file",
        help="Write tags to the audio file."
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


if __name__ == "__main__":
    options, args = get_options().parse_args()

    # Get app configurations.
    if options.generate_config:
        generate_config()
        sys.exit(0)

    # Set up logging.
    if options.log_dir is not None:
        log_dir = options.log_dir
    else:
        from audiotagger.settings.settings import LOG_DIRECTORY
        log_dir = LOG_DIRECTORY
    logger = cl(log_dir=log_dir, name="audiotagger.log")
    logger.info(options)

    # Run main program.
    from audiotagger.api.api import AudioTagger
    at = AudioTagger(logger=logger, options=options)
    at.run()
