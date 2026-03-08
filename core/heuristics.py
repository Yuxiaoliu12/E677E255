"""Pluggable heuristics for cell and value selection in DPLL search.

Each heuristic implements the CellValueHeuristic protocol:
  choose_next(magma, propagator) → (row, col, value)
"""

from __future__ import annotations

from typing import Protocol

from core.magma import PartialMagma


class CellValueHeuristic(Protocol):
    """Protocol for search heuristics."""

    def choose_next(
        self, magma: PartialMagma
    ) -> tuple[int, int, int] | None:
        """Return (row, col, value) for the next assignment.

        Returns None if no unassigned cells remain.
        """
        ...


class MostConstrainedFirst:
    """MRV (Minimum Remaining Values) heuristic.

    Pick the unassigned cell with the fewest available values.
    Among ties, prefer cells in more-filled rows.
    For value selection: pick the smallest available value (deterministic).
    """

    def choose_next(
        self, magma: PartialMagma
    ) -> tuple[int, int, int] | None:
        n = magma.n
        best_cell: tuple[int, int] | None = None
        best_count = n + 1

        for a in range(n):
            for b in range(n):
                if magma.is_assigned(a, b):
                    continue
                avail = magma.available_values(a, b)
                count = len(avail)
                if count == 0:
                    # Dead end — no available values
                    return None
                if count < best_count:
                    best_count = count
                    best_cell = (a, b)
                    if count == 1:
                        # Can't do better than 1
                        break
            if best_count == 1:
                break

        if best_cell is None:
            return None

        a, b = best_cell
        avail = magma.available_values(a, b)
        value = min(avail)  # deterministic: smallest available
        return (a, b, value)

    def ordered_values(self, magma: PartialMagma, a: int, b: int) -> list[int]:
        """Return available values in the order they should be tried."""
        return sorted(magma.available_values(a, b))


class RowFirstHeuristic:
    """Fill the table row by row, left to right.

    Simple but effective for generating training data because it
    produces a consistent ordering across runs.
    """

    def choose_next(
        self, magma: PartialMagma
    ) -> tuple[int, int, int] | None:
        n = magma.n
        for a in range(n):
            for b in range(n):
                if magma.is_assigned(a, b):
                    continue
                avail = magma.available_values(a, b)
                if not avail:
                    return None
                return (a, b, min(avail))
        return None

    def ordered_values(self, magma: PartialMagma, a: int, b: int) -> list[int]:
        return sorted(magma.available_values(a, b))
