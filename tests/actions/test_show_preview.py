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
        "First 5 files: ['src/__init__.py', 'src/app.py',"
        " 'src/utils/__init__.py']\n"
        "First 5 directories: ['src', 'src/utils']\n"
    )


def test_show_preview_does_not_slice(capsys):
    context = {
        "all_files": ["src/__init__.py",
                      "src/app.py", "src/utils/__init__.py"],
        "all_dirs": ["src", "src/utils"]
    }
    show_preview(context)
    result = capsys.readouterr()
    assert result.out == (
        f"Found {len(context['all_files'])}"
        f" files and {len(context['all_dirs'])} directories\n"
        f"All files: {context['all_files']}\n"
        f"All directories: {context['all_dirs']}\n"
    )
