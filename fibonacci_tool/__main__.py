from __future__ import annotations

import argparse
import sys
from typing import List

from . import fibonacci_terms, fibonacci_up_to


def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="fibonacci_tool",
        description=(
            "Generate Fibonacci sequences either by number of terms or up to a maximum value. "
            "Customize the output separator."
        ),
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-t",
        "--terms",
        type=int,
        help="Number of terms to generate (>= 0).",
    )
    group.add_argument(
        "-m",
        "--max-value",
        type=int,
        dest="max_value",
        help="Generate terms up to and including this maximum value (>= 0).",
    )

    parser.add_argument(
        "--sep",
        default=" ",
        help="Separator between numbers (default: space).",
    )

    return parser.parse_args(argv)


def main(argv: List[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]

    try:
        args = parse_args(argv)
    except SystemExit as e:
        # argparse already printed an error; propagate exit code
        return int(e.code)

    try:
        if args.terms is not None:
            if args.terms < 0:
                print("error: --terms must be non-negative", file=sys.stderr)
                return 2
            seq = fibonacci_terms(args.terms)
        else:
            # max_value mode
            if args.max_value is None:
                print("error: one of --terms or --max-value is required", file=sys.stderr)
                return 2
            if args.max_value < 0:
                print("error: --max-value must be non-negative", file=sys.stderr)
                return 2
            seq = fibonacci_up_to(args.max_value)
    except ValueError as ve:
        print(f"error: {ve}", file=sys.stderr)
        return 2

    # Print results
    if seq:
        print(args.sep.join(str(x) for x in seq))
    else:
        print("")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

