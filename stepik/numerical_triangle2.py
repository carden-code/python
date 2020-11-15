# A natural number n is given. Write a program that prints a numerical triangle with height n, according to the example:
#
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21
# ...
#
# Input data format
# One natural number is fed into the program.
#
# Output data format
# The program should output the triangle according to the condition.
#
# Note. Use a nested for loop.
number = int(input())
total = 1
for i in range(1, number + 1):
    for j in range(i):
        print(total, end=' ')
        total += 1
    print()
