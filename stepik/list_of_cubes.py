# The input to the program is a natural number n, and then n integers.
# Write a program that creates a list of cubes from given numbers.
#
# Input data format
# The input to the program is a natural number nn, and then nn integers, each on a separate line.
#
# Output data format
# The program should output a list of cubes of the specified numbers.
num = int(input())
list_cubes = []
for i in range(num):
    list_cubes.append(int(input())**3)
print(list_cubes)
