# Write a program that reads a natural number n and outputs the first n numbers of the Fibonacci sequence.
#
# Input data format
# The input to the program is one number n, (n <= 100) - the number of members of the sequence.
#
# Output data format
# The program should output the members of the Fibonacci sequence, separated by a space character.
f1 = 1
f2 = 1
f3 = 0
num = int(input())
if num == 1:
    print(1)
else:
    print(f1, f2, end=' ')

for i in range(1, num - 1):
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    print(f3, end=' ')
