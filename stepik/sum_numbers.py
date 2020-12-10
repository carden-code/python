# The input to the program is a string of text containing natural numbers.
# Write a program that inserts a + sign between each number and then calculates the sum of the resulting numbers.
#
# Input data format
# The input to the program is a text string containing natural numbers separated by a space character.
#
# Output data format
# The program should text in accordance with the condition of the problem.
list_string = [c for c in input().split()]
amount = sum([int(i) for i in list_string])
print('+'.join(list_string) + '=' + str(amount))
