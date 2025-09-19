#!/usr/bin/env python3
"""
Fibonacci series generator CLI.

Usage examples:
  - First 10 terms:   python fibonacci.py --terms 10
  - Up to value 100:  python fibonacci.py --max 100

By default prints the first 10 terms if no option is given.
"""

from __future__ import annotations

import argparse
from typing import Iterator, List


def fibonacci_terms(n: int) -> Iterator[int]:
    """Yield the first n Fibonacci numbers starting from 0.

    Example for n=6: 0, 1, 1, 2, 3, 5
    """
    if n <= 0:
        return
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def fibonacci_upto(max_value: int) -> Iterator[int]:
    """Yield Fibonacci numbers up to and including max_value (>= 0)."""
    if max_value < 0:
        return
    a, b = 0, 1
    while a <= max_value:
        yield a
        a, b = b, a + b


def parse_args(argv: List[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Print Fibonacci series")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--terms", type=int, help="number of terms to print (>= 0)")
    group.add_argument("--max", dest="max_value", type=int, help="print terms up to this value (>= 0)")
    parser.add_argument("--sep", default=", ", help="separator between numbers (default: ', ')")
    return parser.parse_args(argv)


def main(argv: List[str] | None = None) -> None:
    args = parse_args(argv)

    if args.terms is None and args.max_value is None:
        # Default: first 10 terms
        args.terms = 10

    if args.terms is not None:
        n = args.terms
        if n < 0:
            raise SystemExit("--terms must be >= 0")
        series = list(fibonacci_terms(n))
    else:
        mv = args.max_value
        if mv < 0:
            raise SystemExit("--max must be >= 0")
        series = list(fibonacci_upto(mv))

    print(args.sep.join(str(x) for x in series))


if __name__ == "__main__":
    main()

