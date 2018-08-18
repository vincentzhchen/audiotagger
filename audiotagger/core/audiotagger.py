#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import datetime
import pandas as pd
import optparse
import audiotagger.settings.settings as at_settings
from audiotagger.data.input import AudioTaggerInput
from customlogging import CustomLogging as cl


def get_options():
    parser = optparse.OptionParser()
    parser.add_option(
        "-r",
        action="store",
        dest="root",
        default=None,
        help="Root directory for all audio files."
    )

    parser.add_option(
        "-x",
        action="store",
        dest="write_to_excel",
        default=True,
        help="Store data to Excel for debugging."
    )

    parser.add_option(
        "-l",
        action="store",
        dest="log",
        default=at_settings.LOG_DIRECTORY,
        help="Set log directory."
    )

    return parser


class AudioTagger(object):
    def __init__(self, root, options, logger):
        self.log = logger
        self.root = root
        self.options = options
        self.input = AudioTaggerInput(root=self.root, logger=self.log)
        self._set_pandas_view_options()

    def _set_pandas_view_options(self):
        # sets the print options for Pandas
        pd.set_option("display.max_columns", None)
        pd.set_option("display.expand_frame_repr", False)

    def main(self):
        all_songs = self.input.get_all_audio()
        all_songs = all_songs.drop(["COVER", "LYRICS", "SONG"], axis=1)
        self.input.write_to_csv(
            filepath=os.path.join(at_settings.DEBUGGING_DIRECTORY, "input",
                                  "input_{}.txt".format(
                                      datetime.datetime.now().strftime(
                                          "%Y%m%d_%H%M%S"))))
        self.log.log_dataframe(all_songs)


if __name__ == "__main__":
    # SETUP LOGGING
    options, args = get_options().parse_args()
    log = cl(log_dir=options.log)
    log.info(options)

