# Write a function print_fio (name, surname, patronymic) that takes three parameters:
#
# name - person's name;
# surname - person's surname;
# patronymic - middle name of a person;
# and then prints out the person's full name.
#
# Note. Consider the fact that all three letters in the full name must be uppercase.
def print_fio(_name, _surname, _patronymic):
    print(f'{surname[0]}{name[0]}{patronymic[0]}'.upper())


name, surname, patronymic = input(), input(), input()
print_fio(name, surname, patronymic)
