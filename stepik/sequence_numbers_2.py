# Two integers m and n are given (m> n).
# Write a program that prints all odd numbers from mm to nn, inclusive, in descending order.
#
# Input data format
# The program is given two integers mm and nn, each on a separate line.
#
# Output data format
# The program should display numbers in accordance with the condition of the problem.
m = int(input())
n = int(input())

if m % 2 == 0:
    m -= 1

for i in range(m, n - 1, -2):
    print(i)
