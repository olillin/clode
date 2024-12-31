import re
import subprocess


class CommandException(Exception):
    pass


def run_command(*args: str | None) -> str | None:
    """Run a console command and return stdout"""
    filtered_args: list[str] = [arg for arg in args if arg is not None]
    result = subprocess.run(filtered_args, stderr=subprocess.PIPE, shell=True)
    if result.returncode != 0:
        raise CommandException(
            f'Error {result.returncode} when running {" ".join(filtered_args)}',
            result.stderr.decode(),
        )
    if result.stdout is not None:  # type: ignore
        return result.stdout.decode()


def clone(url: str, path: str | None = None) -> str:
    """Clone a git repository from `url` and return the path"""
    if path is None:
        m = re.search(r"(?<=\/)[^\/]+?(?=(\.git)?$)", url)
        if m is None:
            raise Exception(f"Invalid git repository url: {url}")
        path = m.group(0)

    run_command("git", "clone", url, path)

    return path


def code(path: str):
    """Open a directory in VSCode"""
    run_command("code", path)
