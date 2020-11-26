# The input to the program is a line of text.
# Write a program that verifies that a string ends with a .com or .ru substring.
#
# Input data format
# The input to the program is a line of text.
#
# Output data format
# The program should print "YES" if the input string ends with the substring .com or .ru and "NO" otherwise.
# string = input()
# if string.endswith(('.ru', '.com')):
#     print('YES')
# else:
#     print('NO')
print('YES' if input().endswith(('.ru', '.com')) else 'NO')
