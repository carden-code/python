# The input to the program is a natural number n, and then nn integers.
# Write a program that for each entered number x outputs the value of the function f(x) = x**2 + 2 * x + 1,
# each on a separate line.
#
# Input data format
# The input to the program is a natural number nn, and then nn integers, each on a separate line.
#
# Output data format
# The program should print first the entered numbers, then the empty string, and then the corresponding function values.
num = int(input())
list_num = []
for _ in range(num):
    list_num.append(int(input()))
print(*list_num, sep='\n')
print()
for x in list_num:
    value = x**2 + 2 * x + 1
    print(value)
