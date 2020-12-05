# The input to the program is a line of text containing words.
# Write a program that displays the words of the entered line in a column.
#
# Input data format
# The input to the program is a line of text containing words separated by a space character.
#
# Output data format
# The program should display the text in accordance with the condition of the problem.
#
# Note. The program can be written in one line of code.
print(*[i for i in input().split()], sep='\n')