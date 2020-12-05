# The input to the program is a string of text containing integers.
# Write a program using a list expression that prints the cubes of the specified numbers also on one line.
#
# Input data format
# The input to the program is a string of text containing integers separated by a space character.
#
# Output data format
# The program should display the text in accordance with the condition of the problem.
#
# Note 1. Use a for loop to display the list items.
#
# Note 2. Use the split () method.
print(*[int(i) ** 3 for i in input().split()])
