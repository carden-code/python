# The input to the program is a natural number n, and then n integers.
# Write a program that creates a list from the specified numbers,
# then removes all elements at odd indices, and then displays the resulting list.
#
# Input data format
# The input to the program is a natural number nn, and then nn integers, each on a separate line.
#
# Output data format
# The program should display a list in accordance with the condition of the problem.
#
# Note. Use the del statement.
num = int(input())
list_num = []
for i in range(num):
    list_num.append(int(input()))
del list_num[1::2]
print(list_num)
