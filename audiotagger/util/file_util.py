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
    def _is_audio_file_ext(self, path_to_some_file, extension):
        file_extension = FileUtil.get_file_extension(path_to_some_file)
        return True if file_extension == extension else False

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
    def is_wav(cls, path_to_some_file):
        return FileUtil._is_audio_file_ext(path_to_some_file, ".wav")

    @classmethod
    def is_m4a(cls, path_to_some_file):
        return FileUtil._is_audio_file_ext(path_to_some_file, ".m4a")

    @classmethod
    def is_flac(cls, path_to_some_file):
        return FileUtil._is_audio_file_ext(path_to_some_file, ".flac")

    @classmethod
    def filter_wav_files(cls, arg):
        if isinstance(arg, str):
            arg = [arg]

        return [x for x in arg if FileUtil.is_wav(x)]

    @classmethod
    def filter_m4a_files(cls, arg):
        if isinstance(arg, str):
            arg = [arg]

        return [x for x in arg if FileUtil.is_m4a(x)]

    @classmethod
    def filter_flac_files(cls, arg):
        if isinstance(arg, str):
            arg = [arg]

        return [x for x in arg if FileUtil.is_flac(x)]

    @classmethod
    def generate_metadata_records_from_m4a(cls, m4a_file_paths):
        """Generate a list of metadata records from m4a file paths.

        Also append the file path into the tags.

        Args:
            m4a_file_paths (list of str): m4a file paths.

        Returns:
            out (list of dict): Returns a list of metadata dicts.
        """
        g = (dict(MP4(path).tags, **{"PATH_SRC": [path], "PATH_DST": [path]})
             for path in m4a_file_paths)

        # mutagen stores tag values as lists, so flatten them
        return [{k: d[k][0] if not isinstance(d[k], bool) else d[k]
                 for k in d} for d in g]

    @classmethod
    def generate_metadata_records(cls, file_paths, extension="m4a"):
        if extension == "m4a":
            return FileUtil.generate_metadata_records_from_m4a(file_paths)

        else:
            raise NotImplementedError("Only support for m4a at this time.")

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
        file_extension = ""
        if filter_extension is not None:
            file_extension = f".{filter_extension}"
        file_path = os.path.join(glob.escape(src), "**", f"*{file_extension}")
        all_file_paths = glob.glob(file_path, recursive=True)
        return all_file_paths

    @classmethod
    def replace_invalid_characters(cls, path_to_some_file):
        path_to_some_file = path_to_some_file.replace("/", "_")
        path_to_some_file = path_to_some_file.replace("\0", "_")
        return path_to_some_file
