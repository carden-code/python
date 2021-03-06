# Создайте класс City, у которого есть:
#
# - конструктор __init__, принимающий единственный аргумент - название города.
#    Вам необходимо сохранить его в качестве атрибута экземпляра name,
#    причем вам нужно преобразовать переданное имя города таким образом,
#    чтобы первая буква каждого слова была заглавной,
#    а остальные оказались строчными (пример "new york" - > "New York")
# - переопределить метод __str__ таким образом, чтобы он возвращал имя города
# - переопределить метод __bool__ так, чтобы он возвращал False,
#    если название города заканчивается на любую гласную букву латинского алфавита (a, e, i, o, u),
#    в противном случае True
class City:
    def __init__(self, name):
        self.name = name.title()

    def __str__(self):
        return self.name

    def __bool__(self):
        return self.name[-1] not in ['a', 'e', 'i', 'o', 'u']
