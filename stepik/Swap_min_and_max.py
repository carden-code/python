# The input to the program is a line of text containing various natural numbers.
# A list of numbers is formed from this string.
# Write a program that swaps the minimum and maximum elements of this list.
#
# Input data format
# The input to the program is a line of text containing various natural numbers, separated by a space character.
#
# Output data format
# The program should output a line of text in accordance with the condition of the problem.
#
# Note. Use the appropriate built-in functions and list methods.
string = input()
string_list = string.split()
num_list = []

for i in string_list:
    num_list.append(int(i))

index_min, index_max = num_list.index(min(num_list)), num_list.index(max(num_list))
num_list[index_min], num_list[index_max] = num_list[index_max], num_list[index_min]

print(*num_list)
