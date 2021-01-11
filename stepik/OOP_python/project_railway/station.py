# Класс Station (Станция):
# Имеет название, которое указывается при ее создании
# Может принимать поезда (по одному за раз)
# Может возвращать список всех поездов на станции, находящиеся в текущий момент
# Может возвращать список поездов на станции по типу (см. ниже): кол-во грузовых, пассажирских
# Может отправлять поезда (по одному за раз, при этом, поезд удаляется из списка поездов, находящихся на станции).
class Station:
    def __init__(self, name):
        self.name = name
        self.trains = []

    def arrive(self, train):
        self.trains.append(train)

    def list_train(self):
        return self.trains

    def type_train(self, type):
        pass

    def send_train(self, train):
        self.trains.remove(train)
