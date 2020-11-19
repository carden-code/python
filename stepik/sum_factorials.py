# A natural number nn is given. Write a program that prints the sum value 1! + 2! + 3! +… + n!.
#
# Input data format
# One natural number is fed into the program.
#
# Output data format
# The program should output the value of the sum 1! + 2! + 3! + ... + n!.
#
# Note 1. The factorial of a natural number nn is the product of all natural numbers from 1 to n, that is
# n! = 1 * 2 * 3 * ... * n.
#
# Sample Input:
# 3
# Sample Output:
# 9
n = int(input())
factorial = 1
sum_f = 0
for i in range(1, n + 1):
    factorial *= i
    sum_f += factorial
print(sum_f)
