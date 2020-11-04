# Input data format
# The program receives two real numbers aa and bb, each on a separate line.
#
# Output data format
# The program should output 4 numbers - arithmetic mean, geometric, harmonic and quadratic.
from math import sqrt
a = float(input())
b = float(input())
arithmetic = (a + b) / 2
geometric = sqrt(a * b)
harmonic =(2 * a * b) / (a + b)
square = sqrt((a**2 + b**2) / 2)
print(arithmetic)
print(geometric)
print(harmonic)
print(square)
