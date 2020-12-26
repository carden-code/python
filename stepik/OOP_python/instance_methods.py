# Методы экземпляра. Аргумент self
class Cat:
    breet = 'pers'

    def hello(*args):
        print('Hello world from kitty', args)

    def show_breed(self):
        print(f'my breed is {self.breet}')

    def show_name(self):
        if hasattr(self, 'name'):
            print(f'my name is {self.name}')
        else:
            print('nothing')

    def set_value(self, value, age=2):
        self.name = value
        self.age = age
