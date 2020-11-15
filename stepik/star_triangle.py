# An odd natural number n is given. Write a program that prints an isosceles star triangle with base n according to the example:
#
# *
# **
# ***
# ****
# ***
# **
# *
#
# Input data format
# One odd natural number is fed into the program.
#
# Output data format
# The program should output the triangle according to the condition.
#
# Note. Use a nested for loop.
from math import ceil
number = int(input())
height_triangle = ceil(number / 2)
a = '*'
for base in range(height_triangle):
    for side in range(base + 1):
        print(a, end='')
    print()
for base_2 in range(height_triangle - 1, 0, -1):
    for side_2 in range(base_2):
        print(a, end='')
    print()
