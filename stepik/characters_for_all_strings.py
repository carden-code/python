# The input to the program is a natural number n, and then n lines.
# Write a program that creates a list of characters from all strings and then prints it out.
#
# Input data format
# The input to the program is a natural number nn, and then nn lines, each on a separate line.
#
# Output data format
# The program should output a list consisting of characters of all entered lines.
#
# Note. The resulting list may contain the same characters.
num = int(input())
char_list = []
for _ in range(num):
    char_list.extend(input())
print(char_list)