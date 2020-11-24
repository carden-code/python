# The input to the program is one word written in lowercase.
# Write a program that detects whether it is a palindrome.
#
# Input data format
# The input to the program is one word in lower case.
#
# Output data format
# The program should print "YES" if the word is a palindrome and "NO" otherwise.
string = input()
if string[::-1] == string:
    print('YES')
else:
    print('NO')
