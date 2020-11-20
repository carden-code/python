# A natural number is received for processing.
# You need to write a program that displays the sum of the even digits of this number or 0 if there are no even digits
# in the record. The programmer was in a hurry and wrote the program incorrectly.
#
# Find all errors in this program (there may be one or several).
# Each error is known to affect only one line and can be corrected without changing other lines.
#
# Note. Please note that you need to find errors in the existing program, and not write your own,
# possibly using a different solution algorithm.
#
# n = input()
# s = 0
# while n > 10:
#     if n % 2 == 1:
#         s = n % 10
#     n //= 10
# print(s)
#
n = int(input())
s = 0
while n != 0:
    if (n % 10) % 2 == 0:
        s += n % 10
    n //= 10
print(s)
