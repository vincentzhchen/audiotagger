# SPDX-License-Identifier: GPL-3.0-or-later
from concurrent.futures import ProcessPoolExecutor
import glob
import os
import shutil

from mutagen.easymp4 import MP4


def get_file_extension(path_to_some_file):
    """Get file extension of a given filepath.

    Args:
      path_to_some_file (str): filepath.

    Returns:
      file_extension (str): Returns the file extension.
    """
    root_ext_tuple = os.path.splitext(path_to_some_file)
    file_extension = root_ext_tuple[1]
    return file_extension


def _is_audio_file_ext(path_to_some_file, extension):
    """Helper method to check if audio file extension.

    Args:
      path_to_some_file (str): filepath.
      extension (str): an audio file extension, e.g. ".wav", to compare against.

    Returns:
      anonymous (bool): Returns True if the path extension matches
        the given extension.
    """
    file_extension = get_file_extension(path_to_some_file)
    return bool(file_extension == extension)


def is_xlsx(path_to_some_file):
    """Checks if a file is an Excel (.xlsx) file.

    """
    return _is_audio_file_ext(path_to_some_file, ".xlsx")


def is_wav(path_to_some_file):
    """Check if file is a wav file.

    """
    return _is_audio_file_ext(path_to_some_file, ".wav")


def is_m4a(path_to_some_file):
    """Check if file is a m4a file.

    """
    return _is_audio_file_ext(path_to_some_file, ".m4a")


def is_flac(path_to_some_file):
    """Check if file is a flac file.

    """
    return _is_audio_file_ext(path_to_some_file, ".flac")


def filter_wav_files(arg):
    """Get back a list of wav files.

    Args:
      arg (str or list of str): a list of audio filepaths.

    Returns:
      anonymous (list): Returns a list of all wav files found in arg.
    """
    if isinstance(arg, str):
        arg = [arg]

    return [x for x in arg if is_wav(x)]


def filter_m4a_files(arg):
    """Get back a list of m4a files.

    Args:
      arg (str or list of str): a list of audio filepaths.

    Returns:
      anonymous (list): Returns a list of all m4a files found in arg.
    """
    if isinstance(arg, str):
        arg = [arg]

    return [x for x in arg if is_m4a(x)]


def filter_flac_files(arg):
    """Get back a list of flac files.

    Args:
      arg (str or list of str): a list of audio filepaths.

    Returns:
      anonymous (list): Returns a list of all flac files found in arg.
    """
    if isinstance(arg, str):
        arg = [arg]

    return [x for x in arg if is_flac(x)]


def _generate_metadata_records_from_m4a(path):
    """Get a dictionary of metadata records from m4a filepath.

    """
    d = dict(MP4(path).tags, **{"PATH_SRC": [path], "PATH_DST": [path]})
    return d


def generate_metadata_records_from_m4a(m4a_file_paths):
    """Generate a list of metadata records from m4a file paths.

    This creates the tags using parallel processing.

    Args:
      m4a_file_paths (list of str): m4a file paths.

    Returns:
      out (list of dict): Returns a list of metadata dicts.
    """
    with ProcessPoolExecutor() as executor:
        out = executor.map(_generate_metadata_records_from_m4a,
                           m4a_file_paths,
                           chunksize=10)
    return list(out)


def generate_metadata_records(file_paths, extension="m4a"):
    """Wrapper to generate metadata records.

    This can be extended to work with various file types.

    """
    if extension == "m4a":
        return generate_metadata_records_from_m4a(file_paths)

    raise NotImplementedError("Only support for m4a at this time.")


def traverse_directory(src, filter_extension=None):
    """Recursively traverses a directory and returns all paths in a list.

    If the source is a file path, then return the source as a list.

    Args:
      src (str): Source directory in a list.
      filter_extension (str): Filter results on specified file
        extension.  For example, passing "m4a" will only return
        files that end in ".m4a".

    Returns:
      all_file_paths (list): List of all file paths in `src`.
    """

    # if src is a file path, then return it as a list
    if os.path.isfile(src):
        return [src]

    if not os.path.exists(src):
        raise ValueError(f"{src} does not exist.")

    # walk directory tree
    file_extension = ""
    if filter_extension is not None:
        file_extension = f".{filter_extension}"
    file_path = os.path.join(glob.escape(src), "**", f"*{file_extension}")
    all_file_paths = glob.glob(file_path, recursive=True)
    return all_file_paths


def replace_invalid_characters(path_to_some_file):
    # TODO: make this a config?
    for char in ["/", "\0", ":", "?", '"']:
        path_to_some_file = path_to_some_file.replace(char, "_")
    return path_to_some_file


def parse_sql_query(sql_file):
    with open(sql_file, "r") as f:
        query = f.read().strip()
    return query


def get_file_size(path, unit="GB"):
    if unit.upper() == "GB":
        return os.path.getsize(path) / 1e9

    raise ValueError(f"UNIT {unit} is not supported.")


def get_free_space(path):
    return shutil.disk_usage(path).free / 1e9


def get_mount_point(path):
    path = os.path.abspath(path)
    while not os.path.ismount(path):
        path = os.path.dirname(path)
    return path
