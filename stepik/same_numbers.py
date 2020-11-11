# A natural number is given. Write a program that determines if a specified number consists of the same digits.
#
# Input data format
# One natural number is fed into the program.
#
# Output data format
# The program should print "YES" if the number consists of the same digits and "NO" otherwise.
num = int(input())
last_num = num % 10
flag = True
while num != 0:
    if last_num != num % 10:
        flag = False
    num = num // 10
if flag:
    print('YES')
else:
    print('NO')
