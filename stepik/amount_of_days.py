# Given the ordinal number of the month (1,2, ..., 12).
# Write a program that prints the number of days in this month. Accept that the year is not a leap year.
#
# Note. Try to write your program so that it has no more than three conditions.
#
# Input data format
# The program receives one integer at the entrance - the ordinal number of the month.
#
# Output data format
# The program should output the number of days in this month.
month = int(input('Please enter the month:'))

if month == 2:
    print(28)
elif month == 4 or month == 6 or month == 9 or month == 11:
    print(30)
else:
    print(31)
