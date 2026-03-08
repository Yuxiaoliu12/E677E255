"""Brute-force verification that a completed multiplication table satisfies E677.

E677: x = y * (x * ((y * x) * y)) for all x, y.
"""

from __future__ import annotations

import numpy as np


def verify_e677(table: np.ndarray) -> tuple[bool, list[tuple[int, int]]]:
    """Check E677 for every (x, y) pair.

    Args:
        table: n×n numpy array where table[a][b] = a◇b.

    Returns:
        (all_pass, failures) where failures is a list of (x, y) pairs
        that violate E677.
    """
    n = table.shape[0]
    failures = []
    for x in range(n):
        for y in range(n):
            # e1 = y◇x
            e1 = table[y, x]
            # e2 = (y◇x)◇y = e1◇y
            e2 = table[e1, y]
            # e3 = x◇((y◇x)◇y) = x◇e2
            e3 = table[x, e2]
            # e4 = y◇(x◇((y◇x)◇y)) = y◇e3
            e4 = table[y, e3]
            if e4 != x:
                failures.append((x, y))
    return (len(failures) == 0, failures)


def verify_e677_single(table: np.ndarray, x: int, y: int) -> bool:
    """Check E677 for a specific (x, y) pair."""
    e1 = table[y, x]
    e2 = table[e1, y]
    e3 = table[x, e2]
    e4 = table[y, e3]
    return e4 == x
