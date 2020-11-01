# Write a program that reads one number from the keyboard and prints the inverse of it.
# If at the same time the number entered from the keyboard is zero,
# then output "The reverse number does not exist" (without quotes).
#
# Input data format
# The input to the program is one real number.
#
# Output data format
# The program should output a real number opposite to the given one,
# or the text in accordance with the condition of the problem.
num = float(input())
if num == 0:
    print('The reverse number does not exist')
else:
    print(num**-1 / 1)
