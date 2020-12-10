# An even number n is fed into the program, n> = 2.
# Write a program that outputs a list of even numbers [2, 4, 6, ..., n].
#
# Input data format
# An even natural number is fed into the program.
#
# Output data format
# The program should display the text in accordance with the condition of the problem.
print([i for i in range(1, int(input()) + 1) if i % 2 == 0])
