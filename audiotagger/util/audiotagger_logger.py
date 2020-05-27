# SPDX-License-Identifier: GPL-3.0-or-later
"""Logging for audiotagger.

"""
import logging
import os
import sys

this = sys.modules[__name__]  # pointer to module instance
this.LOGGER_SINGLETON = None  # explicit assignment of singleton


def get_logger(log_dir=None, name="audiotagger.log", level=logging.DEBUG):
    """Get a logger instance.

    The logger returned is a singleton, so if it already has been previously
    instantiated, return the cached logger.  Otherwise, create a new logger
    to be cached and returned.

    Args:
        log_dir (str, default None): the directory to store the log file.
            If None, then only log to console.
        name (str, default `audiotagger.log`): name of the log file.
        level (int, default logging.DEBUG): log level to set the logger to.

    Return:
        logger (logging.RootLogger): returns a logger instance.
    """
    if this.LOGGER_SINGLETON is not None:
        return this.LOGGER_SINGLETON

    logging.captureWarnings(True)

    # default format
    formatter = logging.Formatter("%(asctime)s - "
                                  "%(levelname)s - "
                                  "%(module)s.%(funcName)s - "
                                  "%(message)s")

    # generate logger
    logger = logging.getLogger()

    # setup console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # setup file handler
    if log_dir is not None:
        if os.path.isdir(log_dir):
            log_path = os.path.realpath(os.path.join(log_dir, name))
            file_handler = logging.FileHandler(log_path, encoding="utf-8")
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        else:
            logger.warning(
                "LOG DIRECTORY %s does not exist... only log to console.",
                log_dir)
    else:
        logger.warning(
            "NO LOG DIRECTORY was specified... only log to console.")

    # setup log level
    logger.setLevel(level)

    this.LOGGER_SINGLETON = logger
    return logger
