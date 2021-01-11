# Практикуемся с property
from string import digits


class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__secret = 'abracadabra'

    @property
    def secret(self):
        pw = input('Введите пароль: ')
        if self.password == pw:
            return self.__secret
        else:
            raise ValueError('Нет доступа!')

    @property
    def password(self):
        print('getter called')
        return self.__password

    @staticmethod
    def __is_include_number(password):
        for digit in digits:
            if digit in password:
                return True
        return False

    @staticmethod
    def __check_password(password):
        path = '/home/vyacheslav/python/stepik/OOP_python/pass.txt'
        with open(path, "r") as f:
            array = [line.rstrip('\n') for line in f]

        if password not in array:
            return True
        else:
            return False

    @password.setter
    def password(self, value):
        print('setter called')
        if not isinstance(value, str):
            raise TypeError('Пароль должен быть строкой.')
        if len(value) < 4:
            raise ValueError('Парооль должен быть больше 3х символов.')
        if len(value) > 12:
            raise ValueError('Пароль должен быть меньше 13 символов.')
        if not User.__is_include_number(value):
            raise ValueError('Парооль должен содержать хотябы одну цыфру.')
        if not User.__check_password(value):
            raise ValueError('Слишком простой пароль.')

        self.__password = value
