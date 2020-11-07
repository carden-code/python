# Write a program that reads 10 numbers and prints the product of nonzero numbers.
#
# Input data format
# The program receives 10 integers as input, each on a separate line.
#
# Output data format
# The program should print the product of nonzero numbers.
#
# Note. It is guaranteed that at least one of the 10 numbers is nonzero.
total = 1
for i in range(10):
    num = int(input())
    if num != 0:
        total *= num
print(total)
