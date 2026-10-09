#!/usr/bin/env python3
"""
Compute pi using the Chudnovsky algorithm with binary splitting.
Uses only the Python standard library.
"""

import sys
from decimal import Decimal, getcontext

# Python 3.11+ has a safety limit on converting very large ints to strings.
# Disable it so very large digit counts can be printed.
try:
    sys.set_int_max_str_digits(0)
except (AttributeError, ValueError):
    pass


# Chudnovsky constants
A = 13591409
B = 545140134
C3 = 640320 ** 3
C3_OVER_24 = C3 // 24


def binary_split(a: int, b: int):
    """
    Binary splitting helper.

    Returns integers P, Q, T such that the partial Chudnovsky sum
    over k = a ... b-1 is T / Q.
    """
    if b - a == 1:
        if a == 0:
            P = 1
            Q = 1
        else:
            P = (6 * a - 5) * (2 * a - 1) * (6 * a - 1)
            Q = (a ** 3) * C3_OVER_24

        T = P * (A + B * a)

        # Alternating sign
        if a & 1:
            T = -T

        return P, Q, T

    mid = (a + b) // 2

    P_left, Q_left, T_left = binary_split(a, mid)
    P_right, Q_right, T_right = binary_split(mid, b)

    P = P_left * P_right
    Q = Q_left * Q_right
    T = Q_right * T_left + P_left * T_right

    return P, Q, T


def chudnovsky_pi(digits: int) -> str:
    """
    Return pi as a string with `digits` digits after the decimal point.
    """
    if digits < 0:
        raise ValueError("digits must be non-negative")

    # Extra guard digits help ensure the final rounded result is correct.
    guard_digits = 50
    getcontext().prec = digits + guard_digits

    # Each Chudnovsky term gives about 14 decimal digits.
    terms = digits // 14 + 2

    _, Q, T = binary_split(0, terms)

    # pi = 426880 * sqrt(10005) * Q / T
    sqrt_10005 = Decimal(10005).sqrt()
    pi_value = (Decimal(Q) / Decimal(T)) * Decimal(426880) * sqrt_10005

    return format(pi_value, f".{digits}f")


if __name__ == "__main__":
    requested_digits = int(input())
    # int(sys.argv[1]) if len(sys.argv) > 1 else 100
    print(chudnovsky_pi(requested_digits))
