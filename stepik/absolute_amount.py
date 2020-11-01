# Five numbers are given. Write a program that calculates the sum of their modules.
#
# Input data format
# The input to the program is five real numbers.
#
# Output data format
# The program should output one number - the sum of the modules of the entered numbers.
a_1 = float(input())
a_2 = float(input())
a_3 = float(input())
a_4 = float(input())
a_5 = float(input())
sum_a = abs(a_1) + abs(a_2) + abs(a_3) + abs(a_4) + abs(a_5)
print(sum_a)
