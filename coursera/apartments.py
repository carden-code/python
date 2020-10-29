# The house has several entrances. Each entrance has the same number of apartments.
# Apartments are numbered in a row, starting from one.
# Can the first apartment in some entrance have number x, and the last one - number y?
#
# Input format
#
# Two natural numbers x and y (x ≤ y) are entered.
#
# Output format
#
# Print the word YES (in capital Latin letters), if possible, and NO otherwise.
x = int(input())
y = int(input())
number_apartments = (y - x) + 1
last_apartment_previous = x - 1
previous_entrance = last_apartment_previous - number_apartments
remainder = previous_entrance % number_apartments
if x == 1 or remainder == 0:
    print('YES')
else:
    print('NO')
