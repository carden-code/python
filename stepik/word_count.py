# The input to the program is a line of text consisting of words separated by exactly one space.
# Write a program that counts the number of words in it.
#
# Input data format
# The input to the program is a line of text.
#
# Output data format
# The program should output the word count.
#
# Note 1. A line of text does not contain leading or trailing spaces.
#
# Note 2. Use the count method to solve the problem.
string = input()
s = ' '
print(string.count(s) + 1)
