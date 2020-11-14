# A natural number n is given, (n <= 9).
# Write a program that prints an n × 3 table consisting of a given number (the numbers are separated by one space).
#
# Input data format
# One natural number is fed into the program.
#
# Output data format
# The program should print an n × 3 table consisting of the given number.
#
# Note. There may be a space at the end of the line.
num = int(input())
for i in range(num):
    for j in range(3):
        print(num, end=' ')
    print()


