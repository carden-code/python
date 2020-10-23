# Write a program to find the digits of a four-digit number.
#
# Input data format
# The input to the program is a positive four-digit integer.
#
# Output data format
# The program should display the text in accordance with the condition of the problem.
#
# Sample Input 1:
#
# 3281
# Sample Output 1:
#
# The digit in the thousands position is 3
# The digit in the hundreds position is 2
# The digit in the tens position is 8
# The digit in the units position is 1
number = int(input('Please enter a positive four-digit integer:'))
a = number % 10
b = (number % 100) // 10
c = (number % 1000) // 100
d = number // 1000
print('The digit in the thousands position is', d)
print('The digit in the hundreds position is', c)
print('The digit in the tens position is', b)
print('The digit in the units position is', a)
