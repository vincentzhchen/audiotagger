import os
from mutagen.mp4 import MP4Tags


class ClearTags(object):
    def __init__(self, root, logger):
        self.log = logger
        self.root = root
        self._load_all_file_paths()

    def _load_all_file_paths(self):
        """Loads all file paths in the given root directory.

        """
        self.log.info("Loading all file paths...")
        all_file_paths = []
        for root, dirs, files in os.walk(self.root):
            for file in files:
                file_path = os.path.join(root, file)
                all_file_paths.append(file_path)
        self.all_file_paths = all_file_paths
        self.log.info(f"LOADED {self.all_file_paths} file paths.")

    def clear_tags(self):
        tags = MP4Tags()
        for path in self.all_file_paths:
            self.log.info(f"Cleared tag for {path}")
            tags.save(path)