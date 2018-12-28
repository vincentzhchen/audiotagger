import glob
import os

from mutagen.easymp4 import MP4


class FileUtil(object):
    def __init__(self):
        pass

    @classmethod
    def get_file_extension(cls, path_to_some_file):
        filename, file_extension = os.path.splitext(path_to_some_file)
        return file_extension

    @classmethod
    def is_m4a(cls, path_to_some_file):
        file_extension = FileUtil.get_file_extension(path_to_some_file)
        return True if file_extension == ".m4a" else False

    @classmethod
    def is_mp3(cls, path_to_some_file):
        file_extension = FileUtil.get_file_extension(path_to_some_file)
        return True if file_extension == ".mp3" else False

    @classmethod
    def is_wav(cls, path_to_some_file):
        file_extension = FileUtil.get_file_extension(path_to_some_file)
        return True if file_extension == ".wav" else False

    @classmethod
    def is_flac(cls, path_to_some_file):
        file_extension = FileUtil.get_file_extension(path_to_some_file)
        return True if file_extension == ".flac" else False

    @classmethod
    def is_ape(cls, path_to_some_file):
        file_extension = FileUtil.get_file_extension(path_to_some_file)
        return True if file_extension == ".ape" else False

    @classmethod
    def filter_m4a_files(cls, arg):
        if isinstance(arg, str):
            arg = [arg]

        return [x for x in arg if FileUtil.is_m4a(x)]

    @classmethod
    def apply_utf8(cls, x):
        return x.encode("utf-8").decode("utf-8")

    @classmethod
    def convert_to_mp4_obj(cls, file_paths):
        return [MP4(path) for path in file_paths]

    @classmethod
    def traverse_directory(cls, src, filter_extension=None):
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
        file_extension = "**/*"  # get all files
        if filter_extension is not None:
            file_extension = f"**/*.{filter_extension}"
        all_file_paths = [f for f in glob.iglob(src + file_extension,
                                                recursive=True)]
        return all_file_paths

    @classmethod
    def is_xlsx(cls, path_to_some_file):
        """Checks if a file is an Excel (.xlsx) file.

        Args:
            path_to_some_file (str): Path to the file.

        Returns:
            Returns True if the file is an xlsx file else False.
        """
        file_extension = FileUtil.get_file_extension(path_to_some_file)
        return True if file_extension == ".xlsx" else False

    @classmethod
    def replace_invalid_characters(cls, path_to_some_file):
        path_to_some_file = path_to_some_file.replace("/", "_")
        path_to_some_file = path_to_some_file.replace("\0", "_")
        return path_to_some_file
