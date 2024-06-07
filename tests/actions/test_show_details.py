from pro_filer.actions.main_actions import show_details  # NOQA
import os
import datetime
import pytest


def test_show_details(capsys):
    context = {
      "all_files": ["src/__init__.py",
                    "src/app.py", "src/utils/__init__.py"],
      "all_dirs": ["src", "src/utils"],
      "base_path": "/home/trybe/Downloads/Trybe_logo.png"
    }
    show_details(context)
    result = capsys.readouterr()
    assert result.out == (
      "File 'Trybe_logo.png' does not exist\n")


def test_show_details_timestamp(capsys):
    context = {
      "base_path": "pro_filer.egg-info/entry_points.txt"
    }
    last_modified_date = datetime.datetime.fromtimestamp(
      os.path.getmtime(context['base_path'])).strftime('%Y-%m-%d')
    result_out = (
      f"File name: entry_points.txt\n"
      f"File size in bytes: 58\n"
      f"File type: file\n"
      f"File extension: .txt\n"
      f"Last modified date: {last_modified_date}\n"
    )
    show_details(context)
    result = capsys.readouterr()
    assert result.out == result_out


@pytest.fixture
def file_without_extension():
    file_path = "pro_filer.egg-info/entry_points"
    with open(file_path, "w") as file:
        file.write("")
    yield file_path


def test_show_details_without_extension(capsys, file_without_extension):
    context = {
      "base_path": file_without_extension
    }
    show_details(context)
    result = capsys.readouterr()
    assert "[no extension]" in result.out
