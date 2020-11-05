# A positive real number is given. Print its first digit after the decimal point.
#
# Input data format
# The input to the program is a positive real number.
#
# Output data format
# The program should output a figure in accordance with the condition of the problem.
num = float(input())
fractional = num - (int(num))
first_digit = fractional / 0.10
print(int(first_digit))
