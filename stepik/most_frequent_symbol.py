# The input to the program is a line of text. Write a program that displays the character that appears most frequently.
#
# Input data format
# The input to the program is a line of text.
# The text can contain lowercase and uppercase letters of the English and Russian alphabet, as well as numbers.
#
# Output data format
# The program should display the character that appears most frequently.
#
# Note 1. If there are several such characters, output the last character in order.
#
# Note 2. A distinction should be made between uppercase and lowercase letters,
# as well as letters of the Russian and English alphabets.
string = input()
sym = 'a'
for c in string:
    if string.count(c) >= string.count(sym):
        sym = c
print(sym)
