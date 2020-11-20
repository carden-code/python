# A sequence of 4 integers is received for processing.
# It is known that the entered numbers do not exceed 10 ** 6 in absolute value.
# You need to write a program that displays the number of odd numbers in the original sequence and
# the maximum odd number on the screen. If there are no odd numbers, you need to display "NO" on the screen.
# The programmer was in a hurry and wrote the program incorrectly.
#
# Find all errors in this program (there may be one or several).
# Each error is known to affect only one line and can be corrected without changing other lines.
#
# Note. Please note that you need to find errors in the existing program, and not write your own,
# possibly using a different solution algorithm.
#
# n = 4
# count = 0
# maximum = 999
# for i in range(1, n + 1):
#     x = int(input())
#     if x % 2 != 0:
#         count += 1
#         if x > maximum:
#             maximum = i
#             break
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')
#
n = 4
count = 0
maximum = -10**6
for _ in range(1, n + 1):
    x = int(input())
    if x % 2 == 1:
        count += 1
        if x >= maximum:
            maximum = x

if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')
