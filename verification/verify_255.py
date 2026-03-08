"""Verification of E255: x = ((x ◇ x) ◇ x) ◇ x for each element.

Also checks the equivalent condition under E677: existence of y with y◇x = x.
"""

from __future__ import annotations

import numpy as np


def verify_e255(table: np.ndarray) -> tuple[bool, list[int]]:
    """Check E255 for every element.

    Args:
        table: n×n numpy array where table[a][b] = a◇b.

    Returns:
        (all_pass, violators) where violators is a list of elements x
        where ((x◇x)◇x)◇x != x.
    """
    n = table.shape[0]
    violators = []
    for x in range(n):
        if not check_e255_element(table, x):
            violators.append(x)
    return (len(violators) == 0, violators)


def check_e255_element(table: np.ndarray, x: int) -> bool:
    """Check E255 at a single element x: ((x◇x)◇x)◇x == x."""
    s1 = table[x, x]       # x◇x
    s2 = table[s1, x]      # (x◇x)◇x
    s3 = table[s2, x]      # ((x◇x)◇x)◇x
    return s3 == x


def check_fixer_exists(table: np.ndarray, x: int) -> int | None:
    """Find y such that y◇x = x (the "fixer" of x).

    Under E677, existence of such y is equivalent to E255 at x.
    If found, y must equal ((x◇x)◇x)◇x.

    Returns y if found, None otherwise.
    """
    n = table.shape[0]
    for y in range(n):
        if table[y, x] == x:
            return y
    return None
