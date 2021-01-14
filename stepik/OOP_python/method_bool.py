# Магический метод
# метод __bool__

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print('call __len__')
        return abs(self.x - self.y)

    def __bool__(self):
        print('call __bool__')
        return self.x != 0 or self.y != 0