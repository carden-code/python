# Практикуемся с property
from string import digits


class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def password(self):
        print('getter called')
        return self.__password

    @staticmethod
    def is_include_number(password):
        for digit in digits:
            if digit in password:
                return True
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
        if not User.is_include_number(value):
            raise ValueError('Парооль должен содержать хотябы одну цыфру.')
        self.__password = value
