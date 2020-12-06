# The input to the program is a string of text containing integers. Write a program using a list expression that prints squares of even numbers that do not end in 4.
#
# Input data format
# The input to the program is a string of text containing integers separated by a space character.
#
# Output data format
# The program should display the text in accordance with the condition of the problem.
#
# Note. The program can be written in one line of code.
#
print(*[int(i) ** 2 for i in input().split() if int(i) % 2 == 0 and int(i) ** 2 % 10 != 4])
