# The input to the program is a string of text containing integers.
# A list of numbers is formed from this string.
# Write a program that sorts and displays the given list first in ascending and then descending order.
#
# Input data format
# The input to the program is a string of text containing integers separated by a space character.
#
# Output data format
# The program should output two lines of text in accordance with the condition of the problem.
string = input()
list_num = [int(x) for x in string.split()]
list_num.sort()
print(*list_num)
list_num.sort(reverse=True)
print(*list_num)