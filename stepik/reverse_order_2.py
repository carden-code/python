# A natural number is given. Write a program that reverses the order of the digits of a number.
#
# Input data format
# One natural number is fed into the program.
#
# Output data format
# The program should print the number written in reverse order.
num = int(input())
while num != 0:
    last_num = num % 10
    print(last_num, end='')
    num = num // 10
