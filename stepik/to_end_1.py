# The program receives a sequence of words as input, each word on a separate line.
# The end of the sequence is the word "END" (without quotes).
# Write a program that prints out the members of a given sequence.
#
# Input data format
# The program receives a sequence of words as input, each word on a separate line.
#
# Output data format
# The program should output the members of the given sequence.
text = input()
while text != 'END':
    print(text)
    text = input()
