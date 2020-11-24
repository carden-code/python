# The input to the program is a line of text.
# Write a program that determines whether the shade of the text is good or not.
# The text has a good shade if it contains the substring "good" in all possible cases.
#
# Input data format
# The input to the program is a line of text.
#
# Output data format
# The program should print "YES" if the text has a good shade and "NO" otherwise.

string = input().lower()
a = 'хорош'
print('YES' if a in string else 'NO')
