# The input to the program is two numbers a and b.
# Write a program that, for each code value in the range a through b (inclusive),
# outputs its corresponding character from the Unicode character table.
#
# Input data format
# The input to the program is two natural numbers, each on a separate line.
#
# Output data format
# The program should display the text in accordance with the condition of the problem.
a = int(input())
b = int(input())
for i in range(a, b + 1):
    print(chr(i), end=' ')
