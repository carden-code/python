# The input to the program is a line of text.
# Write a program that prints the index of the second occurrence of the letter "f".
# If the letter "f" occurs only once, print the number -1, and if it does not occur even once, print the number -2.
#
# Input data format
# The input to the program is a line of text.
#
# Output data format
# The program should display the text in accordance with the condition of the problem.
string = input()
if string.count('f') == 1:
    print(-1)
elif string.count('f') == 0:
    print(-2)
else:
    first = string.index('f')
    print(string.index('f', first + 1))
