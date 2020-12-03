# The input to the program is a line of text. Write a program that displays the words of the entered line in a column.
#
# Input data format
# The input to the program is a line of text.
#
# Output data format
# The program should display the text in accordance with the condition of the problem.
string = input()
print(*string.split(), sep='\n')
