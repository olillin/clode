import argparse
from clode import clode


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="clode",
        description="CLI tool to open git repositories quickly",
    )
    parser.add_argument("repository", type=str)
    parser.add_argument("output", type=str, nargs="?")

    return parser.parse_args()


def main():
    args = parse_arguments()
    clode(args.repository, args.output)


if __name__ == "__main__":
    main()
