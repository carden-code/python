# The input to the program is a natural number n.
# Write a program that calculates the sum of those numbers from 1 to n (inclusive) whose square ends in 2, 5, or 8.
#
# Input data format
# The input to the program is a natural number nn.
#
# Output data format
# The program should output a single number in accordance with the condition of the problem.
#
# Note. If there are no such numbers in the specified range, then output 0.
n = int(input())
total = 0
for i in range(1, n + 1):
    if i**2 % 10 == 2 or i**2 % 10 == 5 or i**2 % 10 == 8:
        total += i
print(total)
