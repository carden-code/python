# The input to the program is a line of text.
# Write a program that translates each of its characters into their corresponding code
# from the Unicode character table.
#
# Input data format
# The input to the program is a line of text.
#
# Output data format
# The program should output the code values of the string characters separated by one space character.
string = input()
for c in string:
    print(ord(c), end=' ')
