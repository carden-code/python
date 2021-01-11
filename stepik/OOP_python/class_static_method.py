class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        Robot.population += 1
        print(f'Робот {name} был создан')

    @classmethod
    def how_many(cls):
        print(f'{cls.population}, вот сколько нас еще осталось')

    def destroy(self):
        Robot.population -= 1
        print(f'Робот {self.name} был уничтожен')

    def say_hello(self):
        print(f'Робот {self.name} приветствует тебя, особь человеческого рода')
