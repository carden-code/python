# One line is fed to the program. Write a program that displays the elements of a row in a column in reverse order.
#
# Input data format
# One line is fed to the program.
#
# Output data format
# The program should display the elements of the row in a column in reverse order.
string = input()
for elem in reversed(string):
    print(elem)
