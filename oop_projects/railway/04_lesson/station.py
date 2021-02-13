from instance_counter import InstanceCounter
from train import Train


# Класс Station (Станция):
#   - Имеет название, которое указывается при ее создании.
#   - Может принимать поезда (по одному за раз).
#   - Может возвращать список всех поездов на станции, находящиеся в текущий момент.
#   - Может возвращать список поездов на станции по типу: кол-во грузовых, пассажирских.
#   - Может отправлять поезда (по одному за раз, при этом, поезд удаляется из списка поездов, находящихся на станции).
class Station(InstanceCounter):
    stations = []

    #  Иницилизация объекта. Создаёт атрибуты объекта.
    def __init__(self, name):
        self.__name = name
        self.__is_valid()
        self.__trains = []
        self.register_instance()
        Station.stations.append(self)

    # Развернутое отображение объекта класса Station(отображает имя станции) в консоли.
    def __repr__(self):
        return f"'Станция - {self.name}'"

    # Возвращает все созданные экземпляры класса
    @classmethod
    def all_station(cls):
        return cls.stations

    # Возвращает защищенный атрибут __name (Название станции).
    @property
    def name(self):
        return self.__name

    # Возвращает защищенный атрибут __trains (Список поездов на станции).
    @property
    def trains(self):
        return self.__trains

    # Принимает поез добавляя объект класса Train в атрибут trains.
    def arrival(self, train):
        if isinstance(train, Train):
            self.trains.append(train)

    # Принимает аргумен (тип поезда) и возвращает список поездов соответствуещего типа.
    def return_trains_by_type(self, train_type):
        trains = [train for train in self.trains if train.train_type == train_type]
        return trains

    # Отправляет поез со станции, удаляя его из атрибута trains.
    def send_train(self, train):
        self.__trains.remove(train)

    # Прверка формата названия станции. Больше 2х букв или цифр.
    def __validate(self):
        if len(self.__name) >= 3 and self.__name.isalnum():
            return True
        else:
            raise ValueError('Название должно быть больше 2х букв или цифр.')

    # Проверка объекта на валидность. В случае не валидности выбросит исключение.
    def __is_valid(self):
        if self.__validate():
            return True
        else:
            return False
