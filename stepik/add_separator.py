# The input to the program is a text string and a separator string.
# Write a program that inserts the specified separator between each character of the entered line of text.
#
# Input data format
# The input to the program is a line of text and a line separator, each on a separate line
#
# Output data format
# The program should display the text in accordance with the condition of the problem.
#
# print(*input(), sep=input())
string = input()
separator = input()
list_str = []
for c in string:
    list_str.append(c)
print(separator.join(list_str))
