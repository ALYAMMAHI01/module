"""Utilities for list operations.

Provides `unique_numbers` which returns unique items from a list
while preserving the original order.
"""
from typing import Iterable, List


def unique_numbers(numbers: Iterable[float]) -> List[float]:
    """Return a list of unique numbers preserving input order.

    Example:
        >>> unique_numbers([1,2,2,3,1])
        [1, 2, 3]

    The function treats values using normal equality/hash semantics for numbers.
    """
    seen = set()
    out: List[float] = []
    for x in numbers:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


if __name__ == "__main__":
    # simple CLI: pass numbers separated by spaces
    import sys

    if len(sys.argv) > 1:
        try:
            nums = [float(a) for a in sys.argv[1:]]
        except ValueError:
            print("All arguments must be numbers")
            sys.exit(1)
        print(unique_numbers(nums))
    else:
        print("Usage: python module2/saeed_module2_3.py 1 2 2 3 1")
