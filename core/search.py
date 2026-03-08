"""DPLL-like backtracking search for E677 magmas.

Searches for a finite magma of size n satisfying E677 but violating E255.
Uses constraint propagation, immunity-based pruning, and pluggable heuristics.
"""

from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Callable

import numpy as np

from core.bijectivity import ContradictionError
from core.heuristics import CellValueHeuristic, MostConstrainedFirst
from core.logger import DecisionRecord, NullLogger, SearchLogger
from core.magma import PartialMagma
from core.propagator import E677Propagator
from verification.verify_255 import check_e255_element
from verification.verify_677 import verify_e677


@dataclass
class SearchResult:
    """Result of a search run."""

    found: bool
    models: list[np.ndarray]  # completed tables satisfying E677
    counterexamples: list[np.ndarray]  # models violating E255
    nodes_explored: int
    contradictions: int
    time_seconds: float


@dataclass
class SearchConfig:
    """Configuration for DPLL search."""

    n: int
    find_all_models: bool = False  # if True, enumerate all E677 models
    find_counterexample: bool = True  # if True, stop at first E255 violator
    max_nodes: int = 0  # 0 = unlimited
    max_time: float = 0.0  # 0 = unlimited (seconds)
    anti_e255_element: int = 0  # element that should violate E255
    apply_symmetry_breaking: bool = True
    log_decisions: bool = False


class DPLLSearch:
    """DPLL-style search for E677 models."""

    def __init__(
        self,
        config: SearchConfig,
        heuristic: CellValueHeuristic | None = None,
        logger: SearchLogger | None = None,
    ):
        self.config = config
        self.heuristic = heuristic or MostConstrainedFirst()
        self.logger = logger or NullLogger()
        self.n = config.n

        # Statistics
        self.nodes_explored = 0
        self.contradictions = 0
        self.step = 0
        self.start_time = 0.0

        # Results
        self.models: list[np.ndarray] = []
        self.counterexamples: list[np.ndarray] = []

    def search(self) -> SearchResult:
        """Run the search."""
        self.start_time = time.time()
        magma = PartialMagma(self.n)
        propagator = E677Propagator(magma)

        try:
            # Apply symmetry breaking
            if self.config.apply_symmetry_breaking and self.n >= 5:
                self._apply_symmetry_breaking(magma, propagator)

            # Run recursive search
            self._search_recursive(magma, propagator)

        except _SearchComplete:
            pass

        elapsed = time.time() - self.start_time
        return SearchResult(
            found=len(self.counterexamples) > 0,
            models=self.models,
            counterexamples=self.counterexamples,
            nodes_explored=self.nodes_explored,
            contradictions=self.contradictions,
            time_seconds=elapsed,
        )

    def _apply_symmetry_breaking(
        self, magma: PartialMagma, propagator: E677Propagator
    ) -> None:
        """Apply symmetry-breaking assumptions for anti-E255 search.

        From the Zulip discussion (Jihoon Hyun / Rudi Schneider):
        - Fix element 0 as the E255 violator
        - Set 0◇0 = 1 (non-idempotent at 0, WLOG)
        - E677 with x=0, y=0 gives: 0 = 0◇(0◇((0◇0)◇0)) = 0◇(0◇(1◇0))
        - This forces a chain of assignments
        """
        # 0◇0 = 1 (WLOG: 0 is not idempotent, first "new" element is 1)
        initial_assignments = [(0, 0, 1)]

        for a, b, c in initial_assignments:
            if a < self.n and b < self.n and c < self.n:
                magma.assign(a, b, c)
                propagator.propagate(a, b, c)

    def _search_recursive(
        self, magma: PartialMagma, propagator: E677Propagator
    ) -> None:
        """Recursive DPLL search."""
        self.nodes_explored += 1
        self._check_limits()

        # Complete table — verify
        if magma.is_complete():
            self._handle_complete(magma)
            return

        # Choose next cell and get ordered values
        choice = self.heuristic.choose_next(magma)
        if choice is None:
            # No valid assignment possible — dead end
            self.contradictions += 1
            return

        row, col, _ = choice
        values = self.heuristic.ordered_values(magma, row, col)

        for val in values:
            self.step += 1

            # Log decision point
            if self.config.log_decisions:
                record = DecisionRecord(
                    step=self.step,
                    n=self.n,
                    num_assigned=magma.num_assigned,
                    chosen_cell=(row, col),
                    chosen_value=val,
                    available_values=list(values),
                )
                self.logger.log_decision(record)

            # Try assignment
            assigned_cells: list[tuple[int, int, int]] = []
            try:
                magma.assign(row, col, val)
                assigned_cells.append((row, col, val))

                # Propagate
                forced = propagator.propagate(row, col, val)
                assigned_cells.extend(forced)

                # Recurse
                self._search_recursive(magma, propagator)

            except ContradictionError as e:
                self.contradictions += 1
                if self.config.log_decisions:
                    self.logger.log_contradiction(
                        self.step, self.n, str(e), magma.num_assigned
                    )

            finally:
                # Backtrack: undo all assignments in reverse order
                for a, b, _ in reversed(assigned_cells):
                    magma.unassign(a, b)

    def _handle_complete(self, magma: PartialMagma) -> None:
        """Handle a completed table."""
        table = magma.to_numpy()

        # Verify E677 (should always pass if propagation is correct)
        is_677, failures = verify_e677(table)
        if not is_677:
            # Propagation bug — log but don't count as model
            self.logger.log_contradiction(
                self.step, self.n,
                f"PROPAGATION BUG: E677 fails at {failures[:5]}",
                magma.num_assigned,
            )
            return

        self.models.append(table.copy())
        self.logger.log_model_found(self.step, self.n, table)

        # Check E255
        violates_e255 = False
        for x in range(self.n):
            if not check_e255_element(table, x):
                violates_e255 = True
                break

        if violates_e255:
            self.counterexamples.append(table.copy())
            if self.config.find_counterexample:
                raise _SearchComplete()

        if not self.config.find_all_models and not self.config.find_counterexample:
            raise _SearchComplete()

    def _check_limits(self) -> None:
        """Check if we've hit node or time limits."""
        if self.config.max_nodes > 0 and self.nodes_explored >= self.config.max_nodes:
            raise _SearchComplete()
        if self.config.max_time > 0:
            elapsed = time.time() - self.start_time
            if elapsed >= self.config.max_time:
                raise _SearchComplete()


class _SearchComplete(Exception):
    """Internal signal to stop search."""

    pass


def search_e677(
    n: int,
    max_time: float = 0.0,
    find_all: bool = False,
    log_path: str | None = None,
) -> SearchResult:
    """Convenience function to search for E677 models of size n.

    Args:
        n: Size of the magma.
        max_time: Maximum search time in seconds (0 = unlimited).
        find_all: If True, enumerate all models (not just first).
        log_path: Path to JSONL log file for ML training data.

    Returns:
        SearchResult with found models and statistics.
    """
    config = SearchConfig(
        n=n,
        find_all_models=find_all,
        find_counterexample=True,
        max_time=max_time,
        log_decisions=log_path is not None,
    )
    logger = SearchLogger(log_path) if log_path else NullLogger()
    with logger:
        searcher = DPLLSearch(config, logger=logger)
        return searcher.search()
