# The input to the program is a natural number n. Write a program that calculates the sum of all its divisors.
#
# Input data
# The input to the program is a natural number n.
#
# Output
# The program should output a single number in accordance with the condition of the problem.
n = int(input())
total = 0
for i in range(1, n + 1):
    if n % i == 0:
        total += i
print(total)
