# Red, blue, and yellow are called primary colors because they cannot be obtained by mixing other colors.
# When two primary colors are mixed, a secondary color is obtained:
#
# if you mix red and blue, you get purple;
# if you mix red and yellow, you get orange;
# if you mix blue and yellow, you get green.
# Write a program that reads the names of the two primary colors for mixing.
#   If the user enters anything other than red, blue, or yellow, the program should display an error message. Otherwise,
#   the program should print the name of the secondary color, which will be the result.
#
# Input data format
# The program receives two lines as input, each on a separate line.
#
# Output data format
# The program should display the resulting color of the blend or the message "color error" if a color was not entered.

first = input('Please enter the first color:').lower()
second = input('Please enter a second color:').lower()
if first == second:
    if first == 'red' or first == 'blue' or first == 'yellow':
        print(first)
    else:
        print('Color error')
elif (first == 'red' or first == 'blue') and (second == 'blue' or second == 'red'):
    print('Violet')
elif (first == 'red' or first == 'yellow') and (second == 'yellow' or second == 'red'):
    print('Orange')
elif (first == 'blue' or first == 'yellow') and (second == 'yellow' or second == 'blue'):
    print('Green')
else:
    print('Color error')
