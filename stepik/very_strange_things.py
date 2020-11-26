# Jim Hopper is trying to get Odie's message using the radio.
# The receiver receives nn different Morse code sequences.
# Having decoded them, he receives sequences of numbers and a lowercase Latin alphabet,
# while all Odi's messages contain the number 11, and at least 3 times.
# Help Jim determine the number of messages from Odie.
#
# Input data format
# The first line contains the number n - the number of messages;
# the next n lines contain lines containing Latin lowercase letters and numbers.
#
# Output data format
# The program should print the number of lines containing the number 11 at least 3 times.
#
# Note: The numbers 11 do not have to be separated by other characters,
# you need to count the occurrence of the sequence of characters "11", i.e. for example,
# line "111" contains one such sequence, while "1111" contains two.
n = int(input())
count = 0
for i in range(n):
    if input().count('11') >= 3:
        count += 1
print(count)
