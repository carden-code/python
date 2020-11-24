# One line is fed to the program. Write a program that outputs:
#
# the third character of this line;
# the penultimate character of this line;
# the first five characters of this line;
# the whole line except the last two characters;
# all symbols with even indices;
# all characters with odd indices;
# all characters in reverse order;
# all characters of the string one by one in reverse order, starting with the last one.
# Input data format
# One line is fed to the program, the length of which is more than 5 characters.
#
# Output data format
# The program should output the data according to the condition. Each value is displayed on a separate line.
string = input()
print(string[2])
print(string[-2])
print(string[:5])
print(string[:-2])
print(string[::2])
print(string[1::2])
print(string[::-1])
print(string[::-2])
