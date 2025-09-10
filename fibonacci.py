"""
Fibonacci series script.

Usage:
  python3 fibonacci.py 10   # prints first 10 Fibonacci numbers
"""

from __future__ import annotations

import argparse
from typing import Iterator, List


def fibonacci(n: int) -> Iterator[int]:
    """Yield the first n Fibonacci numbers (starting from 0).

    Args:
        n: Number of terms to generate. Must be >= 0.

    Yields:
        The Fibonacci numbers in order: 0, 1, 1, 2, 3, ...
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Print the first N Fibonacci numbers.")
    parser.add_argument("n", type=int, help="number of terms to print (>= 0)")
    parser.add_argument(
        "--sep",
        default=" ",
        help="separator between numbers (default: space)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    terms: List[str] = [str(x) for x in fibonacci(args.n)]
    print(args.sep.join(terms))


if __name__ == "__main__":
    main()

