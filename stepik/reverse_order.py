# A natural number is given. Write a program that displays its numbers in a column in reverse order.
#
# Input data format
# One natural number is fed into the program.
#
# Output data format
# The program should display the digits of the entered number in a column in the reverse order.
num = int(input())
while num != 0:
    last_num = num % 10
    print(last_num)
    num = num // 10
