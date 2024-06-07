from pro_filer.actions.main_actions import show_disk_usage  # NOQA
import os
import pytest
from unittest.mock import patch


@pytest.fixture
def create_files(tmp_path):
    files = ["file1.txt", "file2.txt", "file3.txt"]
    for file in files:
        path = tmp_path / file
        path.write_text("This is some content")

    return [str(tmp_path / file) for file in files]


def test_show_disk_usage_total_size(create_files, capsys):
    context = {
        "all_files": create_files
    }
    show_disk_usage(context)
    result = capsys.readouterr()
    lines = result.out.split("\n")

    total_size = sum(os.path.getsize(file) for file in context["all_files"])
    assert f"Total size: {total_size}" in lines[-2]


@patch('os.path.getsize', return_value=0)
def test_show_disk_usage_files_empty(create_files, capsys):
    context = {
        "all_files": create_files
    }
    show_disk_usage(context)
    result = capsys.readouterr()
    lines = result.out.split("\n")

    assert "Total size: 0" in lines[-2]


@patch('os.path.getsize', values=[10, 22, 30])
def test_show_disk_usage_sorts(capsys):
    context = {
        "all_files": ["file1.txt", "file2.txt", "file3.txt"]
    }
    show_disk_usage(context)
    result = capsys.readouterr()
    lines = result.out.split("\n")

    sizes = [int(line.split()[1]) for line in lines[:-2]]
    assert sizes == sorted(sizes, reverse=False), ValueError()
