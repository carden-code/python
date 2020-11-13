# A natural number is received for processing.
# You need to write a program that displays the product of the digits of the entered number.
# The programmer was in a hurry and wrote the program incorrectly.
#
# Find all errors in this program (there are exactly 3 of them).
# Each error is known to affect only one line and can be fixed without changing other lines.
#
# n = input()
# product = n % 10
# while n >= 10:
#     digit = n % 10
#     product = product * digit
#     n //= 10
# print(product)
#
number = int(input())
product = 1
while number != 0:
    digit = number % 10
    product *= digit
    number //= 10
print(product)
