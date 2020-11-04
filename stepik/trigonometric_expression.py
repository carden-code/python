# Input data format
# The input to the program is one real number xx measured in degrees.
#
# Output data format
# The program should output one number - the value of the trigonometric expression.
from math import radians, sin, cos, tan
x = radians(float(input()))
prod = sin(x) + cos(x) + tan(x)**2
print(prod)
