# The program receives a sequence of words as input, each word on a separate line.
# The end of the sequence is one of three words: "stop", "enough", "sufficiently" (in small letters, no quotes).
# Write a program that prints the total number of members in a given sequence.
#
# Input data format
# The program receives a sequence of words as input, each word on a separate line.
#
# Output data format
# The program should output the total number of members in the given sequence.
counter = 0
text = input()
while text != 'stop' and text != 'enough' and text != 'sufficiently':
    counter += 1
    text = input()
print(counter)
