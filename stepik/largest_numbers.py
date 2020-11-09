# The input to the program is a natural number n, and then n different natural numbers, each on a separate line.
# Write a program that prints the largest and second largest numbers in a sequence.
#
# Input data format
# The input to the program is a natural number n >= 2, and then n different natural numbers, each on a separate line.
#
# Output data format
# The program should print the two largest numbers, each on a separate line.
n = int(input())
array = []

for i in range(n):
    num = int(input())
    array.append(num)

array.sort()
print(array[-1])
print(array[-2])
