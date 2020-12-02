# The input to the program is a natural number n, and then n integers.
# Write a program that prints all negative numbers first,
# then zeros, then all positive numbers, each on a separate line.
# The numbers must be displayed in the same order in which they were entered.
#
# Input data format
# The input to the program is a natural number nn, and then nn integers, each on a separate line.
#
# Output data format
# The program should display the text in accordance with the condition of the problem.
#
# num = int(input())
# list_numbers = []
# for _ in range(num):
#     list_numbers.append(int(input()))
# should_restart = True
# while should_restart:
#     should_restart = False
#     for i in range(len(list_numbers)):
#         if list_numbers[i] < 0:
#             print(list_numbers[i])
#             del list_numbers[i]
#             should_restart = True
#             break
#         elif min(list_numbers) == 0:
#             if list_numbers[i] == 0:
#                 print(list_numbers[i])
#                 del list_numbers[i]
#                 should_restart = True
#                 break
#         elif min(list_numbers) > 0:
#             print(list_numbers[i])
#             del list_numbers[i]
#             should_restart = True
#             break
n, li = int(input()), []
for _ in range(n):
    x = int(input())
    li.append(x)
for i in li:
    if i < 0:
        print(i)
for i in li:
    if i == 0:
        print(i)
for i in li:
    if i > 0:
        print(i)
