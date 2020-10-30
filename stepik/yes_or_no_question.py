# Write a program that accepts a number as input and, depending on the conditions, outputs the text "YES" or "NO".
#
# Conditions:
#
# if the number is odd, output "YES";
# if the number is even in the range from 2 to 5 (inclusive), then output "NO";
# if the number is even in the range from 6 to 20 (inclusive), then output "YES";
# if the number is even and more than 20, then output "NO".
# Input data format
# The input to the program is a natural number.
#
# Output data format
# The program should display the text in accordance with the condition of the problem.
num = int(input())
if num % 2 != 0:
    print('YES')
elif num % 2 == 0 and 2 <= num <= 5:
    print('NO')
elif num % 2 == 0 and 6 <= num <= 20:
    print('YES')
elif num % 2 == 0 and num > 20:
    print('NO')
