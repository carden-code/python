# The input to the program is a natural number n, and then n integers, each on a separate line.
# Write a program that calculates the sum of the numbers entered.
#
# Input data format
# The input to the program is a natural number n, and then n integers, each on a separate line.
#
# Output data format
# The program should output the sum of the given numbers.
num = int(input())
total = 0
for i in range(num):
    total += int(input())
print(total)
