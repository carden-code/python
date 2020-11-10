# The input to the program is a sequence of integers from 1 to 5, characterizing the student's grade,
# each number on a separate line. The end of the sequence is any negative number or a number greater than 5.
# Write a program that prints the number of fives.
#
# Input data format
# The program is fed with a sequence of numbers, each number on a separate line.
#
# Output data format
# The program should display the number of fives.
counter = 0
i = int(input())
while 0 < i < 6:
    if i == 5:
        counter += 1
    i = int(input())
print(counter)
