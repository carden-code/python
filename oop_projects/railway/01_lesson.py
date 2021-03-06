# Требуется написать следующие классы:
#
# Класс Station (Станция):
# Имеет название, которое указывается при ее создании
# Может принимать поезда (по одному за раз)
# Может возвращать список всех поездов на станции, находящиеся в текущий момент
# Может возвращать список поездов на станции по типу (см. ниже): кол-во грузовых, пассажирских
# Может отправлять поезда (по одному за раз, при этом, поезд удаляется из списка поездов, находящихся на станции).
#
# Класс Route (Маршрут):
# Имеет начальную и конечную станцию, а также список промежуточных станций.
# Начальная и конечная станции указываютсся при создании маршрута, а промежуточные могут добавляться между ними.
# Может добавлять промежуточную станцию в список
# Может удалять промежуточную станцию из списка
# Может выводить список всех станций по-порядку от начальной до конечной
#
# Класс Train (Поезд):
# Имеет номер (произвольная строка) и тип (грузовой, пассажирский) и количество вагонов,
# эти данные указываются при создании экземпляра класса
# Может набирать скорость
# Может возвращать текущую скорость
# Может тормозить (сбрасывать скорость до нуля)
# Может возвращать количество вагонов
# Может прицеплять/отцеплять вагоны (по одному вагону за операцию,
# метод просто увеличивает или уменьшает количество вагонов).
# Прицепка/отцепка вагонов может осуществляться только если поезд не движется.
# Может принимать маршрут следования (объект класса Route).
# При назначении маршрута поезду, поезд автоматически помещается на первую станцию в маршруте.
# Может перемещаться между станциями, указанными в маршруте.
# Перемещение возможно вперед и назад, но только на 1 станцию за раз.
# Возвращать предыдущую станцию, текущую, следующую, на основе маршрута


class Station:
    def __init__(self, name):
        self.__name = name
        self.__trains = list()

    @property
    def name(self):
        return self.__name

    @property
    def trains(self):
        return self.__trains

    def arrival(self, train):
        if isinstance(train, Train):
            self.trains.append(train)

    def train_type(self, train_type):
        trains = []
        for train in self.__trains:
            if train.train_type == train_type:
                trains.append(train)
        return trains

    def send_train(self, train):
        self.__trains.remove(train)


class Route:
    def __init__(self, first_station, finish_station):
        self.__stations = [first_station, finish_station]

    @property
    def stations(self):
        return self.__stations

    def add_station(self, station):
        if isinstance(station, Station):
            self.__stations.insert(-1, station)

    def del_station(self, station):
        if isinstance(station, Station) and station != self.__stations[0] and station != self.__stations[-1]:
            self.__stations.remove(station)


class Train:
    def __init__(self, number, train_type, wagons):
        self.number = number
        self.train_type = train_type
        self.__wagons = wagons
        self.__current_speed = 0
        self.__route = None
        self.__current_station = None

    @property
    def current_speed(self):
        return self.__current_speed

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

    def attach_wagon(self):
        if self.__current_speed == 0:
            self.__wagons += 1

    def detach_wagon(self):
        if self.__current_speed and self.__wagons:
            self.__wagons -= 1

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
