# A sequence of 7 integers is received for processing.
# It is known that the entered numbers do not exceed 10 ** 6 in absolute value.
# You need to write a program that calculates and displays the sum of all even numbers in the sequence,
# or 0 if there are no even numbers in the sequence. The programmer was in a hurry and wrote the program incorrectly.
#
# Find all the errors in this program (there are exactly 4 of them).
# Each error is known to affect only one line and can be fixed without changing other lines.
#
# s = 1
# for i in range(1, 7):
#     n = input()
#     if i % 2 == 0:
#         s = s + n
# print(s)
#
sum_even = 0
for _ in range(7):
    number = int(input())
    if number % 2 == 0:
        sum_even += number
print(sum_even)
