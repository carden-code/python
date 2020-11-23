# The input to the program is a natural number written in the decimal number system.
# Write a program that converts a given number to binary.
#
# Input data format
# One natural number is fed into the program.
#
# Output data format
# The program should output the number written in the binary number system.
n = int(input())
b = ''

while n > 0:
    b = str(n % 2) + b
    n = n // 2

print(b)
