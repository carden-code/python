# One line is fed to the program.
# Write a program that prints the "Digit" message (without quotes) if the string contains a digit.
# Otherwise, display the message "No digits" (without quotes).
#
# Input data format
# One line is fed to the program.
#
# Output data format
# The program should display the text in accordance with the condition of the problem.
string = input()
count = 0
for c in string:
    for j in range(10):
        if c == str(j):
            count += 1
if count > 0:
    print('Digit')
else:
    print('No digits')
