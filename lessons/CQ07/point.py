"""CQ07 - Intro To Object Oriented Programming."""
from __future__ import annotations
__author__ = "730577037"


class Point:
    """Class that represents a point on a coordinate grid."""
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """Constructor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Method that belongs to the Point class and mutates a Point."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Method that belongs to the Point class and instead of mutating a Point, it creates a new Point."""
        x = self.x * factor
        y = self.y * factor
        return Point(x, y)

    def __str__(self) -> str:
        """Magic method to print out points in a readable way."""
        return f"x: {self.x}; y: {self.y}"
    
    def __mul__(self, factor: int | float) -> Point:
        """Magic method to overload the multiplication operator."""
        x = self.x * factor
        y = self.y * factor
        return Point(x, y)

    def __add__(self, factor: int | float) -> Point:
        """Magic method to overload the addition operator."""
        x = self.x + factor
        y = self.y + factor
        return Point(x, y)