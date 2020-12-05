# The input to the program is a line of text.
# Write a program that uses a list expression that prints all the numeric characters in a given string.
#
# Input data format
# The input to the program is a line of text.
#
# Output data format
# The program should display the text in accordance with the condition of the problem.
#
# Note. The program can be written in one line of code.
print(*[i for i in input() if i.isdigit()], sep='')
