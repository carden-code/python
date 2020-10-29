# On the roulette wheel, the pockets are numbered from 0 to 36. Below are the colors of the pockets:
#
# pocket 0 green;
# for pockets 1 to 10, odd numbered pockets are red, even numbered pockets black;
# for pockets 11 to 18, odd numbered pockets are black, even numbered pockets red;
# for pockets 19 to 28, odd numbered pockets are red, even numbered pockets black;
# for pockets 29 to 36, odd numbered pockets are black, even numbered pockets red.
# Write a program that reads the pocket number and indicates whether the pocket is green, red, or black.
# The program should display an error message if the user enters a number that is outside the range from 0 to 36.
#
# Input data format
# The input to the program is one integer.
#
# Output data format
# The program should display the color of the pocket or the message "input error",
# if the entered number is outside the range from 0 to 36.
x = int(input())
if x < 0 or x > 36:
    print('Input Error')
elif x == 0:
    print('Green')
elif 1 <= x <= 10:
    if x % 2 == 0:
        print('Black')
    else:
        print('Red')
elif 11 <= x <= 18:
    if x % 2 == 0:
        print('Red')
    else:
        print('Black')
elif 19 <= x <= 28:
    if x % 2 == 0:
        print('Black')
    else:
        print('Red')
elif 29 <= x <= 36:
    if x % 2 == 0:
        print('Red')
    else:
        print('Black')
