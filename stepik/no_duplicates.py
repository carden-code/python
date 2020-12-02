# The input to the program is a natural number n, and then n lines.
# Write a program that only prints out the unique strings, in the order in which they were entered.
#
# Input data format
# The input to the program is a natural number n, and then n lines, each on a separate line.
#
# Output data format
# The program should display the text in accordance with the condition of the problem.
num = int(input())
no_duplicates = []

for _ in range(num):
    string = input()
    if string not in no_duplicates:
        no_duplicates.append(string)

print(*no_duplicates, sep='\n')
