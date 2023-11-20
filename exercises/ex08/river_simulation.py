"""File to run river simulations."""
from exercises.ex08.river import River
__author__ = "730577037"


my_river: River = River(10, 2)
my_river.one_river_week()
print(my_river.one_river_day())