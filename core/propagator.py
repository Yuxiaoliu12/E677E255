"""E677 constraint propagation engine.

E677: x = y ◇ (x ◇ ((y ◇ x) ◇ y)) for all x, y.

For each pair (x, y), we track the evaluation chain:
  e1 = y◇x         → cell (y, x)
  e2 = e1◇y        → cell (e1, y)     [depends on e1]
  e3 = x◇e2        → cell (x, e2)     [depends on e2]
  e4 = y◇e3        → cell (y, e3)     [depends on e3]
  ASSERT: e4 == x

Key propagation rules:
1. Forward: e1,e2,e3 known → force e4 = table[y][e3] = x
2. Mid-chain: e1,e2 known, L_y⁻¹(x) known → force e3 = table[x][e2] = L_y⁻¹(x)
3. Naked single: row with n-1 cells filled → force last cell
4. Contradiction: e1,e2,e3,e4 all known but e4 ≠ x
"""

from __future__ import annotations

from collections import deque

from core.bijectivity import ContradictionError
from core.magma import PartialMagma


class ConstraintInstance:
    """Tracks one (x, y) instance of the E677 equation.

    The chain: e1 = y◇x, e2 = e1◇y, e3 = x◇e2, e4 = y◇e3.
    Constraint: e4 == x.
    """

    __slots__ = ("x", "y")

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class E677Propagator:
    """Constraint propagation engine for E677 on a PartialMagma.

    Maintains watcher lists: for each cell (a, b), which constraint
    instances could be affected when that cell is assigned.

    The watcher structure is dynamic — when e1 becomes known, we know
    which cell e2 lives in and can register watchers there, etc.
    """

    def __init__(self, magma: PartialMagma):
        self.magma = magma
        self.n = magma.n

        # Static watchers: cell (a,b) -> list of (x, y) constraints
        # where cell (a,b) is the e1 = y◇x cell, i.e., a=y, b=x.
        # So constraint (x=b, y=a) watches cell (a, b) for e1.
        # We store constraint instances as (x, y) tuples for compactness.

        # For e1: cell (y, x) is watched by constraint (x, y)
        # For e2: cell (e1, y) — we only know this once e1 is resolved
        # For e3: cell (x, e2) — we only know this once e2 is resolved
        # For e4: cell (y, e3) — we only know this once e3 is resolved

        # Strategy: we maintain static watchers for e1 (always known which
        # cell it is). For e2/e3/e4, we re-evaluate all constraints involving
        # the assigned cell. This is O(n) per assignment in the worst case
        # but avoids complex dynamic watcher management.

        # cell_to_e1_constraints[y][x] = constraint (x, y)
        # This is just the identity mapping, so we iterate directly.

        # For efficient reverse lookup: when cell (a, b) is assigned,
        # which constraints have their e2/e3/e4 at (a, b)?
        # e2 is at cell (e1_val, y) — so any constraint (x, y=b) where
        #   table[b][x] = a (i.e., e1 = a, meaning y◇x = a, so a = table[b][x])
        # This requires scanning, but we can organize it.

        # For simplicity and correctness, we use a "trigger on any cell"
        # approach: when (a, b) is assigned, check all constraints where
        # y = a (the row could be e1, e2, or e4 step) and where x = a
        # or involve column b. We batch-check all n constraints for each
        # row and all relevant constraints.

        # More precisely: cell (a, b) can appear in a constraint's chain as:
        # - e1 = y◇x at cell (y, x): this is constraint (x=b, y=a)
        # - e2 = e1◇y at cell (e1, y): for any constraint (x', y=b) where
        #   table[b][x'] = a (e1 = a)
        # - e3 = x◇e2 at cell (x, e2): for any constraint (x=a, y') where
        #   the chain gives e2 = b
        # - e4 = y◇e3 at cell (y, e3): for any constraint (x', y=a) where
        #   the chain gives e3 = b

        # We precompute the e1 watchers (static). For others, we check
        # during propagation by evaluating all constraints that *could*
        # be affected.

    def propagate(self, a: int, b: int, c: int) -> list[tuple[int, int, int]]:
        """After assigning table[a][b] = c, propagate all E677 consequences.

        Returns list of (row, col, val) forced assignments.
        Raises ContradictionError on conflict — but first undoes all
        intermediate forced assignments to keep the magma state clean.
        """
        forced: list[tuple[int, int, int]] = []
        queue: deque[tuple[int, int, int]] = deque()
        queue.append((a, b, c))

        try:
            while queue:
                ra, rb, rc = queue.popleft()
                new_forced = self._check_affected_constraints(ra, rb, rc)
                # Also check naked singles for the row
                ns = self._check_naked_singles(ra)
                new_forced.extend(ns)

                for (fa, fb, fc) in new_forced:
                    if self.magma.is_assigned(fa, fb):
                        if self.magma.get(fa, fb) != fc:
                            raise ContradictionError(
                                f"Propagation conflict: cell ({fa},{fb}) is "
                                f"{self.magma.get(fa, fb)} but forced to {fc}",
                                cell=(fa, fb),
                            )
                        continue  # already consistent
                    self.magma.assign(fa, fb, fc)
                    forced.append((fa, fb, fc))
                    queue.append((fa, fb, fc))

        except ContradictionError:
            # Undo all intermediate forced assignments before re-raising
            for fa, fb, _ in reversed(forced):
                self.magma.unassign(fa, fb)
            forced.clear()
            raise

        return forced

    def _check_affected_constraints(
        self, a: int, b: int, c: int
    ) -> list[tuple[int, int, int]]:
        """Check all constraint instances that could be affected by
        the assignment table[a][b] = c.

        We check constraints where:
        1. (a, b) is the e1 cell → constraint (x=b, y=a)
        2. (a, b) could be an e2 cell → constraints (x', y=b) where e1=a
        3. (a, b) could be an e3 cell → constraints (x=a, y') where e2=b
        4. (a, b) could be an e4 cell → constraints (x', y=a) where e3=b
        """
        forced: list[tuple[int, int, int]] = []
        m = self.magma

        # Case 1: cell (a, b) is e1 for constraint (x=b, y=a)
        self._try_propagate_constraint(b, a, forced)

        # Case 2: cell (a, b) is e2 = e1◇y for some constraint.
        # e2 is at cell (e1, y). So a = e1, b = y.
        # For constraint (x', y=b): e1 = table[b][x'].
        # We need e1 = a, i.e., table[b][x'] = a.
        # That means x' = L_b⁻¹(a).
        x_prime = m.left_inverse(b, a)
        if x_prime is not None:
            self._try_propagate_constraint(x_prime, b, forced)

        # Case 3: cell (a, b) is e3 = x◇e2 for some constraint.
        # e3 is at cell (x, e2). So a = x, b = e2.
        # For constraint (x=a, y'): we need to find y' such that
        # the chain gives e2 = b. That means:
        #   e1 = y'◇a = table[y'][a]
        #   e2 = e1◇y' = table[e1][y'] = b
        # We check all y' where table[y'][a] is known.
        for y_prime in range(self.n):
            e1_val = m.get(y_prime, a)
            if e1_val is not None:
                e2_check = m.get(e1_val, y_prime)
                if e2_check == b:
                    self._try_propagate_constraint(a, y_prime, forced)

        # Case 4: cell (a, b) is e4 = y◇e3 for some constraint.
        # e4 is at cell (y, e3). So a = y, b = e3.
        # For constraint (x', y=a): we need e3 = b.
        # Chain: e1 = table[a][x'], e2 = table[e1][a], e3 = table[x'][e2].
        # We need table[x'][e2] = b. We check all x'.
        for x_prime in range(self.n):
            e1_val = m.get(a, x_prime)
            if e1_val is None:
                continue
            e2_val = m.get(e1_val, a)
            if e2_val is None:
                continue
            e3_val = m.get(x_prime, e2_val)
            if e3_val == b:
                # e4 = table[a][b] = c, constraint says e4 must = x_prime
                if c != x_prime:
                    raise ContradictionError(
                        f"E677 violated: constraint ({x_prime},{a}) has "
                        f"e4={c} but expected {x_prime}",
                        cell=(a, b),
                    )

        return forced

    def _try_propagate_constraint(
        self, x: int, y: int, forced: list[tuple[int, int, int]]
    ) -> None:
        """Try to propagate the constraint for pair (x, y).

        Chain: e1 = y◇x, e2 = e1◇y, e3 = x◇e2, e4 = y◇e3.
        Constraint: e4 == x.
        """
        m = self.magma

        # Step 1: e1 = table[y][x]
        e1 = m.get(y, x)
        if e1 is None:
            # Can't propagate without e1. But check reverse:
            # If we know L_y⁻¹(x) (call it v), and e2, e3 are somehow
            # determined... this is rare without e1. Skip.
            return

        # Step 2: e2 = table[e1][y]
        e2 = m.get(e1, y)
        if e2 is None:
            # Can't continue chain. No propagation possible here.
            return

        # Step 3: e3 = table[x][e2]
        e3 = m.get(x, e2)

        # We also know L_y⁻¹(x) from the identity:
        # L_y⁻¹(x) = x ◇ ((y◇x)◇y) = x ◇ e2 = e3
        ly_inv_x = m.left_inverse(y, x)  # b such that y◇b = x

        if e3 is None:
            # Mid-chain forcing: if L_y⁻¹(x) is known, force e3
            if ly_inv_x is not None:
                forced.append((x, e2, ly_inv_x))
            return

        # All of e1, e2, e3 known.
        # Consistency check: e3 should equal L_y⁻¹(x)
        if ly_inv_x is not None and e3 != ly_inv_x:
            raise ContradictionError(
                f"E677 chain inconsistency: constraint ({x},{y}) has "
                f"e3={e3} but L_{y}⁻¹({x})={ly_inv_x}",
                cell=(x, e2),
            )

        # Step 4: e4 = table[y][e3]
        e4 = m.get(y, e3)
        if e4 is None:
            # Forward forcing: force e4 = x
            forced.append((y, e3, x))
            return

        # Full chain known — verify
        if e4 != x:
            raise ContradictionError(
                f"E677 violated: constraint ({x},{y}) has e4={e4} != x={x}",
                cell=(y, e3),
            )

    def _check_naked_singles(self, row: int) -> list[tuple[int, int, int]]:
        """Check if row has exactly one unassigned cell (naked single)."""
        forced_pair = self.magma.left_perms[row].forced_single()
        if forced_pair is not None:
            col, val = forced_pair
            if not self.magma.is_assigned(row, col):
                return [(row, col, val)]
        return []

    def check_all_constraints(self) -> list[tuple[int, int, int]]:
        """Scan all n² constraints for any new propagations.

        Useful after batch assignments or as a consistency check.
        More expensive than incremental propagation but catches everything.
        """
        forced: list[tuple[int, int, int]] = []
        for x in range(self.n):
            for y in range(self.n):
                self._try_propagate_constraint(x, y, forced)
        # Check all naked singles
        for row in range(self.n):
            forced.extend(self._check_naked_singles(row))
        return forced
