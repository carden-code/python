# Write a program that determines the Euclidean distance between two points whose coordinates are given.
#
# Input data format
# The program is fed four real numbers, each on a separate line - x_1, y_1, x_2, y_2
#
# Output data format
# The program should output one number - the Euclidean distance.
from math import sqrt
x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
p = sqrt((x_1 - x_2)**2 + (y_1 - y_2)**2)
print(p)
