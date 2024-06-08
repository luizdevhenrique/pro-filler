from pro_filer.actions.main_actions import show_disk_usage  # NOQA
import pytest


@pytest.fixture
def create_files(tmp_path):
    files = ["file1.txt", "file2.txt", "file3.txt"]
    for file in files:
        path = tmp_path / file
        path.write_text("This is some content")

    return [str(tmp_path / file) for file in files]


def test_show_disk_usage_empty(capsys):
    context = {
        "all_files": []
    }
    show_disk_usage(context)
    result = capsys.readouterr()
    assert result.out == "Total size: 0\n"


def test_show_disk_usage(create_files, capsys):
    context = {
        "all_files": create_files
    }
    show_disk_usage(context)
    result = capsys.readouterr()
    lines = result.out.split("\n")

    assert len(lines) == 5
    assert "Total size: 60" in lines[-2]

    sizes = [int(line.split()[1]) for line in lines[:-2]]
    sorted_sizes = sorted(sizes, reverse=True)
    assert sorted_sizes == sorted(sizes, reverse=True)

    for line in lines[:-2]:
        assert "(33%)" in line
