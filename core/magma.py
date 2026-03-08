"""Partial multiplication table for finite magmas.

Represents an n×n table with left-bijectivity enforcement.
Each row is tracked as a PartialPermutation ensuring L_y is always
a partial bijection.
"""

from __future__ import annotations

from typing import Any

import numpy as np

from core.bijectivity import ContradictionError, PartialPermutation

UNSET = np.int16(-1)


class PartialMagma:
    """An n×n partial multiplication table with left-bijectivity tracking.

    table[a, b] = a ◇ b (row = left operand, col = right operand).
    UNSET (-1) marks unassigned cells.

    Each row a is backed by a PartialPermutation enforcing that L_a
    is a partial bijection (required by E677 + finiteness).
    """

    def __init__(self, n: int):
        self.n = n
        self.table = np.full((n, n), UNSET, dtype=np.int16)
        self.left_perms: list[PartialPermutation] = [
            PartialPermutation(n) for _ in range(n)
        ]
        self.num_assigned = 0
        # Track right-multiplication images: right_images[b] = {a◇b : a assigned}
        self.right_images: list[dict[int, list[int]]] = [
            {} for _ in range(n)
        ]  # col -> {value -> [rows producing it]}

    def get(self, a: int, b: int) -> int | None:
        """Return a◇b if assigned, else None."""
        v = self.table[a, b]
        return None if v == UNSET else int(v)

    def is_assigned(self, a: int, b: int) -> bool:
        return self.table[a, b] != UNSET

    def assign(self, a: int, b: int, c: int) -> None:
        """Set a◇b = c. Raises ContradictionError on conflict.

        Does NOT propagate — propagation is handled by the Propagator.
        This only updates the table and permutation tracking.
        """
        current = self.table[a, b]
        if current != UNSET:
            if current == c:
                return  # already set consistently
            raise ContradictionError(
                f"Cell ({a},{b}) already has value {current}, cannot set to {c}",
                cell=(a, b),
            )

        # Check and update left-bijectivity for row a
        self.left_perms[a].assign(b, c)

        # Update table
        self.table[a, b] = np.int16(c)
        self.num_assigned += 1

        # Update right-image tracking for column b
        rim = self.right_images[b]
        if c not in rim:
            rim[c] = [a]
        else:
            rim[c].append(a)

    def unassign(self, a: int, b: int) -> None:
        """Remove assignment at (a, b). For backtracking."""
        current = self.table[a, b]
        if current == UNSET:
            return
        c = int(current)

        self.left_perms[a].unassign(b)
        self.table[a, b] = UNSET
        self.num_assigned -= 1

        # Update right-image tracking
        rim = self.right_images[b]
        rows = rim[c]
        rows.remove(a)
        if not rows:
            del rim[c]

    def available_values(self, a: int, b: int) -> set[int]:
        """Return values still available for cell (a, b).

        These are the range values not yet used in row a
        (left-bijectivity constraint).
        """
        return self.left_perms[a].available_range()

    def left_inverse(self, a: int, c: int) -> int | None:
        """Return b such that a◇b = c (i.e., L_a⁻¹(c)), or None."""
        return self.left_perms[a].inverse(c)

    def is_complete(self) -> bool:
        return self.num_assigned == self.n * self.n

    def fill_ratio(self) -> float:
        return self.num_assigned / (self.n * self.n)

    def right_cancel_failure_count(self) -> int:
        """Count columns where R_b is not injective on assigned cells."""
        count = 0
        for b in range(self.n):
            for val, rows in self.right_images[b].items():
                if len(rows) > 1:
                    count += 1
                    break  # one failure per column is enough to count
        return count

    def snapshot(self) -> dict[str, Any]:
        """Return a serializable snapshot of the current state."""
        return {
            "n": self.n,
            "num_assigned": self.num_assigned,
            "table": self.table.tolist(),
            "fill_ratio": self.fill_ratio(),
        }

    def to_numpy(self) -> np.ndarray:
        """Return the raw table (copy). UNSET cells are -1."""
        return self.table.copy()

    def copy(self) -> PartialMagma:
        """Deep copy for branching."""
        pm = PartialMagma.__new__(PartialMagma)
        pm.n = self.n
        pm.table = self.table.copy()
        pm.left_perms = [lp.copy() for lp in self.left_perms]
        pm.num_assigned = self.num_assigned
        pm.right_images = [
            {v: list(rows) for v, rows in rim.items()}
            for rim in self.right_images
        ]
        return pm

    def __repr__(self) -> str:
        return f"PartialMagma(n={self.n}, assigned={self.num_assigned}/{self.n*self.n})"
