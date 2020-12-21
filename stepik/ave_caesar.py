string = 'Day, mice. "Year" is a mistake!'
english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
list_text = [c for c in string.split()]
list_not_sym = []
b = ''
for s in list_text:
    for j in s:
        if j.isalpha():
            b += j
    list_not_sym.append(b)
    b = ''
cs = ''
print(list_text)
print(list_not_sym)
for c in list_text:
    list_c = c
    step = len(list_not_sym[list_text.index(c)])
    for j in list_c:
        if j.lower() in english_alphabet:
            index = english_alphabet.index(j.lower())
            index_step = index + step
            if j == j.upper():
                if index_step > len(english_alphabet) - 1:
                    index = index_step - (len(english_alphabet) - 1)
                    cs += english_alphabet[index + step].upper()
                elif index_step == len(english_alphabet) - 1:
                    index = index_step - (len(english_alphabet) - 1)
                    cs += english_alphabet[index + step].upper()
                else:
                    cs += english_alphabet[index + step].upper()
            elif j == j.lower():
                if index_step > len(english_alphabet) - 1:
                    index = index_step - (len(english_alphabet) - 1)
                    cs += english_alphabet[index + step]
                elif index_step == len(english_alphabet):
                    index = index_step - (len(english_alphabet) - 1)
                    cs += english_alphabet[index + step]
                else:
                    cs += english_alphabet[index + step]
            else:
                cs += j
print(cs)