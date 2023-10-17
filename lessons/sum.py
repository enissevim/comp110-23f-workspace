"""Summing the elements of a list using different loops."""
__author__ = "730577037"


def w_sum(vals: list[float]) -> float:
    """Calculate the sum of a list."""
    idx: int = 0
    sum: float = 0.0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Calculate the sum of a list."""
    idx: int = 0
    sum: float = 0.0
    for elem in vals:
        sum += vals[idx]
        idx += 1
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Calculate the sum of a list."""
    idx: int = 0
    sum: float = 0.0
    for elem in range(0, len(vals)):
        sum += vals[idx]
        idx += 1
    return sum