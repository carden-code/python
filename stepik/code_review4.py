# A natural number is received for processing.
# You need to write a program that displays its first (most significant) digit on the screen.
# The programmer was in a hurry and wrote the program incorrectly.
#
# Find all errors in this program (there are exactly 2 of them).
# Each error is known to affect only one line and can be fixed without changing other lines.
#
# n = int(input())
# while n > 0:
#     n %= 10
# print(n)
#
number = int(input())
while number > 9:
    number //= 10
print(number)
