# Two natural numbers m and n are given (m <= n).
# Write a program that prints all numbers from mm to nn, inclusive, that satisfy at least one of the conditions:
#
# - the number is a multiple of 17;
# - the number ends in 9;
# - the number is a multiple of 3 and 5 at the same time.
#
# Input data format
# The program receives two natural numbers m and n (m <= n), each on a separate line.
#
# Output data format
# The program should display numbers in accordance with the condition of the problem.
#
# Note. If there are no numbers that satisfy the condition, nothing needs to be displayed.
m = int(input())
n = int(input())
for i in range(m, n + 1):
    if i % 17 == 0 or i % 10 == 9 or (i % 3 == 0 and i % 5 == 0):
        print(i)
