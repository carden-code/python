# The input to the program is a natural number n. Write a program that creates a list of divisors of an entered number.
#
# Input data format
# The input to the program is a natural number nn.
#
# Output data format
# The program should display a list consisting of the divisors of the entered number.
num = int(input())
list_divisor = []
for i in range(1, num + 1):
    if num % i == 0:
        list_divisor.append(i)
print(list_divisor)