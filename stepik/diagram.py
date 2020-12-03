# The input to the program is a string of text containing integers.
# Write a program that plots a bar chart for given numbers.
#
# Input data format
# The input to the program is a text string containing integers separated by a space character.
#
# Output data format
# The program should output a bar chart.
# Sample Input 1:
#
# 1 2 3 4 5
# Sample Output 1:
#
# +
# ++
# +++
# ++++
# +++++
string = input()
sym = '+'
for i in string.split():
    print(sym * int(i))
