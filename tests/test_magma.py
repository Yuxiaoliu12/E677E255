"""Tests for core/magma.py — PartialMagma."""

import pytest
import numpy as np

from core.bijectivity import ContradictionError
from core.magma import PartialMagma, UNSET


class TestPartialMagma:
    def test_init(self):
        m = PartialMagma(5)
        assert m.n == 5
        assert m.num_assigned == 0
        assert not m.is_complete()
        assert m.fill_ratio() == 0.0

    def test_assign_and_get(self):
        m = PartialMagma(5)
        m.assign(0, 1, 3)
        assert m.get(0, 1) == 3
        assert m.is_assigned(0, 1)
        assert m.num_assigned == 1

    def test_assign_duplicate_ok(self):
        m = PartialMagma(5)
        m.assign(0, 1, 3)
        m.assign(0, 1, 3)  # same value — no error
        assert m.num_assigned == 1

    def test_assign_conflict(self):
        m = PartialMagma(5)
        m.assign(0, 1, 3)
        with pytest.raises(ContradictionError):
            m.assign(0, 1, 4)

    def test_left_bijectivity_conflict(self):
        m = PartialMagma(5)
        m.assign(0, 1, 3)
        with pytest.raises(ContradictionError):
            m.assign(0, 2, 3)  # row 0 already maps something to 3

    def test_unassign(self):
        m = PartialMagma(5)
        m.assign(0, 1, 3)
        m.unassign(0, 1)
        assert m.get(0, 1) is None
        assert m.num_assigned == 0
        assert 3 in m.available_values(0, 1)

    def test_available_values(self):
        m = PartialMagma(3)
        assert m.available_values(0, 0) == {0, 1, 2}
        m.assign(0, 0, 1)
        assert m.available_values(0, 1) == {0, 2}  # 1 already used in row 0
        m.assign(0, 1, 0)
        assert m.available_values(0, 2) == {2}  # only 2 left

    def test_left_inverse(self):
        m = PartialMagma(5)
        m.assign(2, 3, 4)  # 2◇3 = 4, so L_2(3) = 4, L_2⁻¹(4) = 3
        assert m.left_inverse(2, 4) == 3
        assert m.left_inverse(2, 0) is None

    def test_right_image_tracking(self):
        m = PartialMagma(5)
        m.assign(0, 2, 3)  # 0◇2 = 3
        m.assign(1, 2, 3)  # 1◇2 = 3 — right-cancel failure!
        assert m.right_cancel_failure_count() >= 1

    def test_copy(self):
        m = PartialMagma(5)
        m.assign(0, 1, 3)
        m2 = m.copy()
        m2.assign(0, 2, 4)
        assert m.get(0, 2) is None  # original unchanged
        assert m2.get(0, 2) == 4

    def test_snapshot(self):
        m = PartialMagma(3)
        m.assign(0, 0, 1)
        snap = m.snapshot()
        assert snap["n"] == 3
        assert snap["num_assigned"] == 1
        assert snap["table"][0][0] == 1

    def test_complete(self):
        m = PartialMagma(2)
        m.assign(0, 0, 1)
        m.assign(0, 1, 0)
        m.assign(1, 0, 0)
        m.assign(1, 1, 1)
        assert m.is_complete()
        assert m.fill_ratio() == 1.0
