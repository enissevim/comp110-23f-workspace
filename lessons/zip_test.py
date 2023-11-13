"""Test my zip function."""
__author__ = "730577037"


from lessons.zip import zip


def test_empty_list() -> None:
    """Tests the zip function when there is empty inputs(should return an empty dictionary)."""
    assert zip([], []) == {}


def test_same_length() -> None:
    """Tests the zip function when there is two input lists with the same length(should return a dictionary with keys on one side and values on the other)."""
    assert zip(["a", "b", "c"], [1, 2, 3]) == {"a": 1, "b": 2, "c": 3}


def test_diff_length() -> None:
    """Tests the zip function when there is two input lists of different lenghts(should return an empty dictionary)."""
    assert zip(["d", "e"], [4, 5, 6]) == {}
