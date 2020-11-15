# A natural number n is given. Write a program that prints the numerical triangle according to the example:
#
# 1
# 22
# 333
# 4444
# 55555
# ...
# Input data format
# One natural number is fed into the program.
#
# Output data format
# The program should output the triangle according to the condition.
#
# Note. Use a nested for loop.
num = int(input())
for i in range(1, num + 1):
    for j in range(i):
        print(i, end='')
    print()
