import pytest
from audiotagger.core.paths import (audiotagger_config_dir,
                                    audiotagger_config_path)
from audiotagger.util import file_util as futil


@pytest.mark.parametrize("src, min_output_length", [
    # fake directory; expect to fail
    pytest.param("/fake/path", -1, marks=pytest.mark.xfail),

    # real directory
    pytest.param(audiotagger_config_dir(), 0),

    # fake path
    pytest.param("/fake/path/test.txt", -1, marks=pytest.mark.xfail),

    # real path
    pytest.param(audiotagger_config_path(), 0),
])
def test_traverse_directory(src, min_output_length):
    all_file_paths = futil.traverse_directory(src)
    assert all_file_paths.__class__ == list
    assert len(all_file_paths) > min_output_length


@pytest.mark.parametrize("input_path, expected_result", [
    # not a path; expect to return False
    pytest.param("/fake/path", False),

    # potentially real path, expect True
    pytest.param("~/file.xlsx", True),

    # not an Excel file, expect False
    pytest.param("~/file.csv", False),
])
def test_is_xlsx(input_path, expected_result):
    assert futil.is_xlsx(input_path) == expected_result
