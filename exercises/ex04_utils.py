"""EX04 - `list` Utility Functions."""
__author__ = "730577037"


def all(int_list: list[int], num: int) -> bool:
    """Checks to see if the numbers in the list match the indicated number and returns True or False."""
    idx: int = 0

    if len(int_list) == 0:
        return False
    else:
        while idx < len(int_list):
            if num == int_list[idx]:
                idx += 1
            else:
                return False
        return True
    

def max(input: list[int]) -> int:
    """Returns the maximum value from a given list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    maximum: int = input[0]
    
    while i < len(input):
        if input[i] > maximum:
            maximum = input[i]
        i += 1
    return maximum


def is_equal(first_list: list[int], second_list: list[int]) -> bool:
    """Checks to see if the two lists are equivalent to one another."""
    idx: int = 0
    if len(first_list) != len(second_list):
        return False
    while idx < len(first_list) and idx < len(second_list):
        if first_list[idx] == second_list[idx]:
            idx += 1
        else:
            return False
    return True