"""
Fibonacci Series Script

Generates the Fibonacci series for a given number of terms and prints
both the series and the sum of its numbers.

Usage:
  - With CLI argument:  python3 fibonacci_series.py 10
  - Interactive prompt: python3 fibonacci_series.py  (then enter a number)
"""

from __future__ import annotations

import argparse
import sys


def generate_fibonacci(terms: int) -> list[int]:
    """Return the Fibonacci sequence with the given number of terms.

    Args:
        terms: Positive integer count of terms to generate.

    Returns:
        List of integers representing the Fibonacci sequence.

    Raises:
        ValueError: If terms is not a positive integer.
    """
    if terms <= 0:
        raise ValueError("Number of terms must be a positive integer.")

    sequence: list[int] = []
    a, b = 0, 1
    for _ in range(terms):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate Fibonacci series and its sum.")
    parser.add_argument(
        "terms",
        type=int,
        nargs="?",
        help="Number of terms to generate (positive integer).",
    )
    args = parser.parse_args()

    if args.terms is None:
        try:
            user_input = input("Enter number of terms: ").strip()
            terms = int(user_input)
        except Exception:
            print("Invalid input. Please enter an integer.")
            sys.exit(1)
    else:
        terms = args.terms

    try:
        series = generate_fibonacci(terms)
    except ValueError as exc:
        print(exc)
        sys.exit(1)

    series_sum = sum(series)
    print("Fibonacci series:", " ".join(map(str, series)))
    print("Sum:", series_sum)


if __name__ == "__main__":
    main()

