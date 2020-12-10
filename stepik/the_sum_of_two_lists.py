# The input to the program is two lines of text containing integers.
# Lists of numbers L and M are formed from these lines.
# Write a program that creates a third list,
# the elements of which are the sums of the corresponding elements of the lists L and M.
# Next, the program should output each element of the resulting list on one line, separated by 1 space character.
#
# Input data format
# The program receives as input two lines of text containing integers separated by a space character.
#
# Output data format
# The program should display the text in accordance with the condition of the problem.
#
# Note. The number of numbers in both lines is the same.
L = [int(i) for i in input().split()]
M = [int(i) for i in input().split()]
print(*[L[i] + M[i] for i in range(len(L))])

