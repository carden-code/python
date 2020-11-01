# Write a program that orders three numbers from highest to lowest.
#
# Input data format
# The program is fed three integers, each on a separate line.
#
# Output data format
# The program should print three numbers, each on a separate line, ordered from highest to lowest.
num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
first = max(num_1, num_2, num_3)
last = min(num_1, num_2, num_3)
second = 0
if (num_1 == first and num_2 == last) or (num_2 == first and num_1 == last):
    second = num_3
elif (num_1 == first and num_3 == last) or (num_3 == first and num_1 == last):
    second = num_2
elif (num_2 == first and num_3 == last) or (num_2 == last and num_3 == first):
    second = num_1
print(first)
print(second)
print(last)
