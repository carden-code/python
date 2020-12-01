# When analyzing data collected from a scientific experiment,
# it can be helpful to remove the largest and smallest value.
#
# The input to the program is a natural number n, and then n different natural numbers.
# Write a program that removes the smallest and largest values from specified numbers,
# and then prints the remaining numbers, each on a separate line, without changing their order.
#
# Input data format
# The input to the program is a natural number nn, and then n different natural numbers, each on a separate line.
#
# Output data format
# The program should display the text in accordance with the condition of the problem.
num = int(input())
list_num = []
for _ in range(num):
    list_num.append(int(input()))
a, b = max(list_num), min(list_num)
del list_num[list_num.index(a)]
del list_num[list_num.index(b)]
print(*list_num, sep='\n')
