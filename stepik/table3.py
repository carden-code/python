# A natural number n is given, (n <= 9).
# Write a program that prints the addition table for all numbers from 1 to n according to the example.
#
# Input data format
# One natural number is fed into the program.
#
# Output data format
# The program should print the addition table for all numbers from 1 to n.
#
# Note. There may be a space at the end of the line.
num = int(input())
for i in range(1, num + 1):
    for j in range(1, 10):
        print(i, '+', j, '=', i + j)
    print()
