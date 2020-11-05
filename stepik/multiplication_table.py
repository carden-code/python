# A natural number n is given. Write a program that prints the multiplication table by n.
#
# Input data format
# A natural number is fed into the program.
#
# Output data format
# The program should display the multiplication table by the entered number.
num = int(input())
for i in range(10):
    print(num, 'x', i + 1, '=', num * (i + 1))
