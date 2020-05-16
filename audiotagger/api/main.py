"""Main module and entry into audiotagger.

"""

# !/usr/bin/env python
# -*- coding: utf-8 -*-

# STANDARD LIB
import argparse
import os
import sys

# PROJECT LIB
from audiotagger.core import paths
from audiotagger.util import audiotagger_logger, audiotagger_setup


def get_args():
    """Construct all run arguments.

    """
    parser = argparse.ArgumentParser()

    # add arguments here
    help_msg = """
    Source directory or audio file path for all audio files.
    """
    parser.add_argument("-s", "--src", type=str, help=help_msg)

    help_msg = """
    Write metadata to Excel (.xlsx) file.
    """
    parser.add_argument("-x",
                        "--write-to-excel",
                        action="store_true",
                        help=help_msg)

    help_msg = """
    Given an Excel (.xlsx) metadata file containing tags and the
    audio file paths of the files associated, write tags to the files.
    """
    parser.add_argument("-t", "--tag-file", action="store_true", help=help_msg)

    help_msg = """
    Modifiers to apply to metadata.
    """
    parser.add_argument("-m", "--modifier", type=str, help=help_msg)

    help_msg = """
    Clears the tags for a given directory. (`all` clears all tags and
    `excess` clears all tags not in desired base metadata).
    """
    parser.add_argument("--clear-tags", type=str, help=help_msg)

    help_msg = """
    Copies the audio file from the source path to destination path.
    """
    parser.add_argument("-c",
                        "--copy-file",
                        action="store_true",
                        help=help_msg)

    help_msg = """
    Base destination directory for file output (e.g.
    from file renaming or playlist generation)."
    """
    parser.add_argument("-d", "--dst", type=str, help=help_msg)

    help_msg = """
    Commit changes to audio file.
    """
    parser.add_argument("-w",
                        "--write-to-file",
                        action="store_true",
                        help=help_msg)

    help_msg = """
    Create configuration file for the application.
    """
    parser.add_argument("--generate-config",
                        action="store_true",
                        help=help_msg)

    help_msg = """
    Creates a playlist from the given query on the source.
    """
    parser.add_argument("--create-playlist",
                        type=str,
                        dest="playlist_query",
                        help=help_msg)

    help_msg = """
    Generates an Excel (.xlsx) metadata template file.
    """
    parser.add_argument("--generate-metadata-template",
                        action="store_true",
                        help=help_msg)

    return parser.parse_args()


if __name__ == "__main__":
    # Set up logging.
    logger = audiotagger_logger.get_logger(paths.audiotagger_log_dir())

    logger.info("-" * 40)
    logger.info("Starting audiotagger.")
    logger.info("-" * 40)

    args = get_args()
    logger.info(args)

    # If the app was never configured, generate configuration once.
    if not os.path.exists(paths.audiotagger_config_path()):
        logger.info("Application will configure for the first time...")
        audiotagger_setup.generate_config()
        logger.info("Default configuration generated, exiting app.")
        sys.exit(0)

    # Reset app configurations.
    if args.generate_config:
        logger.info("Generating default app configurations...")
        audiotagger_setup.generate_config()
        logger.info("Done.")
        sys.exit(0)

    # Generate metadata Excel template.
    if args.generate_metadata_template:
        logger.info("Generating blank metadata template...")
        audiotagger_setup.generate_metadata_template(dst_dir=args.dst)
        logger.info("Done.")
        sys.exit(0)

    # RUN MAIN PROGRAM HERE.
    from audiotagger.api import api  # keep this lazy in case there is no config
    api.AudioTaggerAPI(logger=logger,
                       src=args.src,
                       to_excel=args.write_to_excel,
                       dst_dir=args.dst).run()
    logger.info("Done.")
