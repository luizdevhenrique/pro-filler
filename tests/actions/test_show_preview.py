from pro_filer.actions.main_actions import show_preview  # NOQA


def test_show_preview_context(capsys):
    context = {"all_files": [], "all_dirs": []}

    show_preview(context)
    result = capsys.readouterr()
    assert result.out == "Found 0 files and 0 directories\n"


def test_show_preview(capsys):
    context = {
        "all_files": ["src/__init__.py",
                      "src/app.py", "src/utils/__init__.py"],
        "all_dirs": ["src", "src/utils"]
    }
    show_preview(context)
    result = capsys.readouterr()
    assert result.out == (
        "Found 3 files and 2 directories\n"
        "Files: ['src/__init__.py', 'src/app.py', 'src/utils/__init__.py']\n"
        "Directories: ['src', 'src/utils']\n"
    )
