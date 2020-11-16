# A natural number n is given. Write a program that prints a numerical triangle with height n, according to the example:
#
# 1
# 121
# 12321
# 1234321
# 123454321
# ...
# Input data format
# One natural number is fed into the program.
#
# Output data format
# The program should output the triangle according to the condition.
#
# Note. Use a nested for loop.
number = int(input())
for i in range(1, number + 1):
    for j in range(1, i + 1):
        print(j, end='')
    for k in range(i - 1, 0, -1):
        print(k, end='')
    print()
