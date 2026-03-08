"""Left-bijectivity enforcement via partial permutation tracking.

In any finite E677 magma, each left-multiplication map L_y is a bijection.
PartialPermutation tracks the state of each L_y during search.
"""

from __future__ import annotations

import numpy as np

UNSET = -1


class ContradictionError(Exception):
    """Raised when an assignment creates an inconsistency."""

    def __init__(self, message: str, cell: tuple[int, int] | None = None):
        self.cell = cell
        super().__init__(message)


class PartialPermutation:
    """Tracks a partial bijection from {0,...,n-1} to {0,...,n-1}.

    Used to enforce that each row of the multiplication table is a
    permutation (left-bijectivity). Provides O(1) assignment, removal,
    and available-value queries.
    """

    __slots__ = ("n", "forward", "backward", "unassigned_domain", "unassigned_range")

    def __init__(self, n: int):
        self.n = n
        self.forward: dict[int, int] = {}   # domain -> range
        self.backward: dict[int, int] = {}  # range -> domain
        self.unassigned_domain: set[int] = set(range(n))
        self.unassigned_range: set[int] = set(range(n))

    def assign(self, x: int, y: int) -> None:
        """Map x -> y. Raises ContradictionError if conflict."""
        if x in self.forward:
            if self.forward[x] == y:
                return  # already assigned consistently
            raise ContradictionError(
                f"Domain {x} already maps to {self.forward[x]}, cannot map to {y}"
            )
        if y in self.backward:
            raise ContradictionError(
                f"Range {y} already taken by {self.backward[y]}, cannot assign from {x}"
            )
        self.forward[x] = y
        self.backward[y] = x
        self.unassigned_domain.discard(x)
        self.unassigned_range.discard(y)

    def unassign(self, x: int) -> None:
        """Remove the mapping from x."""
        if x not in self.forward:
            return
        y = self.forward.pop(x)
        del self.backward[y]
        self.unassigned_domain.add(x)
        self.unassigned_range.add(y)

    def get(self, x: int) -> int | None:
        """Return f(x) if assigned, else None."""
        return self.forward.get(x)

    def inverse(self, y: int) -> int | None:
        """Return x such that f(x) = y, or None if y is not yet in image."""
        return self.backward.get(y)

    def available_range(self) -> set[int]:
        """Return range values not yet assigned to any domain element."""
        return self.unassigned_range

    def num_assigned(self) -> int:
        return len(self.forward)

    def is_complete(self) -> bool:
        return len(self.forward) == self.n

    def forced_single(self) -> tuple[int, int] | None:
        """If exactly one domain element and one range element remain,
        return the forced (domain, range) pair."""
        if len(self.unassigned_domain) == 1 and len(self.unassigned_range) == 1:
            d = next(iter(self.unassigned_domain))
            r = next(iter(self.unassigned_range))
            return (d, r)
        return None

    def copy(self) -> PartialPermutation:
        pp = PartialPermutation.__new__(PartialPermutation)
        pp.n = self.n
        pp.forward = self.forward.copy()
        pp.backward = self.backward.copy()
        pp.unassigned_domain = self.unassigned_domain.copy()
        pp.unassigned_range = self.unassigned_range.copy()
        return pp
