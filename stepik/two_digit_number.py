# Write a program that determines if a two-digit number entered from the keyboard consists of the same numbers.
# If so, the program outputs "YES", otherwise the program outputs "NO".
num = int(input('Please enter a two-digit number:'))
last_digit = num % 10    # last digit of the number
first_digit = num // 10  # first digit of number

if last_digit == first_digit:
    print('Yes')
else:
    print('No')
