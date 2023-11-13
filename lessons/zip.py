"""Combining two lists into a dictionary."""
__author__ = "730577037"


def zip(keys: list[str], values: list[int]) -> dict[str, int]:
    """Using two input lists, create a dictionary that corresponds to one another."""
    if len(keys) != len(values) or len(keys) == 0:
        return {}

    result = {}
    for idx in range(len(keys)):
        result[keys[idx]] = values[idx]
    return result