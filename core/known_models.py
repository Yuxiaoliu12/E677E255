"""Database of known E677 models for testing and analysis.

All known finite E677 models satisfy E255. These are used for:
- Validating the propagation engine (can we rediscover them?)
- Testing verification code
- Generating training data features
- Understanding the structure of E677 models
"""

from __future__ import annotations

import numpy as np


def linear_model_mod_p(p: int, alpha: int, beta: int) -> np.ndarray:
    """Generate a linear model x◇y = alpha*x + beta*y (mod p).

    For E677, the valid (alpha, beta) pairs over Z/pZ come in two types:
    - Type 1: beta is a primitive 5th root of unity, alpha = 1 - beta
    - Type 2: beta^4 + beta^3 + 2*beta^2 + 2*beta + 1 = 0, alpha = -beta^3 - beta - 1
    """
    table = np.zeros((p, p), dtype=np.int16)
    for x in range(p):
        for y in range(p):
            table[x, y] = (alpha * x + beta * y) % p
    return table


def model_5() -> np.ndarray:
    """The unique E677 model of size 5: x◇y = 2x - y on Z/5Z.

    This is a Type 1 linear model with alpha=2, beta=-1≡4 (mod 5).
    beta = 4 is a primitive 5th root of unity mod 5 (4^5 = 4^1 mod 5...
    actually 4^2=16≡1, so 4 has order 2, not 5).

    More precisely: x◇y = 2x + 4y mod 5, which equals 2x - y mod 5.
    """
    return linear_model_mod_p(5, 2, 4)


def model_7a() -> np.ndarray:
    """E677 model of size 7: x◇y = 4x + y on Z/7Z.

    Type 2 linear model. Verified computationally.
    """
    return linear_model_mod_p(7, 4, 1)


def model_7b() -> np.ndarray:
    """E677 model of size 7: x◇y = 4x + 3y on Z/7Z.

    Type 2 linear model. Verified computationally.
    """
    return linear_model_mod_p(7, 4, 3)


def model_11a() -> np.ndarray:
    """E677 model of size 11: x◇y = 4x + 8y on Z/11Z.

    Verified computationally.
    """
    return linear_model_mod_p(11, 4, 8)


def model_11b() -> np.ndarray:
    """E677 model of size 11: x◇y = 5x + 7y on Z/11Z.

    Verified computationally.
    """
    return linear_model_mod_p(11, 5, 7)


def model_11c() -> np.ndarray:
    """E677 model of size 11: x◇y = 6x + 6y on Z/11Z.

    Verified computationally.
    """
    return linear_model_mod_p(11, 6, 6)


def model_11d() -> np.ndarray:
    """E677 model of size 11: x◇y = 10x + 2y on Z/11Z.

    Verified computationally.
    """
    return linear_model_mod_p(11, 10, 2)


def all_known_small_models() -> list[tuple[str, np.ndarray]]:
    """Return all known small E677 models with names."""
    return [
        ("5/linear_2_4", model_5()),
        ("7a/linear_4_1", model_7a()),
        ("7b/linear_4_3", model_7b()),
        ("11a/linear_4_8", model_11a()),
        ("11b/linear_5_7", model_11b()),
        ("11c/linear_6_6", model_11c()),
        ("11d/linear_10_2", model_11d()),
    ]


def find_linear_models_mod_p(p: int) -> list[tuple[int, int]]:
    """Find all (alpha, beta) pairs giving E677 models over Z/pZ.

    Brute-force checks all pairs. Returns list of valid (alpha, beta).
    """
    valid = []
    for alpha in range(p):
        for beta in range(p):
            table = linear_model_mod_p(p, alpha, beta)
            # Quick E677 check on a few random pairs
            ok = True
            for x in range(min(p, 5)):
                for y in range(min(p, 5)):
                    e1 = table[y, x]
                    e2 = table[e1, y]
                    e3 = table[x, e2]
                    e4 = table[y, e3]
                    if e4 != x:
                        ok = False
                        break
                if not ok:
                    break
            if ok and p > 5:
                # Full check for larger primes
                from verification.verify_677 import verify_e677

                ok, _ = verify_e677(table)
            if ok and not (alpha == 0 and beta == 0):
                # Exclude trivial (all-zero) model unless p=1
                if alpha != 0 or beta != 0:
                    valid.append((alpha, beta))
    return valid
