# The input to the program is a natural number nn and nn lines, and then the number k.
# Write a program that prints the k-th letter of the entered lines on one line without spaces.
#
# Input data format
# The input to the program is a natural number n, then n lines, each on a separate line.
# At the end, a natural number k is entered - the number of the letter (the numbering starts with one).
#
# Output data format
# The program should display the text in accordance with the condition of the problem.
#
# Note. If some lines are too short, and they do not have a character with a given number,
# then such lines should be ignored in the output.
num = int(input())
list_strings = []
for i in range(num):
    list_strings.append(input())
k = int(input())
for j in list_strings:
    if len(j) >= k:
        print(j[k - 1], end='')
