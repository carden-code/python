# Практика: элементы класса
#
# Создайте класс Movie и определите конструктор класса с такими параметрами, как заголовок, режиссер и год выпуска.
#
# Затем создайте такие объекты, как «Титаник» (реж. Джеймс Кэмерон, 1997),
# «Звездные войны» (реж. Джордж Лукас, 1977) и «Бойцовский клуб» (реж. Дэвид Финчер, 1999).
#
# Некоторые атрибуты этих объектов будут напечатаны, чтобы проверить их.
#
# Год передается в виде строки.
class Movie:

    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year


titanic = Movie('Титаник', 'Джеймс Кэмерон', '1997')
star_wars = Movie('Звездные войны', 'Джордж Лукас', '1977')
fight_club = Movie('Бойцовский клуб', 'Дэвид Финчер', '1999')

# don't delete this code
# it is here to check your results
print(titanic.title)
print(star_wars.year)
print(fight_club.director)