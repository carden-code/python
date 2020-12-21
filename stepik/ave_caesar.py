string = 'Day, mice. "Year" is a mistake!'
english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
max_index = (len(english_alphabet) - 1)
list_text = [c for c in string.split()]
new = ''
print(list_text)
for s in list_text:
    index = list_text.index(s)
    count = 0
    step = count
    for i in s:
        if i.isalpha():
            count += 1
    for c in s:
        new = ''
        if c.isalpha():
            index_alpha = english_alphabet.index(c.lower())
            index_step = index_alpha + step
            if c == c.upper():
                if index_step >= max_index:
                    index_step = ((max_index - index_alpha) - step) - 1
                    new += english_alphabet[index_step].upper()
                else:
                    new += english_alphabet[index_step].upper()
            if c == c.lower():
                if index_step >= max_index:
                    index_step = ((max_index - index_alpha) - step) - 1
                    new += english_alphabet[index_step]
                else:
                    new += english_alphabet[index_step]
        else:
            new += c
        list_text[index] = new
    new = ''


print(list_text)