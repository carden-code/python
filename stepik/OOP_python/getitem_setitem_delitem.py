# Магические методы
# Методы __getitem__, __setitem__, __delitem__

class Vector:
    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return str(self.values)

    def __getitem__(self, item):
        if 0 <= item < len(self.values):
            return self.values[item]
        else:
            raise IndexError('Индекс за границами нашей коллекции.')

    # # Изменение нумерации списка ( с нуля на 1)
    # def __getitem__(self, item):
    #     if 1 <= item <= len(self.values):
    #         return self.values[item - 1]
    #     else:
    #         raise IndexError('Индекс за границами нашей коллекции.')

    def __setitem__(self, key, value):
        if 0 <= key < len(self.values):
            self.values[key] = value
        else:
            raise IndexError('Индекс за границами нашей коллекции.')

    # # Создаст разряженный список, если попытаться присвоить значение по индексу за пределами списка.
    # def __setitem__(self, key, value):
    #     if 1 <= key <= len(self.values):
    #         self.values[key - 1] = value
    #     elif key > len(self.values):
    #         diff = key - len(self.values)
    #         self.values.extend([0] * diff)
    #         self.values[key - 1] = value
    #     else:
    #         raise IndexError('Индекс за границами нашей коллекции.')

    def __delitem__(self, key):
        if 0 <= key < len(self.values):
            del self.values[key]
        else:
            raise IndexError('Индекс за границами нашей коллекции.')
