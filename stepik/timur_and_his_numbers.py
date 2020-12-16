# Timur thought of a number from 1 to n.
# For what is the smallest number of questions (to which Timur answers "more" or "less")
# Ruslan can be guaranteed to guess Timur's number?
#
# Input data format
# The input to the program is a natural number nn.
#
# Output data format
# The program should display the smallest number of questions that are guaranteed to be enough for
# Ruslan to guess Timur's number.
from math import log, ceil
num = int(input())
print(ceil(log(num, 2)))