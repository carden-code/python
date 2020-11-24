# The input to the program is a string consisting of the person's first and last name, separated by one space.
# Write a program that verifies that first and last names start with a capital letter.
#
# Input data format
# The input to the program is a string.
#
# Output data format
# The program should print "YES" if the first and last name begins with a capital letter and "NO" otherwise.
#
# Note. The string contains only letters.
string = input()
print('YES' if string == string.title() else 'NO')

