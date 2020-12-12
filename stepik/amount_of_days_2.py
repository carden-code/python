# Write a function get_days (month) that takes a month as an argument and returns the number of days in a given month.
#
# Note 1. It is guaranteed that the passed argument is in the range 1 to 12.
#
# Note 2. Consider a non-leap year.
def get_days(month):
    dictionary = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    return dictionary[month]


num = int(input())
print(get_days(num))
