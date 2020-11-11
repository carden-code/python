# A natural number n is given, (n >= 10). Write a program that determines its maximum and minimum numbers.
#
# Input data format
# One natural number is fed into the program.
#
# Output data format
# The program should display the maximum and minimum digits of the entered number (with an explanatory inscription).
num = int(input())
maxim = num % 10
minim = num % 10
while num != 0:
    last_num = num % 10
    if last_num >= maxim:
        maxim = last_num
    elif last_num <= minim:
        minim = last_num
    num = num // 10
print('The maximum digit is', maxim)
print('The minimum digit is', minim)
