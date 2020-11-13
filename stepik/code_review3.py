# A natural number is received for processing.
# You need to write a program that displays the maximum digit of a number that is a multiple of 3.
# If there are no numbers that are multiples of 3, you need to display "NO" on the screen.
# The programmer was in a hurry and wrote the program incorrectly.
#
# Find all the errors in this program (there are exactly 5 of them).
# Each error is known to affect only one line and can be fixed without changing other lines.
#
# Note 1. Number 0 is divisible by any natural number.
#
# Note 2. If necessary, you can add the required lines of code.
#
# n = int(input())
# max_digit = n % 10
# while n > 0:
#     digit = n % 10
#     if digit % 3 == 0:
#         if digit < max_digit:
#             digit = max_digit
#     n = n % 10
# if max_digit == 0:
#     print('NO')
# else:
#     print(max_digit)
#
number = int(input())
max_digit = -1
while number != 0:
    digit = number % 10
    if digit % 3 == 0:
        if digit >= max_digit:
            max_digit = digit
    number //= 10
if max_digit >= 0:
    print(max_digit)
else:
    print('NO')
