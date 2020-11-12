# A natural number is given. Write a program that determines whether the sequence of its digits,
# when viewed from right to left, is non-decreasing.
#
# Input data format
# One natural number is fed into the program.
#
# Output data format
# The program should print "YES" if the sequence of its digits when viewed from right to left is sorted
# in non-decreasing order, and "NO" otherwise.
num = int(input())
first_digit = int(str(abs(num))[0])
last2_digit = num % 100 // 10
last_digit = num % 10
flag = True

while num != first_digit:
    last2_digit = num % 100 // 10
    last_digit = num % 10
    if last_digit > last2_digit:
        flag = False
    num = num // 10

if flag:
    print('YES')
else:
    print('NO')



