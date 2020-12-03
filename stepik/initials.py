# The input to the program is a line of text containing the name, patronymic and surname of the person.
# Write a program that prints out the person's initials.
#
# Input data format
# The input to the program is a line of text containing the name, patronymic and surname of the person.
#
# Output data format
# The program should display the text in accordance with the condition of the problem.
string = input()
list_string = string.split()
initials = []

for i in range(len(list_string)):
    initials.append(list_string[i][0].upper())

print('.'.join(initials), '.', sep='')
