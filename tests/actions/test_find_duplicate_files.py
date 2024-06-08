import pytest
from pro_filer.actions.main_actions import find_duplicate_files


def test_find_duplicate_files_no_duplicates(tmp_path):
    (tmp_path / "file1.txt").write_text("Hello, World!")
    (tmp_path / "file2.txt").write_text("Hello, Python!")
    (tmp_path / "file3.txt").write_text("Hello, GitHub Copilot!")

    context = {
        "all_files": [
            str(tmp_path / "file1.txt"),
            str(tmp_path / "file2.txt"),
            str(tmp_path / "file3.txt"),
        ]
    }

    assert find_duplicate_files(context) == []


def test_find_duplicate_files_with_duplicates(tmp_path):
    (tmp_path / "file1.txt").write_text("Hello, World!")
    (tmp_path / "file2.txt").write_text("Hello, World!")
    (tmp_path / "file3.txt").write_text("Hello, World!")

    context = {
        "all_files": [
            str(tmp_path / "file1.txt"),
            str(tmp_path / "file2.txt"),
            str(tmp_path / "file3.txt"),
        ]
    }

    assert find_duplicate_files(context) == [
        (str(tmp_path / "file1.txt"), str(tmp_path / "file2.txt")),
        (str(tmp_path / "file1.txt"), str(tmp_path / "file3.txt")),
        (str(tmp_path / "file2.txt"), str(tmp_path / "file3.txt")),
    ]


def test_find_duplicate_files_file_not_found(tmp_path):
    (tmp_path / "file1.txt").write_text("Hello, World!")

    context = {
        "all_files": [
            str(tmp_path / "file1.txt"),
            str(tmp_path / "file2.txt"),
        ]
    }

    with pytest.raises(ValueError):
        find_duplicate_files(context)
