import argparse
from typing import Sequence, Optional, List

EXCLUDED: List[str] = ["pkg-resources==0.0.0"]


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to check")
    parser.add_argument(
        "--excluded-entries",
        dest="excl",
        nargs="*",
        help="Additional entries to exclude",
    )
    args = parser.parse_args(argv)

    excluded_entries = EXCLUDED

    if args.excl is not None:
        excluded_entries += args.excl

    ret = 0

    for filename in args.filenames:
        with open(filename, "r+", encoding="UTF-8") as f:
            lines = f.readlines()
            f.seek(0)
            f.truncate()
            new_lines = [line for line in lines if line.strip() not in excluded_entries]
            removed = len(lines) - len(new_lines)
            if removed > 0:
                print(f"Removed {removed} entries from {filename}")
                ret = 1
            f.writelines(new_lines)

    return ret


if __name__ == "__main__":
    exit(main())
