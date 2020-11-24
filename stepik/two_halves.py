# The input to the program is a line of text.
# Write a program that cuts it into two equal parts, rearranges them, and displays them.
#
# Input data format
# The input to the program is a line of text.
#
# Output data format
# The program should display the text in accordance with the condition of the problem.
#
# Note. If the length of the string is odd, then the length of the first part must be one character longer.
string = input()
string_len = len(string)
a = string_len // 2
b = a + string_len % 2

if b > a:
    print(string[b:] + string[:b])
else:
    print(string[a:] + string[:b])
