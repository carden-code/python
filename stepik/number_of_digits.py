# The input to the program is a line of text. Write a program that counts the number of digits in a given line.
#
# Input data format
# The input to the program is a line of text.
#
# Output data format
# The program should print the number of digits in the given line.
string = input()
count = 0
digits = '1234567890'
for c in string:
    if c in digits:
        count += 1
print(count)
