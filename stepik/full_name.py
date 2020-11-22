# The program receives three lines at the entrance: first name, last name and patronymic.
# Write a program that prints out the person's initials.
#
# Input data format
# The program receives three lines as input, each on a separate line.
#
# Output data format
# The program should display the name of the person.
#
# Note. It is guaranteed that the first name, last name and patronymic start with a capital letter.
name = input()
surname = input()
patronymic = input()
print(surname[0], name[0], patronymic[0], sep='')
