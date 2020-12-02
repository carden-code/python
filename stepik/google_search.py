# The input to the program is a natural number n, then n lines, then another line - a search query.
# Write a program that prints out all the lines entered that contain the search term.
#
# Input data format
# The input to the program is a natural number n - the number of lines,
# then the lines themselves in the specified amount, then one search query.
#
# Output data format
# The program should display all entered strings in which the search query occurs.
#
# Note. Search should not be case sensitive.
num = int(input())
string_list = []
for _ in range(num):
    string_list.append(input())
search = input()
for i in string_list:
    if search.lower() in i.lower():
        print(i)
