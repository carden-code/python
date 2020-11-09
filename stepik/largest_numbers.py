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
maxim = 0
maxim_2 = 0

for i in range(n):
    num = int(input())
    array.append(num)

maxim = max(array)
array.remove(maxim)
maxim_2 = max(array)
print(maxim)
print(maxim_2)
