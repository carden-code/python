string = input()
count_vowels = 0
count_consonants = 0
consonants = 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
vowels = 'ауоыиэяюёеАУОЫИЭЯЮЁЕ'
for c in string:
    if c in vowels:
        count_vowels += 1
    elif c in consonants:
        count_consonants += 1

print(f'Количество гласных букв равно {count_vowels}')
print(f'Количество согласных букв равно {count_consonants}')
