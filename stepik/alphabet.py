# Write a program that prints out the following list:
#
# ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]
# Output data format
# The program should print the specified list.
#
# Note. The last item in the list consists of 26 z characters.
alphabet = 'abcdefghijklmnopqrstuvwxyz'
list_alphabet = []
count = 1
for i in alphabet:
    list_alphabet.append(i * count)
    count += 1
print(list_alphabet)