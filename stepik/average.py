# Three different integers are given. Write a program that finds the average number.
#
# Input data format
# The program receives three different integers as input, each on a separate line.
#
# Output data format
# The program should print the average.
a = int(input('Please enter the first number:'))
b = int(input('Please enter the second number:'))
c = int(input('Please enter the third number:'))
if a > b and a > c:
    if b > c:
        print(b)
    else:
        print(c)
elif b > a and b > c:
    if a > c:
        print(a)
    else:
        print(c)
elif c > a and c > b:
    if b > a:
        print(b)
    else:
        print(a)
