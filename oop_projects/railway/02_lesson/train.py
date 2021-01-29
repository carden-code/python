from wagon import Wagon
from route import Route


class Train:
    def __init__(self, number, train_type):
        self.__number = number
        self.__train_type = train_type
        self.__wagons = list()
        self.__current_speed = 0
        self.__route = None
        self.__current_station = None

    def __repr__(self):
        return f'Поезд номер - {self.__number}, Тип - {self.__train_type}'

    @property
    def current_station(self):
        return self.__current_station

    @property
    def current_speed(self):
        return self.__current_speed

    @property
    def train_type(self):
        return self.__train_type

    @property
    def number(self):
        return self.__number

    @property
    def wagons(self):
        return self.__wagons

    @property
    def route(self):
        return self.__route

    def speed_up(self):
        self.__current_speed += 1

    def stop(self):
        self.__current_speed = 0

    def attach_wagon(self, wagon):
        if self.__current_speed == 0:
            if isinstance(wagon, Wagon):
                if wagon.wagon_type == self.__train_type:
                    self.__wagons.append(wagon)

    def detach_wagon(self):
        if self.__current_speed and self.__wagons:
            self.__wagons.pop()

    def assign_route(self, route_train):
        if isinstance(route_train, Route):
            self.__route = route_train
            self.__current_station = self.__route.stations[0]

    def forward_movement(self):
        self.__current_station = self.__route.stations[self.__route.stations.index(self.__current_station) + 1]

    def moving_backward(self):
        self.__current_station = self.__route.stations[self.__route.stations.index(self.__current_station) - 1]

    def next_station(self):
        if self.__route.stations.index(self.__current_station) + 1 != self.__route.stations[-1]:
            return self.__route.stations[self.__route.stations.index(self.__current_station) + 1]

    def previous_station(self):
        if self.__current_station != self.__route.stations[0]:
            return self.__route.stations[self.__route.stations.index(self.__current_station) - 1]