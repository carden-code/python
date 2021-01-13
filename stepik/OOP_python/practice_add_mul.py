class Vector:
    def __init__(self, *args):
        self.values = [i for i in args if isinstance(i, int)]
        self.values.sort()

    def __str__(self):
        return f'Вектор{tuple(self.values)}' if self.values else 'Пустой вектор'

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Vector(*[i + other for i in self.values])
        elif isinstance(other, Vector):
            if len(other.values) == len(self.values):
                new_values = []
                for i in self.values:
                    for j in other.values:
                        if self.values.index(i) == other.values.index(j):
                            new_values.append(i + j)
                return Vector(*new_values)
            else:
                return "Сложение векторов разной длины недопустимо"
        else:
            print(f"Вектор нельзя сложить с {other}")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(*[i * other for i in self.values])
        elif isinstance(other, Vector):
            if len(other.values) == len(self.values):
                new_values = []
                for i in self.values:
                    for j in other.values:
                        if self.values.index(i) == other.values.index(j):
                            new_values.append(i * j)
                return Vector(*new_values)
            else:
                return "Умножение векторов разной длины недопустимо"
        else:
            return f"Вектор нельзя Умножить на {other}"
