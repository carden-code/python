# Given three real numbers aa, bb, cc. Write a program that finds the real roots of a quadratic equation.
# Input data format
# The program receives three real numbers a! = 0, b, c, each on a separate line.
#
# Output data format
# The program should print the real roots of the equation if they exist, or the text "No roots" otherwise.
#
# Note. If the equation has two roots, then you should output them in ascending order.
from math import sqrt

a = float(input("'A' is not equal to zero: a = "))
b = float(input('b = '))
c = float(input('c = '))

d = b**2 - 4 * a * c
if d == 0:
    x = (-b + sqrt(d)) / (2 * a)
    print(x)
elif d > 0:
    x_1 = (-b + sqrt(d)) / (2 * a)
    x_2 = (-b - sqrt(d)) / (2 * a)
    if x_1 > x_2:
        print(x_2)
        print(x_1)
    else:
        print(x_1)
        print(x_2)
else:
    print('No roots')
