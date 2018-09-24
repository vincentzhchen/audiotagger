import pytest
from audiotagger.core.paths import (audiotagger_config_dir,
                                    audiotagger_config_path)
from audiotagger.utils.utils import AudioTaggerUtils


@pytest.mark.parametrize("src, min_output_length", [
    # fake directory; expect to fail
    pytest.param("/fake/path", -1, marks=pytest.mark.xfail),

    # real directory
    (audiotagger_config_dir(), 0),

    # fake path
    pytest.param("/fake/path/test.txt", -1, marks=pytest.mark.xfail),

    # real path
    (audiotagger_config_path(), 0),
])
def test_traverse_directory(src, min_output_length):
    all_file_paths = AudioTaggerUtils.traverse_directory(src)
    assert all_file_paths.__class__ == list
    assert len(all_file_paths) > min_output_length
