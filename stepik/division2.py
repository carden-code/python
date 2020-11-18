# The input to the program is a natural number n.
# Write a program that displays a graphical representation of the divisibility of numbers from 1 to n, inclusive.
# In each line it is necessary to print the next number and as many “+” symbols as there are divisors for this number.
#
# Input data format
# One natural number is fed into the program.
#
# Output data format
# The program should display a graphical representation of numbers from 1 to n, each on a separate line.
#
# Sample Input:
#
# 5
# Sample Output:
#
# 1+
# 2++
# 3++
# 4+++
# 5++
n = int(input())
count = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i % j == 0:
            count += 1
    print(i, '+' * count, sep='')
    count = 0
