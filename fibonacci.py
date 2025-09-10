#!/usr/bin/env python3
"""
Fibonacci series utility.

Usage examples:
  - First N numbers:    python3 fibonacci.py --count 10
  - Up to a limit:      python3 fibonacci.py --limit 100
  - N-th number (0-indexed): python3 fibonacci.py --nth 20

Notes:
  - Sequence starts at 0, 1, 1, 2, 3, ...
  - "--nth" is 0-indexed (n=0 -> 0, n=1 -> 1).
"""

from __future__ import annotations

import argparse
import sys
from typing import Iterable, Optional


def fib_sequence(*, count: Optional[int] = None, limit: Optional[int] = None) -> Iterable[int]:
    """Generate Fibonacci numbers.

    Exactly one of `count` or `limit` must be provided.

    - If `count` is set, yields the first `count` numbers starting at 0.
    - If `limit` is set, yields numbers <= `limit`.
    """
    if (count is None) == (limit is None):
        raise ValueError("Provide exactly one of 'count' or 'limit'.")

    a, b = 0, 1

    if count is not None:
        if count < 0:
            raise ValueError("count must be non-negative")
        for _ in range(count):
            yield a
            a, b = b, a + b
        return

    # limit mode
    if limit is None:
        raise ValueError("limit must not be None when count is None")
    while a <= limit:
        yield a
        a, b = b, a + b


def fib_n(n: int) -> int:
    """Return the n-th Fibonacci number (0-indexed).

    Examples: fib_n(0)=0, fib_n(1)=1, fib_n(2)=1, fib_n(3)=2, ...
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate Fibonacci numbers.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--count",
        type=int,
        help="Print the first N Fibonacci numbers (starting at 0)",
    )
    group.add_argument(
        "--limit",
        type=int,
        help="Print Fibonacci numbers up to LIMIT (inclusive)",
    )
    group.add_argument(
        "--nth",
        type=int,
        help="Print the n-th Fibonacci number (0-indexed)",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    ns = parse_args(argv if argv is not None else sys.argv[1:])

    try:
        if ns.count is not None:
            seq = list(fib_sequence(count=ns.count))
            print(" ".join(str(x) for x in seq))
            return 0
        if ns.limit is not None:
            if ns.limit < 0:
                print("")
                return 0
            seq = list(fib_sequence(limit=ns.limit))
            print(" ".join(str(x) for x in seq))
            return 0
        # nth
        print(fib_n(ns.nth))
        return 0
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())

