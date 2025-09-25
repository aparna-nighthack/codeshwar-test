#!/usr/bin/env python3
"""
Fibonacci series generator script.

Usage examples:
  - First N terms:   python3 fibonacci.py --terms 10
  - Up to a value:   python3 fibonacci.py --max-value 1000

Options:
  --terms/-n N        Print the first N Fibonacci numbers (N >= 1)
  --max-value/-m V    Print all Fibonacci numbers <= V (V >= 0)
  --sep SEPARATOR     Separator for output (default: ", ")
"""

from __future__ import annotations

import argparse
from typing import Iterator, List


def fib_terms(n: int) -> Iterator[int]:
    """Yield the first n Fibonacci numbers (starting at 0).

    Raises ValueError if n < 0.
    """
    if n < 0:
        raise ValueError("n must be >= 0")
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def fib_upto(max_value: int) -> Iterator[int]:
    """Yield Fibonacci numbers up to and including max_value."""
    a, b = 0, 1
    while a <= max_value:
        yield a
        a, b = b, a + b


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Print a Fibonacci series by count or max value.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-n",
        "--terms",
        type=int,
        help="Number of terms to print (>= 1)",
    )
    group.add_argument(
        "-m",
        "--max-value",
        type=int,
        help="Print all terms <= this value (>= 0)",
    )
    parser.add_argument(
        "--sep",
        default=", ",
        help="Separator string between numbers",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.terms is not None:
        if args.terms < 1:
            raise SystemExit("--terms must be >= 1")
        sequence: List[int] = list(fib_terms(args.terms))
    else:
        # args.max_value is guaranteed by argparse to be set if terms isn't
        if args.max_value < 0:
            raise SystemExit("--max-value must be >= 0")
        sequence = list(fib_upto(args.max_value))

    print(args.sep.join(str(x) for x in sequence))


if __name__ == "__main__":
    main()

