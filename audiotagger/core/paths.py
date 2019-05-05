import os


def get_home_dir():
    """Get the real path of the home directory"""
    homedir = os.path.expanduser("~")
    # resolve potential symbolic links
    homedir = os.path.realpath(homedir)
    return homedir


def audiotagger_config_dir():
    """Get the audiotagger config directory for this platform and user.

    For now, return ~/.audiotagger
    """
    return os.path.join(get_home_dir(), ".audiotagger")


def audiotagger_config_path():
    """Get the config file path for audiotagger."""
    return os.path.join(audiotagger_config_dir(), "audiotagger_config.py")


def audiotagger_log_dir():
    """Default directory to hold logs."""
    return os.path.join(audiotagger_config_dir(), "log")


def audiotagger_data_dir():
    """Default directory to hold input / output data files."""
    return os.path.join(audiotagger_config_dir(), "data")


def audiotagger_test_dir():
    """Default directory to hold unittest files."""
    return os.path.join(audiotagger_config_dir(), "test")
