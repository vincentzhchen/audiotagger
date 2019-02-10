import glob
import os
import shutil

from concurrent.futures import ProcessPoolExecutor
from mutagen.easymp4 import MP4


def get_file_extension(path_to_some_file):
    filename, file_extension = os.path.splitext(path_to_some_file)
    return file_extension


def _is_audio_file_ext(path_to_some_file, extension):
    file_extension = get_file_extension(path_to_some_file)
    return True if file_extension == extension else False


def is_xlsx(path_to_some_file):
    """Checks if a file is an Excel (.xlsx) file.

    Args:
        path_to_some_file (str): Path to the file.

    Returns:
        Returns True if the file is an xlsx file else False.
    """
    file_extension = get_file_extension(path_to_some_file)
    return True if file_extension == ".xlsx" else False


def is_wav(path_to_some_file):
    return _is_audio_file_ext(path_to_some_file, ".wav")


def is_m4a(path_to_some_file):
    return _is_audio_file_ext(path_to_some_file, ".m4a")


def is_flac(path_to_some_file):
    return _is_audio_file_ext(path_to_some_file, ".flac")


def filter_wav_files(arg):
    if isinstance(arg, str):
        arg = [arg]

    return [x for x in arg if is_wav(x)]


def filter_m4a_files(arg):
    if isinstance(arg, str):
        arg = [arg]

    return [x for x in arg if is_m4a(x)]


def filter_flac_files(arg):
    if isinstance(arg, str):
        arg = [arg]

    return [x for x in arg if is_flac(x)]


def _generate_metadata_records_from_m4a(path):
    d = dict(MP4(path).tags, **{"PATH_SRC": [path], "PATH_DST": [path]})

    return d


def generate_metadata_records_from_m4a(m4a_file_paths):
    """Generate a list of metadata records from m4a file paths.

    Also append the file path into the tags.

    Args:
        m4a_file_paths (list of str): m4a file paths.

    Returns:
        out (list of dict): Returns a list of metadata dicts.
    """
    with ProcessPoolExecutor() as executor:
        out = executor.map(_generate_metadata_records_from_m4a,
                           m4a_file_paths, chunksize=10)
    return list(out)


def generate_metadata_records(file_paths, extension="m4a"):
    if extension == "m4a":
        return generate_metadata_records_from_m4a(file_paths)

    else:
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
    else:
        raise ValueError(f"UNIT {unit} is not supported.")


def get_free_space(path):
    return shutil.disk_usage(path).free / 1e9


def get_mount_point(path):
    path = os.path.abspath(path)
    while not os.path.ismount(path):
        path = os.path.dirname(path)
    return path
