# Создайте класс Zebra, внутри которого есть метод which_stripe ,
#     который поочередно печатает фразы "Полоска белая", "Полоска черная", начиная именно с фразы "Полоска белая"
#
# Пример работы с классом Zebra
#
# z1 = Zebra()
# z1.which_stripe() # печатает "Полоска белая"
# z1.which_stripe() # печатает "Полоска черная"
# z1.which_stripe() # печатает "Полоска белая"
#
# z2 = Zebra()
# z2.which_stripe() # печатает "Полоска белая"
class Zebra:
    def __init__(self, strip='Полоска белая'):
        self.strip = strip
        self.num = 1

    def which_stripe(self):
        self.strip = 'Полоска черная' if self.num % 2 == 0 else 'Полоска белая'
        self.num += 1
        print(self.strip)
