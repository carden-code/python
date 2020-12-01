# The input to the program is a natural number n, n> = 2, and then n integers.
# Write a program that creates a list from the specified numbers,
# consisting of the sums of adjacent numbers (0 and 1, 1 and 2, 2 and 3, etc.).
#
# Input data format
# The input to the program is a natural number nn, and then nn integers, each on a separate line.
#
# Output data format
# The program should output a list of the sums of adjacent numbers.
num = int(input())
list_sum = []
a = int(input())
for i in range(num - 1):
    b = int(input())
    list_sum.append(a + b)
    a = b
print(list_sum)