from .command_line import clone, code, CommandException
import re
from colorama import Fore

import os

DEFAULT_CLODE_USERNAME = os.environ.get("DEFAULT_CLODE_USERNAME")


def clode(repository: str, output: str | None = None):
    # Resolve repository name only
    if re.match("^[a-zA-Z0-9._-]+$", repository):
        if DEFAULT_CLODE_USERNAME is None:
            print(
                Fore.RED
                + "No username provided and DEFAULT_CLODE_USERNAME is not set"
                + Fore.RESET
            )
            exit()

        repository = DEFAULT_CLODE_USERNAME + "/" + repository

    if re.match("^[a-zA-Z0-9._-]+/[a-zA-Z0-9._-]+$", repository):
        repository = "https://github.com/" + repository

    try:
        print(f"Cloning {Fore.YELLOW}{repository}{Fore.LIGHTBLACK_EX}")
        output_folder: str = clone(repository, output)
    except CommandException:
        print(Fore.RED + "git clone failed" + Fore.RESET)
        exit()

    print(f"{Fore.RESET}Opening {Fore.YELLOW}{output_folder}{Fore.RESET} in VSCode")
    code(output_folder)
