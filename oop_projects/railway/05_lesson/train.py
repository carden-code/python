from module_company import ModuleCompany
from train_car import TrainCar
from route import Route
from instance_counter import InstanceCounter


# Класс Train (Поезд):
#  - Имеет номер (произвольная строка) и тип (грузовой, пассажирский) и количество вагонов,
#       эти данные указываются при создании экземпляра класса.
#  - Может набирать скорость.
#  - Может возвращать текущую скорость.
#  - Может тормозить (сбрасывать скорость до нуля).
#  - Может возвращать количество вагонов.
#  - Может прицеплять/отцеплять вагоны (по одному вагону за операцию,
#       метод просто увеличивает или уменьшает количество вагонов).
#       Прицепка/отцепка вагонов может осуществляться только если поезд не движется.
#  - Может принимать маршрут следования (объект класса Route).
#  - При назначении маршрута поезду, поезд автоматически помещается на первую станцию в маршруте.
#  - Может перемещаться между станциями, указанными в маршруте.
#       Перемещение возможно вперед и назад, но только на 1 станцию за раз.
# - Возвращать предыдущую станцию, текущую, следующую, на основе маршрута
class Train(ModuleCompany, InstanceCounter):
    trains = {}

    # Иницилизация объекта. Создаёт атрибуты объекта.
    def __init__(self, number, train_type):
        self.__name = number
        self._is_valid()
        self.__train_type = train_type
        self.__wagons = []
        self.__current_speed = 0
        self.__route = None
        self.__current_station = None
        self.register_instance()
        Train.trains[number] = self

    # Развернутое отображение объекта класса Train в консоли.
    def __repr__(self):
        if isinstance(self.__route, Route):
            return f"'number: {self.name} " \
                   f"type: {self.train_type} " \
                   f"wagons: {len(self.wagons)} " \
                   f"route_id: {str(id(self.route))[-3:]} " \
                   f"current_station: {self.current_station.name}'"
        return f"'number: {self.name} " \
               f"type: {self.train_type} " \
               f"wagons: {len(self.wagons)}'"

    # Метод класса find, который принимает номер поезда (указанный при его создании)
    # и возвращает объект поезда по номеру или None, если поезд с таким номером не найден.
    @classmethod
    def find(cls, number):
        try:
            return cls.trains[number]
        except KeyError:
            return None

    # Возвращает защищенный атрибут __current_station (Текущая станция).
    @property
    def current_station(self):
        return self.__current_station

    # Возвращает защищенный атрибут __current_speed (Текущая скорость поезда).
    @property
    def current_speed(self):
        return self.__current_speed

    # Возвращает защищенный атрибут __train_type (Тип поезда - (passenger/cargo)).
    @property
    def train_type(self):
        return self.__train_type

    # Возвращает защищенный атрибут __name (Номер поезда).
    @property
    def name(self):
        return self.__name

    # Возвращает защищенный атрибут __wagons (Список вагонов).
    @property
    def wagons(self):
        return self.__wagons

    # Возвращает защищенный атрибут __route (Маршрут).
    @property
    def route(self):
        return self.__route

    # Увеличивает текущую скорость на 1 при каждом выызове.
    def speed_up(self):
        self.__current_speed += 1

    # Останавливает поезд.
    def stop(self):
        self.__current_speed = 0

    # Прицеплет вагон к поезду если поезд стоит и типы совпадают.
    def attach_wagon(self, wagon):
        if self.__current_speed == 0:
            if isinstance(wagon, TrainCar):
                if wagon.wagon_type == self.train_type:
                    self.__wagons.append(wagon)

    # Отцепляет вагон от поезда и возвращает этот вагон.
    def detach_wagon(self):
        if self.__current_speed == 0 and self.__wagons:
            return self.__wagons.pop()

    # Назначает маршрут поезду и помещает поезд на первую станцию в маршруте.
    def assign_route(self, route_train):
        if isinstance(route_train, Route):
            self.__route = route_train
            self.__current_station = self.route.stations[0]
            self.current_station.arrival(self)

    # Перемещает поезд вперед по маршруту, отправляя с текущей станции поезд на следущую.
    def forward_movement(self):
        if self.current_station != self.route.stations[-1]:
            self.current_station.send_train(self)
            self.__current_station = self.next_station()
            self.current_station.arrival(self)
        else:
            raise IndexError('Перемещение вперед не возможно. Поезд находится на конечной станции.')

    # Перемещает поезд назад по маршруту, отправляя поезд с текущей станции на предыдущую.
    def moving_backward(self):
        if self.current_station != self.route.stations[0]:
            self.current_station.send_train(self)
            self.__current_station = self.previous_station()
            self.current_station.arrival(self)
        else:
            raise IndexError('Перемещение назад не возможно. Поезд находится на начальной станции.')

    # Возвращает индекс текущей станции в маршруте.
    def index_current_station(self):
        return self.route.stations.index(self.current_station)

    # Возвращает следущую станцию в маршруте.
    def next_station(self):
        if self.index_current_station() + 1 < len(self.route.stations):
            return self.route.stations[self.index_current_station() + 1]

    # Возвращает предыдущую станцию в маршруте.
    def previous_station(self):
        if self.current_station != self.route.stations[0]:
            return self.route.stations[self.index_current_station() - 1]

    def generate_wagons(self):
        for wagon in self.wagons:
            yield wagon

    # Проверка формата номера поезда.
    # Допустимый формат: три буквы или цифры в любом порядке,
    # необязательный дефис (может быть, а может нет) и еще 2 буквы или цифры после дефиса.
    def _validate(self):
        if len(self.__name) not in [5, 6]:
            return False
        if not self.__name[:3].isalnum():
            return False
        if self.__name[3:4] == '-' and self.__name[4:].isalnum():
            return True
        if self.__name[3:].isalnum():
            return True

    # Проверка объекта на валидность. В случае не валидности выбросит исключение.
    def _is_valid(self):
        if self._validate():
            return True
        raise ValueError('Не верный формат номера поезда!')


