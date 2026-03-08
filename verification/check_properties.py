"""Check structural properties of completed magma tables."""

from __future__ import annotations

import numpy as np


def is_left_cancellative(table: np.ndarray) -> bool:
    """Check if every L_y is injective (each row is a permutation)."""
    n = table.shape[0]
    for y in range(n):
        if len(set(table[y])) != n:
            return False
    return True


def is_right_cancellative(table: np.ndarray) -> bool:
    """Check if every R_x is injective (each column has distinct values)."""
    n = table.shape[0]
    for x in range(n):
        col = table[:, x]
        if len(set(col)) != n:
            return False
    return True


def is_idempotent(table: np.ndarray) -> bool:
    """Check if x◇x = x for all x."""
    n = table.shape[0]
    return all(table[x, x] == x for x in range(n))


def idempotent_elements(table: np.ndarray) -> list[int]:
    """Return list of elements x where x◇x = x."""
    n = table.shape[0]
    return [x for x in range(n) if table[x, x] == x]


def right_cancel_failures(table: np.ndarray) -> list[tuple[int, int, int]]:
    """Return all (a, b, x) where a◇x = b◇x and a != b."""
    n = table.shape[0]
    failures = []
    for x in range(n):
        seen: dict[int, int] = {}
        for a in range(n):
            v = int(table[a, x])
            if v in seen:
                failures.append((seen[v], a, x))
            else:
                seen[v] = a
    return failures


def square_map(table: np.ndarray) -> np.ndarray:
    """Return the square map S(x) = x◇x."""
    n = table.shape[0]
    return np.array([table[x, x] for x in range(n)], dtype=np.int16)


def is_commutative(table: np.ndarray) -> bool:
    """Check if a◇b = b◇a for all a, b."""
    return np.array_equal(table, table.T)
