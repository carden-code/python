# One line is fed to the program. Write a program that determines how many times + and * characters appear in a string.
#
# Input data format
# One line is fed to the program.
#
# Output data format
# The program should print the number of times + and * appear in the string.
#
# Sample Input:
# bcd+a++++**31415
#
# Sample Output:
# The + symbol occurs 5 times
# The * symbol occurs 2 times
string = input()
count_1 = 0
count_2 = 0
for c in string:
    if c == '+':
        count_1 += 1
    elif c == '*':
        count_2 += 1
print(f'The + symbol occurs {count_1} times')
print(f'The * symbol occurs {count_2} times')
