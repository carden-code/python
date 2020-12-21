# Описание проекта:
#     Требуется написать программу, способную шифровать и дешифровать текст в соответствии с алгоритмом Цезаря.
#     Она должна запрашивать у пользователя следующие данные:
#
#     направление: шифрование или дешифрование;
#     язык алфавита: русский или английский;
#     шаг сдвига (со сдвигом вправо).
#
#     Примечание 1. Считайте, что в русском языке 32 буквы (буква ё отсутствует).
#     Примечание 2. Неалфавитные символы — знаки препинания, пробелы, цифры — не меняются.
#     Примечание 3. Сохраните регистр символов.
#
#     Например, текст:
#         "Умом Россию не понять" при сдвиге на одну позицию вправо будет преобразован в: "Фнпн Спттйя ож рпоауэ".
#
text = input('Введите ваш текст для шифрования или дешифрования: ')
text_list = [c for c in text]
russian_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
text_new = ''
direction = ''
language = ''
step = ''
lang = ''

while True:
    direction = input("Если вы хотите зашифровать текст введите '+', если расшифровать '-': ")
    if direction not in ['+', '-']:
        print('Может быть введём + или - ?')
        continue
    language = input("На каком языке ваш текст? Если Русский введите - 'ru', если Английский - 'en': ")
    if language not in ['ru', 'en']:
        print('Может быть введём ru или - en ?')
        continue
    step = input('Введите целое положительное число - шаг шифровния или дешифрования: ')
    if not step.isdigit():
        print('Может быть введём целое положительное число?')
        continue
    else:
        step = int(step)
        break

if language == 'ru':
    lang = russian_alphabet
elif language == 'en':
    lang = english_alphabet

for c in text_list:
    if c.lower() in lang:
        index = lang.index(c.lower())
        index_encrypt = index + step
        index_decipher = index - step
        if c == c.upper():
            if direction == '+':
                if index_encrypt >= len(lang):
                    index = index_encrypt - len(lang)
                    text_new += lang[index].upper()
                else:
                    text_new += lang[index_encrypt].upper()
            elif direction == '-':
                if index_decipher < 0:
                    index = index_decipher + len(lang)
                    text_new += lang[index].upper()
                else:
                    text_new += lang[index_decipher].upper()
        elif c == c.lower():
            if direction == '+':
                if index_encrypt >= len(lang):
                    index = index_encrypt - len(lang)
                    text_new += lang[index]
                else:
                    text_new += lang[index_encrypt]
            elif direction == '-':
                if index_decipher < 0:
                    index = index_decipher + len(lang)
                    text_new += lang[index]
                else:
                    text_new += lang[index_decipher]
    else:
        text_new += c
print(text_new)
