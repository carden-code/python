# The input to the program is a sequence of integers divisible by 7, each number on a separate line.
# The end of a sequence is any number not divisible by 7.
# Write a program that prints out the members of a given sequence.
#
# Input data format
# The program is fed with a sequence of numbers, each number on a separate line.
#
# Output data format
# The program should output the members of the given sequence.
num = int(input())

while num % 7 == 0:
    print(num)
    num = int(input())
