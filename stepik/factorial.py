# The input to the program is a natural number n. Write a program that computes n !.
#
# Input data
# The input to the program is a natural number n, (n <= 12).
#
# Output
# The program should output a single number in accordance with the condition of the problem.
#
# Note. The factorial of a natural number nn is the product of all natural numbers from 1 to n, that is
# n! = 1 * 2 * 3 ... * n
n = int(input())
total = 1
for i in range(2, n + 1):
    total *= i
print(total)
