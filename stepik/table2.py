# A natural number n is given, (n <= 9).
# Write a program that prints an n × 5 table where the i-th line contains the number i
# (the numbers are separated by one space).
#
# Input data format
# One natural number is fed into the program.
#
# Output data format
# The program should output an n × 5 table according to the condition.
#
# Note. There may be a space at the end of the line.
num = int(input())
for i in range(1, num + 1):
    for j in range(5):
        print(i, end=' ')
    print()
