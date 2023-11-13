"""CQ07 - Intro To Object Oriented Programming Test."""
__author__ = "730577037"


from lessons.CQ07.point import Point

my_point: Point = Point(7.0, 6.0)

print("Your initial points are:")
print(my_point.x) + print(my_point.y)

my_point.scale_by(3)
print("Your scaled points are:")
print(my_point.x) + print(my_point.y)