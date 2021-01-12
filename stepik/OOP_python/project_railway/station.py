# Класс Station (Станция):
# Имеет название, которое указывается при ее создании
# Может принимать поезда (по одному за раз)
# Может возвращать список всех поездов на станции, находящиеся в текущий момент
# Может возвращать список поездов на станции по типу (см. ниже): кол-во грузовых, пассажирских
# Может отправлять поезда (по одному за раз, при этом, поезд удаляется из списка поездов, находящихся на станции).
class Station:
    def __init__(self, name):
        self.__name = name
        self.__trains = []

    def arrive(self, train):
        self.trains.append(train)

    @property
    def name(self):
        return self.__name

    @property
    def trains(self):
        return self.__trains

    def type_train(self, type):
        pass

    def send_train(self, train):
        self.__trains.remove(train)
