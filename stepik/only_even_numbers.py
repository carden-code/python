# Write a program that reads a sequence of 10 integers and determines whether each of them is even or not.
#
# Input data format
# The program receives 10 integers as input, each on a separate line.
#
# Output data format
# The program should print the string "YES" if all numbers are even and "NO" otherwise.
even = 0
odd = 0
for _ in range(10):
    num = int(input())
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
if odd > 0:
    print('NO')
else:
    print('YES')
