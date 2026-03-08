"""Tests for verification modules."""

import numpy as np
import pytest

from core.known_models import model_5, model_7a, model_7b, model_11a, model_11b
from verification.verify_255 import check_e255_element, check_fixer_exists, verify_e255
from verification.verify_677 import verify_e677, verify_e677_single
from verification.check_properties import (
    is_left_cancellative,
    is_right_cancellative,
    is_idempotent,
    idempotent_elements,
    is_commutative,
)


class TestVerifyE677:
    def test_model_5(self):
        table = model_5()
        ok, failures = verify_e677(table)
        assert ok, f"E677 fails at {failures}"

    def test_model_7a(self):
        table = model_7a()
        ok, failures = verify_e677(table)
        assert ok, f"E677 fails at {failures}"

    def test_model_7b(self):
        table = model_7b()
        ok, failures = verify_e677(table)
        assert ok, f"E677 fails at {failures}"

    def test_model_11a(self):
        table = model_11a()
        ok, failures = verify_e677(table)
        assert ok, f"E677 fails at {failures}"

    def test_model_11b(self):
        table = model_11b()
        ok, failures = verify_e677(table)
        assert ok, f"E677 fails at {failures}"

    def test_trivial_model(self):
        # Size 1 trivially satisfies E677
        table = np.array([[0]], dtype=np.int16)
        ok, failures = verify_e677(table)
        assert ok

    def test_random_fails(self):
        # A random 5x5 table should almost certainly fail E677
        np.random.seed(42)
        table = np.random.randint(0, 5, size=(5, 5), dtype=np.int16)
        ok, failures = verify_e677(table)
        assert not ok

    def test_single_pair(self):
        table = model_5()
        assert verify_e677_single(table, 0, 0)
        assert verify_e677_single(table, 2, 3)


class TestVerifyE255:
    def test_model_5_satisfies(self):
        table = model_5()
        ok, violators = verify_e255(table)
        assert ok, f"E255 violated at elements {violators}"

    def test_model_7a_satisfies(self):
        table = model_7a()
        ok, violators = verify_e255(table)
        assert ok, f"E255 violated at elements {violators}"

    def test_model_11a_satisfies(self):
        table = model_11a()
        ok, violators = verify_e255(table)
        assert ok, f"E255 violated at elements {violators}"

    def test_trivial(self):
        table = np.array([[0]], dtype=np.int16)
        ok, _ = verify_e255(table)
        assert ok

    def test_fixer_exists_for_known_models(self):
        table = model_5()
        for x in range(5):
            fixer = check_fixer_exists(table, x)
            assert fixer is not None, f"No fixer for element {x}"


class TestProperties:
    def test_left_cancellative(self):
        assert is_left_cancellative(model_5())
        assert is_left_cancellative(model_7a())

    def test_right_cancellative(self):
        assert is_right_cancellative(model_5())
        assert is_right_cancellative(model_7a())

    def test_model_5_idempotent(self):
        # x◇y = 2x + 4y mod 5 → x◇x = 6x mod 5 = x. So model_5 IS idempotent.
        table = model_5()
        assert is_idempotent(table)

    def test_model_7a_not_idempotent(self):
        # x◇y = 4x + y mod 7 → x◇x = 5x mod 7. 5x = x iff 4x=0 mod 7 iff x=0.
        table = model_7a()
        assert not is_idempotent(table)

    def test_idempotent_elements(self):
        table = model_5()
        idem = idempotent_elements(table)
        assert len(idem) == 5  # all idempotent

    def test_commutative(self):
        table = model_5()
        # 2x + 4y vs 2y + 4x — these are different, so not commutative
        # unless 2x+4y = 2y+4x => 2(x-y) = 4(x-y) => -2(x-y)=0 mod 5
        # => 3(x-y)=0 mod 5. Not always true, so not commutative.
        assert not is_commutative(table)
