import os
import shutil
import subprocess


print(os.getcwd())  # prints /absolute/path/to/{{ cookiecutter.dist_name }}


def run_cmd(args, **kwargs):
    return subprocess.run(args, check=True, **kwargs)


def check_command_exists(cmd):
    try:
        run_cmd([cmd, "-h"], capture_output=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print(f"{cmd} command is not installed")
        return False

    return True


def remove(file_path):
    if os.path.isfile(file_path):
        os.remove(file_path)
    elif os.path.isdir(file_path):
        shutil.rmtree(file_path)


def setup_pre_commit():
    if not check_command_exists("pre-commit"):
        return
    if not check_command_exists("git"):
        return

    # Run pre-commit install
    run_cmd(["git", "init"])
    run_cmd(["pre-commit", "install"])


def main():
    use_dependabot = "{{ cookiecutter.use_dependabot }}" == "y"
    use_pre_commit_hook = "{{ cookiecutter.use_pre_commit_hook }}" == "y"

    if use_pre_commit_hook:
        setup_pre_commit()
    else:
        remove(".pre-commit-config.yaml")

    if not use_dependabot:
        remove(os.path.join(os.getcwd(), ".github/dependabot.yml"))


if __name__ == '__main__':
    main()
