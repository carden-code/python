class BankAccount:
    def __init__(self, name, balance):
        print('new_obj init')
        self.name = name
        self.balance = balance

    def __repr__(self):
        return f'Клиент {self.name} с балансовм: {self.balance}'

    def __add__(self, other):
        print('__add__ call')
        if isinstance(other, BankAccount):
            return self.balance + other.balance
        if isinstance(other, (int, float)):
            return BankAccount(self.name, self.balance + other)
        raise NotImplemented

    def __radd__(self, other):
        print('__radd__ call')
        return self + other

    def __mul__(self, other):
        print('__mul__ call')
        if isinstance(other, BankAccount):
            return self.balance * other.balance
        if isinstance(other, (int, float)):
            return self.balance * other
        if isinstance(other, str):
            return self.name + other
        raise NotImplemented
