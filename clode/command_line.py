import re
import subprocess


class CommandException(Exception):
    pass


def run_command(*args: str | None) -> str:
    filtered_args: list[str] = [arg for arg in args if arg is not None]
    print(f"Running: {filtered_args}")
    result = subprocess.run(filtered_args, shell=True)
    if result.returncode != 0:
        raise CommandException(
            f'Error {result.returncode} when running {" ".join(filtered_args)}',
            result.stderr.decode(),
        )

    return result.stdout.decode()


def clone(url: str, path: str | None = None) -> str:
    """Clone a git repository from `url` and return the path"""
    result = run_command("git", "clone", "--progress", url, path)
    lines = result.splitlines()
    print(lines)
    first_line = lines[0]
    output = re.search("(?<=').+(?=')", first_line)
    if output is None:
        raise CommandException(f"Unable to find output directory in line: {first_line}")
    return output.group(0)


def code(path: str):
    """Open a directory in VSCode"""
    run_command("code", path)
