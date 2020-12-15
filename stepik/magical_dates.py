# The magic date is the date when the day multiplied by the month
# is equal to the number formed by the last two digits of the year.
#
# Write a function, is_magic (date), that takes a string representation of a corrected date as an argument and
# returns True if the date is magic and False otherwise.
def is_magic(date):
    list_date = [int(c) for c in date.split('.')]
    return list_date[0] * list_date[1] == list_date[2] % 100


date = input()

print(is_magic(date))
