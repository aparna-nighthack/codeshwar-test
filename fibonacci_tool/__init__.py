"""Fibonacci sequence utilities and CLI.

This package provides:
- A simple Fibonacci sequence generator function.
- A CLI that supports generating by number of terms or up to a max value.
- Customizable output separator and helpful validation errors.

Run as a module:
    python -m fibonacci_tool --terms 10 --sep ", "

Or as a script (via __main__):
    python -m fibonacci_tool --max-value 1000
"""

from __future__ import annotations

from typing import Iterable, List


def fibonacci_terms(n: int) -> List[int]:
    """Return a list with the first ``n`` Fibonacci numbers (starting 0, 1).

    Args:
        n: Number of terms to generate. Must be >= 0.

    Raises:
        ValueError: If ``n`` is negative.
    """
    if n < 0:
        raise ValueError("terms must be non-negative")
    if n == 0:
        return []
    if n == 1:
        return [0]

    seq = [0, 1]
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq


def fibonacci_up_to(max_value: int) -> List[int]:
    """Return Fibonacci numbers up to and including ``max_value``.

    Starts from 0, 1 and stops when the next term would exceed ``max_value``.

    Args:
        max_value: The maximum value allowed in the sequence. Must be >= 0.

    Raises:
        ValueError: If ``max_value`` is negative.
    """
    if max_value < 0:
        raise ValueError("max_value must be non-negative")

    seq: List[int] = []
    a, b = 0, 1
    while a <= max_value:
        seq.append(a)
        a, b = b, a + b
    return seq

