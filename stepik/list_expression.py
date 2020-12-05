# The input to the program is a natural number n.
# Write a program that runs a list expression that creates a list of input numbers from 1 to n,
# and then outputs its elements line by line, that is, each on a separate line.
#
# Input data format
# A natural number is offered at the entrance to the program.
#
# Output data format
# The program should display the text in accordance with the condition of the problem.
#
# Note. To display items, list list loop for.
print(*[i ** 2 for i in range(1, int(input()) + 1)], sep='\n')
