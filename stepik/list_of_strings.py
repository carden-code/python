# The input to the program is a natural number n, and then n lines.
# Write a program that creates a list from the specified strings and outputs it.
#
# Input data format
# The input to the program is a natural number nn, and then nn lines, each on a separate line.
#
# Output data format
# The program should display a list consisting of the specified strings.
num = int(input())
array = []
for i in range(num):
    array.append(input())
print(array)
