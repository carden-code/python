from random import choice, shuffle
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
password_chars = ''
number_passwords = input('введите количество паролей для генерации: ')
password_length = int(input('Какой длины должен быть пароль?: '))
dig = input('Включать ли цифры 0123456789 ? (да/нет): ').lower()
u_alpha = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (да/нет): ')
l_alpha = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (да/нет): ')
sym = input('Включать ли символы !#$%&*+-=?@^_? (да/нет): ')
ambiguous = input('Исключать ли неоднозначные символы il1Lo0O? (да/нет): ')


def generate_password(length, chars):
    pass
