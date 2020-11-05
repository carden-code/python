# You are given two integers m and n.
# Write a program that prints all numbers from mm to nn, inclusive, in ascending order if m < n,
# or in descending order otherwise.
#
# Input data format
# The program is given two integers mm and nn, each on a separate line.
#
# Output data format
# The program should display numbers in accordance with the condition of the problem.
m = int(input())
n = int(input())
if m <= n:
    for i in range(m, n + 1):
        print(i)
elif m >= n:
    for i in range(m, n - 1, -1):
        print(i)
