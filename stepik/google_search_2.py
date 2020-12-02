# The input to the program is a natural number n, then n lines, then number k - the number of search queries,
# then k lines - search queries.
# Write a program that prints out all the strings that you entered, which include all searches.
#
# Input data format
# The input to the program is a natural number n - the number of lines,
# then the lines themselves in the specified amount, then the number k, then the search queries themselves.
#
# Output data format
# The program should display all entered lines in which all search queries are found.
#
# Note. Search should not be case sensitive.
num = int(input())
list_string = []
for _ in range(num):
    list_string.append(input())

num_search = int(input())
list_search = []
for _ in range(num_search):
    list_search.append(input())

count = 0
for i in list_string:
    for j in list_search:
        if j.lower() in i.lower():
            count += 1
        if count == num_search:
            print(i)
    count = 0
