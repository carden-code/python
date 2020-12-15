# Write a function get_circle (radius) that takes the radius of a circle as an argument and returns two values:
# the circumference of the circle and the area of the circle bounded by the given circle.
from math import pi


def get_circle(radius):
    return 2 * pi * radius, pi * radius**2


r = float(input())
length, square = get_circle(r)
print(length, square)
