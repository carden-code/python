# our class Ship
class Ship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0
        self.city = ''

    def sail(self, city):
        self.city = city
        print(f"The {self.name} has sailed for {self.city}!")


black_pearl = Ship("Black Pearl", 800)
black_pearl.sail(input())
