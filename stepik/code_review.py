# A sequence of 10 integers is received for processing.
# It is known that the entered numbers do not exceed 10 ** 6 in absolute value.
# You need to write a program that prints the sum of all negative numbers in the sequence and
# the maximum negative number in the sequence.
# If there are no negative numbers, you need to display "NO".
# The programmer was in a hurry and wrote the program incorrectly.
#
# Find all the errors in this program (there are exactly 5 of them).
# Each error is known to affect only one line and can be fixed without changing other lines.
#
# Note 1. The number xx does not exceed 10 ** 6 in absolute value if -10 ** 6 <= x <= 10 ** 6.
#
# Note 2. If necessary, you can add the required lines of code.
#
# mx = 0
# s = 0
# for i in range(11):
#     x = int(input())
#     if x < 0:
#         s = x
#     if x > mx:
#         mx = x
# print(s)
# print(mx)
#
maximum_negative = -10**6
sum_negative = 0

for _ in range(10):
    number = int(input())
    if number < 0:
        sum_negative += number
    if 0 > number > maximum_negative:
        maximum_negative = number

if sum_negative == 0:
    print('NO')
else:
    print(sum_negative)
    print(maximum_negative)
