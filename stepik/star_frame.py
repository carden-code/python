# The input to the program is a natural number nn. Write a program that prints an n * 19 star frame.
#
# Input data format
# The input to the program is a natural number n ∈ [3; 19] - the height of the star frame.
#
# Output data format
# The program should display a star frame with dimensions n * 19.
#
# Prompt. To print a star line, use string multiplication by a number.
n = int(input())
z = '*' * 19
f = '*                 *'
for i in range(n):
    if i == 0 or i == (n - 1):
        print(z)
    else:
        print(f)
