# Класс Station (Станция):
# Имеет название, которое указывается при ее создании
# Может принимать поезда (по одному за раз)
# Может возвращать список всех поездов на станции, находящиеся в текущий момент
# Может возвращать список поездов на станции по типу (см. ниже): кол-во грузовых, пассажирских
# Может отправлять поезда (по одному за раз, при этом, поезд удаляется из списка поездов, находящихся на станции).
class Station:
    def __init__(self, name):
        self.name = name
        self.list_train = []

    def train_arrival(self, train):
        self.list_train.append(train)

    def list_train(self):
        return self.list_train

    def type_train(self, type):
        pass

    def send_train(self, train):
        for t in self.list_train:
            if t == train:
                self.list_train.remove(train)
