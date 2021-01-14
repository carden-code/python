# Сейчас вам нужно создать класс Quadrilateral (четырехугольник), в котором есть:
#
# - конструктор __init__. Он должен сохранять в экземпляр класса два атрибута: width и height.
#     При этом в сам метод __init__ может передаваться один аргумент
#     (тогда в width и height присваивать это одно одинаковое значение, тем самым делать квадрат),
#     либо два аргумента( первый идет в атрибут width, второй - в height)
# - переопределить метод __str__ следующим образом:
#     если width и height одинаковые, возвращать строку "Куб размером <width>х<height>
#     в противном случае, возвращать строку "Прямоугольник размером <width>х<height>
# - переопределить метод __bool__ так, чтобы он возвращал True, если объект является кубом, и False в противном случае
class Quadrilateral:
    def __init__(self, width, height=0):
        if height > 0:
            self.width = width
            self.height = height
        else:
            self.width = width
            self.height = width

    def __str__(self):
        if self.width == self.height:
            return f'Куб размером {self.width}х{self.height}'
        else:
            return f'Прямоугольник размером {self.width}х{self.height}'

    def __bool__(self):
        return self.width == self.height

