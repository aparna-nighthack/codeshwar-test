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
    """
    Generate the first n Fibonacci numbers starting from 0.
    
    Parameters:
        n (int): Number of terms to generate; must be >= 0.
    
    Returns:
        iterator (Iterator[int]): An iterator that yields n Fibonacci numbers beginning with 0.
    
    Raises:
        ValueError: If `n` is less than 0.
    """
    if n < 0:
        raise ValueError("n must be >= 0")
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def fib_upto(max_value: int) -> Iterator[int]:
    """
    Yield Fibonacci numbers up to and including max_value.
    
    Parameters:
        max_value (int): Inclusive upper bound for generated values; if less than 0, the generator yields no values.
    
    Returns:
        Iterator[int]: Fibonacci numbers starting at 0 and continuing while each value is less than or equal to max_value.
    """
    a, b = 0, 1
    while a <= max_value:
        yield a
        a, b = b, a + b


def parse_args() -> argparse.Namespace:
    """
    Parse command-line arguments for the Fibonacci script.
    
    Provides a required mutually exclusive choice between:
    - --terms / -n: number of Fibonacci terms to print (integer >= 1 expected),
    - --max-value / -m: print all Fibonacci terms less than or equal to this value (integer >= 0 expected).
    Also accepts --sep to customize the output separator (default: ", ").
    
    Returns:
        argparse.Namespace: Parsed arguments with attributes `terms` (int or None), `max_value` (int or None), and `sep` (str).
    """
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
    """
    Run the command-line interface: parse arguments, generate the requested Fibonacci sequence, and print it using the configured separator.
    
    Parses command-line options produced by parse_args(); if the --terms option is provided, validates it and generates the first N Fibonacci numbers, otherwise validates --max-value and generates all Fibonacci numbers up to that value. The resulting sequence is printed with elements joined by the provided separator.
    
    Raises:
    	SystemExit: If --terms is less than 1 or --max-value is less than 0.
    """
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

