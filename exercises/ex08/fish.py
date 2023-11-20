"""File to define Fish class."""
__author__ = "730577037"


class Fish:
    """Create Fish Class and attributes."""
    age: int = 0

    def __init__(self):
        """Init for Fish Class."""
        self.age = 0
        return None
    
    def one_day(self):
        """One day passes."""
        self.age += 1
        return None