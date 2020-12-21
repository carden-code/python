# At the entrance to the program, a line of text in English, in which you need to encrypt all the words.
# Each word in the string should be encrypted using the Caesar cipher (cyclic shift by the length of that word).
# Lowercase letters remain lowercase and uppercase letters remain uppercase.
#
# Input data format
# The input to the program is a line of text in English.
#
# Output data format
# The program should output the cipher text in accordance with the condition of the problem.
#
# Note. Non-English characters are not modified.
string = input()
english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
max_index = (len(english_alphabet) - 1)
list_text = [c for c in string.split()]
encrypted_string = ''
step = 0

for s in list_text:
    index = list_text.index(s)
    for i in s:
        if i.isalpha():
            step += 1
    for c in s:
        if c.isalpha():
            index_alpha = english_alphabet.index(c.lower())
            index_step = index_alpha + step
            if c.isupper():
                if index_step >= max_index:
                    index_step = (step - (max_index - index_alpha)) - 1
                    encrypted_string += english_alphabet[index_step].upper()
                else:
                    encrypted_string += english_alphabet[index_step].upper()
            if c.islower():
                if index_step >= max_index:
                    index_step = (step - (max_index - index_alpha)) - 1
                    encrypted_string += english_alphabet[index_step]
                else:
                    encrypted_string += english_alphabet[index_step]
        else:
            encrypted_string += c
    list_text[index] = encrypted_string
    encrypted_string = ''
    step = 0

print(' '.join(list_text))
