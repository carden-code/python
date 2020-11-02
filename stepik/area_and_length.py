# Write a program that determines the area of a circle and the circumference of a circle for a given radius R.
#
# Input data format
# The input to the program is one real number R.
#
# Output data format
# The program should output two numbers - the area of a circle and the circumference of a circle of radius R.
from math import pi
r = float(input())
s = pi * r**2
c = 2 * pi * r
print(s)
print(c)
