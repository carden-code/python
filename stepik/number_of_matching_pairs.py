# The input to the program is a string of text containing natural numbers. A list of numbers is formed from this string.
# Write a program that calculates how many pairs of elements in the resulting list are equal to each other.
# It is considered that any two elements equal to each other form one pair, which must be counted.
#
# Input data format
# The input to the program is a line of text containing natural numbers, separated by a space character.
#
# Output data format
# The program should output one number - the number of pairs of elements that are equal to each other.
string = input()
list_num = string.split()
total = 0
for i in range(len(list_num)):
    for j in range(i + 1, len(list_num)):
        if list_num[i] == list_num[j]:
            total += 1
print(total)