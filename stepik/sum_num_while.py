# The program is fed a sequence of integers, each number on a separate line.
# The end of the sequence is any negative number.
# Write a program that outputs the sum of all the members of a given sequence.
#
# Input data format
# The program is fed with a sequence of numbers, each number on a separate line.
#
# Output data format
# The program should display the sum of the members of the given sequence.
total = 0
i = int(input())
while i >= 0:
    total += i
    i = int(input())
print(total)
