import re
import argparse
from typing import Sequence, Optional

TOKEN_REGEX = re.compile(r"\d{9,}:[-\w]{34,}")


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to check")
    parser.add_argument(
        "--excluded-files",
        dest="excl",
        nargs="*",
        help="Files to exclude from checking",
    )
    args = parser.parse_args(argv)

    excluded = []
    if args.excl is not None:
        excluded += args.excl
    file_list = [file for file in args.filenames if file not in excluded]

    found = []
    for filename in file_list:
        with open(filename, "r+", encoding="UTF-8") as f:
            lines = f.read()
            if re.search(TOKEN_REGEX, lines):
                found.append(filename)

    ret = len(found)
    if ret > 0:
        print(
            """Potential Telegram bot tokens found in the following file{}:
{}""".format(
                "s" if ret > 1 else "", "\n".join(found)
            )
        )
    return ret


if __name__ == "__main__":
    exit(main())
