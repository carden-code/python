# The input to the program is a line of text.
# Write a program that removes from it all characters that are multiples of 3, that is, characters with indices 0, 3, 6.
#
# Input data format
# The input to the program is a line of text.
#
# Output data format
# The program should output a line of text in accordance with the condition of the problem.
string = input()
for c in range(len(string)):
    if not c % 3 == 0:
        print(string[c], end='')
