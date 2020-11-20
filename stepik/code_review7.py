# A sequence of 8 integers is received for processing.
# It is known that the entered numbers do not exceed 10 ** 6 in absolute value.
# You need to write a program that displays the number of integers that are divisible by 4 in the original sequence
# and the maximum divisible by 4. If there are no integers divisible by 4, you need to display "NO" on the screen.
# The programmer was in a hurry and wrote the program incorrectly.
#
# Find all errors in this program (there may be one or several).
# Each error is known to affect only one line and can be corrected without changing other lines.
#
# Note. Please note that you need to find errors in the existing program, and not write your own,
# possibly using a different solution algorithm.
#
# n = 7
# count = 0
# maximum = 1000
# for i in range(1, n + 1):
#     x = int(input())
#     if x // 4 == 0:
#         count += 1
#         if x < maximum:
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')
#
n = 8
count = 0
maximum = -10**6
for i in range(1, n + 1):
    x = int(input())
    if x % 4 == 0:
        count += 1
        if x >= maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')
