"""Logging for audiotagger.

"""

# STANDARD LIB
import logging
import os
import sys

this = sys.modules[__name__]  # pointer to module instance
this.LOGGER_SINGLETON = None  # explicit assignment of singleton


def get_logger(log_dir=None, name="audiotagger.log", level=logging.DEBUG):
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
        log_path = os.path.realpath(os.path.join(log_dir, name))
        file_handler = logging.FileHandler(log_path, encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    else:
        logger.warning("NO LOG DIRECTORY was specified... only log to console.")

    # setup log level
    logger.setLevel(level)

    this.LOGGER_SINGLETON = logger
    return logger
