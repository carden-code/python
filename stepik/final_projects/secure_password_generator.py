from random import choice


def is_yes(yes):
    return yes.lower() == 'да'


def generate_password(length, chars):  # Метод принимает длину пароля и символы допустимые для генерации пароля.
    password = ''
    for _ in range(length):  # Задаём колличество итераций (длину пароля).
        password += choice(chars)  # С помощью функции choise() прибавляем случайный элемент к переменной password.
    return password  # По завершению цикла возвращаем password.


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
password_chars = ''

while True:  # С помощью бесконечного цикла запрашиваем данные от пользователя.
    number_passwords = input('Введите количество паролей для генерации: ')
    if number_passwords.isdigit() and int(number_passwords) > 0:  # Валидация (Является ли положительным целым числом).
        number_passwords = int(number_passwords)  # Преобразование строки в целое число.
        break  # Выход из цикла.
    else:  # Если введённые данные не валидны печатаем сообщение и снова запрашиваем данные.
        print('Пожалуйста введите целое число больше 0')
        continue

while True:
    password_length = input('Какой длины должен быть пароль?: ')
    if password_length.isdigit() and int(password_length) > 3:  # Валидация.
        password_length = int(password_length)  # Преобразование строки в целое число.
        break  # Выход из цикла.
    else:  # Если введённые данные не валидны печатаем сообщение и снова запрашиваем данные.
        print('Пожалуйста введите целое число больше 3')
        continue

while password_chars == '':
    dig = input(
        "Включать ли цифры 0123456789 ? ('Да' или любой другой символ если 'Нет'.): ")
    l_alpha = input(
        "Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? ('Да' или любой другой символ если 'Нет'.): ")
    u_alpha = input(
        "Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? ('Да' или любой другой символ если 'Нет'.): ")
    sym = input(
        "Включать ли символы !#$%&*+-=?@^_? ('Да' или любой другой символ если 'Нет'.): ")
    ambiguous = input(
        "Исключать ли неоднозначные символы il1Lo0O? ('Да' или любой другой символ если 'Нет'.): ")
    if is_yes(dig):
        password_chars += digits
    if is_yes(l_alpha):
        password_chars += lowercase_letters
    if is_yes(u_alpha):
        password_chars += uppercase_letters
    if is_yes(sym):
        password_chars += punctuation
    if password_chars == '':
        print('Пароль не может быть сформирован. Нужно включить хотябы 1 пункт. Попробуйте ещё раз.')
        continue
    if is_yes(ambiguous):
        for c in password_chars:
            if c in 'il1Lo0O':
                password_chars = password_chars.replace(c, '')

for i in range(number_passwords):
    print(generate_password(password_length, password_chars))
