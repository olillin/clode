from command_line import clone, code, CommandException
import re

import os

DEFAULT_CLODE_USERNAME = os.environ.get("DEFAULT_CLODE_USERNAME")


def clode(repository: str, output: str | None = None):
    # Resolve repository name only
    if re.match("^[a-zA-Z0-9._-]+$", repository):
        if DEFAULT_CLODE_USERNAME is None:
            print("No username provided and DEFAULT_CLODE_USERNAME is not set")
            exit()

        repository = DEFAULT_CLODE_USERNAME + "/" + repository

    if re.match("^[a-zA-Z0-9._-]+/[a-zA-Z0-9._-]+$", repository):
        repository = "https://github.com/" + repository
        print(f"Resolved repository to '{repository}'")

    try:
        output_folder: str = clone(repository, output)
    except CommandException as e:
        print("git clone failed:")
        if len(e.args) > 1:
            print(e.args[1])
        else:
            print("".join(e.args))
        exit()

    print(f"Opening '{output_folder}' in VSCode...")
    code(output_folder)
