# The input to the program is a line of text in which the letter "h" occurs at least twice.
# Write a program that removes the first and
# last occurrences of the letter "h" from this string, as well as any characters in between.
#
# Input data format
# The input to the program is a line of text.
#
# Output data format
# The program should display the text in accordance with the condition of the problem.
string = input()
elem = 'h'
print(string[:string.find(elem)] + string[string.rfind(elem) + 1:])
