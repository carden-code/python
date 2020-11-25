# The input to the program is a string. Write a program that counts the number of lowercase alphabetic characters.
#
# Input data format
# The input to the program is a string.
#
# Output data format
# The program should print the number of alphabetic characters in lowercase.
string = input()
count = 0
for c in string:
    if c == c.lower() and c not in '1234567890':
        count += 1
print(count)
# count = 0
# for c in input():
#     if c.islower():
#         count += 1
# print(count)
#
