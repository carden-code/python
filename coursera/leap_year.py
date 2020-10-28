# A natural number is given. It is required to determine whether the year with the given number is a leap year.
# If the year is a leap year, then output YES, otherwise output NO.
# Recall that according to the Gregorian calendar,
# A year is a leap year if its number is a multiple of 4 but not a multiple of 100, or if it is a multiple of 400.
#
# Input format
#
# One natural number is entered.
#
# Output format
#
# Print the answer to the problem.
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('YES')
else:
    print('NO')
