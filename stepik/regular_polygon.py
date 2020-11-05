# Two numbers are given: a natural number nn and a real number aa.
# Write a program that finds the area of a specified regular polygon.
#
# Input data format
# The program receives two numbers nn and aa, each on a separate line.
#
# Output data format
# The program should output a real number - the area of the polygon.
from math import tan, pi
n = int(input())
a = float(input())
s = (n * a**2) / (4 * tan(pi / n))
print(s)
