# One line is fed to the program. Write a program that outputs:
#
# the total number of characters in the line;
# the original line repeated 3 times;
# the first character of the line;
# the first three characters of the string;
# the last three characters of the string;
# string in reverse order;
# a string with the first and last character removed.
# Input data format
# One line is fed to the program, the length of which is more than 3 characters.
#
# Output data format
# The program should output the data in accordance with the condition. Each value is displayed on a separate line.
string = input()
print(len(string))
print(string * 3)
print(string[0])
print(string[:3])
print(string[-3:])
print(string[::-1])
print(string[1:- 1])
