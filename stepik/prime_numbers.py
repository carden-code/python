# The input to the program is two natural numbers a and b (a < b).
# Write a program that finds all prime numbers from a to b, inclusive.
#
# Input data format
# The program receives two numbers as input, each on a separate line.
#
# Output data format
# The program should print all prime numbers from a to b inclusive, each on a separate line.
a = int(input())
b = int(input())
total = 0
for i in range(a, b + 1):
    for j in range(1, b + 1):
        if i % j == 0:
            total += 1
    if total < 3 and i > 1:
        print(i)
        total = 0
    else:
        total = 0
