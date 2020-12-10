# The input to the program is a line of text.
# Write a program using a list expression that finds the length of the longest word.
#
# Input data format
# The input to the program is a line of text.
#
# Output data format
# The program should display the text in accordance with the condition of the problem.
print(max([len(i) for i in input().split()]))
