# The input to the program is a string containing English text.
# Write a program that counts the total number of articles: 'a', 'an', 'the'.
#
# Input data format
# The input to the program is a string containing English text.
# The words of the text are separated by a space character.
#
# Output data format
# The program should output the total number of articles 'a', 'an', 'the' along with explanatory text.
#
# Note. Articles can start with a capital letter 'A', 'An', 'The'.
list_string = input().lower().split()
count = 0

for c in list_string:
    if c == 'a' or c == 'an' or c == 'the':
        count += 1

print(f'Общее количество артиклей: {count}')
