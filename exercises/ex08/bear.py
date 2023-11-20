"""File to define Bear class."""
__author__ = "730577037"


class Bear:
    """Create Bear Class and attributes."""
    age: int = 0
    hunger_score: int = 0

    def __init__(self):
        """Init for Bear Class."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """One day passes."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """When a bear eats a fish."""
        self.hunger_score += num_fish