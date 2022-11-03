import os
import re
import subprocess
from pathlib import Path

from binaryornot.check import is_binary

RE_OBJ = re.compile(r"{{(\s?cookiecutter)[.](.*?)}}")


def check_paths(paths):
    """Method to check all paths have correct substitutions."""
    # Assert that no match is found in any of the files
    for path in paths:
        if is_binary(str(path)):
            continue

        with path.open() as fd:
            content = fd.read()
            match = RE_OBJ.search(content)
            assert match is None, f"cookiecutter variable not replaced in {path}"


def test_generate_project(cookies, base_context):
    result = cookies.bake(extra_context=base_context)

    assert result.exit_code == 0, result.exception
    assert result.exception is None
    assert result.project.basename == "boardpack-project"
    assert result.project.isdir()

    paths = [
        Path(dirpath) / file_path
        for dirpath, subdirs, files in os.walk(result.project)
        for file_path in files
    ]
    assert paths
    check_paths(paths)


def test_top_package_description(cookies, base_context):
    result = cookies.bake(extra_context=base_context)

    full_path = os.path.join(
        str(result.project), result.context["package_name"], "__init__.py"
    )
    with open(full_path) as fp:
        description = fp.readline()

    assert description[3:-4] == result.context["project_short_description"]


def test_install_dependencies(cookies, base_context):
    result = cookies.bake(extra_context=base_context)
    subprocess.check_call(
        ["flit", "install", "--symlink"],
        env=os.environ.copy(),
        cwd=result.project_path,
    )
