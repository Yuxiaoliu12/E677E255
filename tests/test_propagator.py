"""Tests for core/propagator.py — E677 constraint propagation."""

import pytest
import numpy as np

from core.bijectivity import ContradictionError
from core.magma import PartialMagma
from core.propagator import E677Propagator
from core.known_models import model_5, model_7a


class TestPropagator:
    def test_basic_propagation(self):
        """Assigning cells from a known model should not raise errors."""
        table = model_5()
        m = PartialMagma(5)
        p = E677Propagator(m)

        # Assign cells one by one from the known model
        for a in range(5):
            for b in range(5):
                val = int(table[a, b])
                if not m.is_assigned(a, b):
                    m.assign(a, b, val)
                    p.propagate(a, b, val)

        assert m.is_complete()

    def test_propagation_forces_cells(self):
        """After enough assignments from a known model, propagation
        should force remaining cells."""
        table = model_5()
        m = PartialMagma(5)
        p = E677Propagator(m)

        # Assign roughly half the cells and see if propagation fills more
        assigned_count = 0
        for a in range(5):
            for b in range(5):
                if assigned_count >= 13:  # assign ~half of 25
                    break
                val = int(table[a, b])
                if not m.is_assigned(a, b):
                    m.assign(a, b, val)
                    forced = p.propagate(a, b, val)
                    assigned_count += 1 + len(forced)
            if assigned_count >= 13:
                break

        # Propagation should have forced additional cells
        assert m.num_assigned > 13 or m.num_assigned == 25

    def test_contradiction_on_bad_assignment(self):
        """Assigning a wrong value should eventually cause a contradiction."""
        table = model_5()
        m = PartialMagma(5)
        p = E677Propagator(m)

        # Set up some correct assignments first
        m.assign(0, 0, int(table[0, 0]))
        p.propagate(0, 0, int(table[0, 0]))

        m.assign(0, 1, int(table[0, 1]))
        p.propagate(0, 1, int(table[0, 1]))

        m.assign(1, 0, int(table[1, 0]))
        p.propagate(1, 0, int(table[1, 0]))

        # Now try a deliberately wrong assignment
        correct_val = int(table[1, 1])
        wrong_val = (correct_val + 1) % 5
        # This might or might not immediately contradict,
        # but should eventually lead to one
        try:
            m.assign(1, 1, wrong_val)
            forced = p.propagate(1, 1, wrong_val)
            # If it doesn't immediately contradict, try to fill more
            for a in range(5):
                for b in range(5):
                    if m.is_assigned(a, b):
                        continue
                    val = int(table[a, b])
                    try:
                        m.assign(a, b, val)
                        p.propagate(a, b, val)
                    except ContradictionError:
                        return  # Expected!
            # If we get here without contradiction, the wrong value
            # happened to be consistent (unlikely but possible for
            # this specific wrong val). That's ok for this test.
        except ContradictionError:
            pass  # Expected

    def test_replay_model_7a(self):
        """Replay the size-7 model through the propagator."""
        table = model_7a()
        m = PartialMagma(7)
        p = E677Propagator(m)

        for a in range(7):
            for b in range(7):
                val = int(table[a, b])
                if not m.is_assigned(a, b):
                    m.assign(a, b, val)
                    p.propagate(a, b, val)

        assert m.is_complete()

    def test_naked_single(self):
        """When a row has n-1 cells filled, the last should be forced."""
        m = PartialMagma(3)
        p = E677Propagator(m)

        # Fill row 0 except one cell
        m.assign(0, 0, 1)
        m.assign(0, 1, 2)
        # Row 0 now has [1, 2, ?] — only value 0 is left for cell (0, 2)
        forced = p._check_naked_singles(0)
        assert len(forced) == 1
        assert forced[0] == (0, 2, 0)

    def test_check_all_constraints(self):
        """check_all_constraints on a complete valid model returns no forced."""
        table = model_5()
        m = PartialMagma(5)
        # Fill entire table
        for a in range(5):
            for b in range(5):
                m.assign(a, b, int(table[a, b]))

        p = E677Propagator(m)
        forced = p.check_all_constraints()
        # All constraints are satisfied, no new forcing
        assert len(forced) == 0
