# Write a program that reads two integers and a string from the keyboard.
# If this string is one of the four mathematical operations (+, -, *, /),
# then print the result of applying this operation to the numbers entered earlier,
# otherwise, output “Invalid operation”.
# If the user wants to divide by zero, output the text "You cannot divide by zero!"
#
# Input data format
# The input to the program is two integers, each on a separate line, and a string.
#
# Output data format
# The program should display the result of applying the operation to the entered numbers or the corresponding text,
# if the operation is invalid or if division by zero occurs.
num_1 = int(input())
num_2 = int(input())
sign = input()

if sign != '+' and sign != '-' and sign != '*' and sign != '/':
    print('Invalid operation')
elif sign == '+':
    print(num_1 + num_2)
elif sign == '-':
    print(num_1 - num_2)
elif sign == '*':
    print(num_1 * num_2)
elif sign == '/':
    if num_2 == 0:
        print('You cannot divide by zero!')
    else:
        print(num_1 / num_2)
