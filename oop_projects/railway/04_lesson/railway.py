from station import Station
from passenger_train import PassengerTrain
from cargo_train import CargoTrain
from passenger_wagon import PassengerTrainCar
from cargo_wagon import CargoTrainCar
from route import Route


# Класс Railway (Железная дорога) может:
#   - Выводить меню.
#   - Создавать станции.
#   - Создавать поезда.
#   - Создавать маршруты и управлять станциями в нем (добавлять, удалять).
#   - Назначать маршрут поезду.
#   - Добавлять вагоны к поезду.
#   - Отцеплять вагоны от поезда.
#   - Перемещать поезд по маршруту вперед и назад.
#   - Просматривать список станций и список поездов на станции.
class Railway:
    __BORDERLINE = '-' * 50

    # Иницилизация объекта. Создаёт атрибуты объекта.
    def __init__(self):
        self.routes = list()
        self.trains = list()
        self.wagons = list()
        self.stations = list()

    # Ввыводит меню (Список действий) в консоль.
    def menu_items(self):
        messages = ['Выберите действие, введя номер из списка: ',
                    self.__BORDERLINE,
                    ' 1 - Создать станцию.',
                    ' 2 - Создать пассажирский поезд.',
                    ' 3 - Создать грузовой поезд.',
                    ' 4 - Создать пассажирский вагон.',
                    ' 5 - Создать грузовой вагон.',
                    ' 6 - Посмотреть список вагонов.',
                    ' 7 - Прицепить вагон к поезду.',
                    ' 8 - Отцепить вагон от поезда.',
                    ' 9 - Создать маршрут.',
                    ' 10 - Добавить промежуточную станцию в маршрут.',
                    ' 11 - Удалить промежуточную станцию из маршрута.',
                    ' 12 - Назначить маршрут поезду.',
                    ' 13 - Переместить поезд по маршруту вперед.',
                    ' 14 - Переместить поезд по маршруту назад.',
                    ' 15 - Посмотреть список станций.',
                    ' 16 - Посмотреть список поездов на станции.',
                    self.__BORDERLINE,
                    '  0 - Для выхода из программы.']

        for item in messages:
            print(item)

    # Статический метод принимает сообщение и печатает его,
    # запрашивает значение у пользователя и возвращает его.
    @staticmethod
    def _data_input(message):
        args = []
        for mess in message:
            print(mess)

        args.append(input())
        return args[0]

    # Принимает список и строку и проверяет есть ли совпадения в списке.
    # Если есть возвращает True если нет False
    @staticmethod
    def _is_duplicate_name(arr, name):
        for elem in arr:
            if elem.name == str(name):
                return True
        return False

    # Принимает экземпляр класса и выводит сообщение с названием класса.
    @staticmethod
    def object_created_successfully(instance):
        print(f'Объект {instance.__class__.__name__} успешно создан.')

    # Принимает экземпляр класса и выводит сообщение об ошибке.
    @staticmethod
    def unsuccessful_object_creation(exception):
        print(f'Ошибка - {exception}')

    # Запрашивает у пользователя название станции и создаёт станцию, добавляет ее в атрибут stations.
    def create_station(self):
        message = ['Введите название станции(Формат: больше 2х букв или цифр.):']
        name = self._data_input(message)

        if name and not self._is_duplicate_name(self.stations, name):
            try:
                station = Station(name)
                self.stations.append(station)
            except ValueError as val:
                self.unsuccessful_object_creation(val)
                return None

    # Запрашивает у пользователя номер поезда и создаёт пассажирский поезд, добавляет его в атрибут trains.
    def create_passenger_train(self):
        message = ['Введите номер поезда(Формат: 123-AA; 123456):']
        number = self._data_input(message)

        if number and not self._is_duplicate_name(self.trains, number):
            try:
                passenger_train = PassengerTrain(number)
                self.trains.append(passenger_train)
                self.object_created_successfully(passenger_train)
            except ValueError as val:
                self.unsuccessful_object_creation(val)

    # Запрашивает у пользователя номер поезда и создаёт грузовой поезд, добавляет его в атрибут trains.
    def create_cargo_train(self):
        message = ['Введите номер поезда(Формат: 123-AA; 123456): ']
        number = self._data_input(message)

        if number and not self._is_duplicate_name(self.trains, number):
            try:
                cargo_train = CargoTrain(number)
                self.trains.append(cargo_train)
            except ValueError as val:
                self.unsuccessful_object_creation(val)

    # Создаёт пассажирский вагон, добавляет его в атрибут wagons.
    def create_passenger_wagon(self):
        self.wagons.append(PassengerTrainCar())

    # Создаёт грузовой вагон, добавляет его в атрибут wagons.
    def create_cargo_wagon(self):
        self.wagons.append(CargoTrainCar())

    # Выводит пронумерованный список созданных вагонов.
    def list_wagons(self):
        for index in range(len(self.wagons)):
            print(f'{index + 1} - {self.wagons[index]}')

    # Принимает сообщение. Выводит пронумерованный список поездов.
    # Запрашивает у пользователя выбор поезда и возвращает его.
    def choose_train(self, message):
        if self.trains:
            for index, train in enumerate(self.trains, 1):
                print(f'{index} - {train}')
            choice = self._data_input(message)
            if choice.isdigit():
                index_train = int(choice) - 1
                if index_train in range(len(self.trains)):
                    return self.trains[index_train]

    # Принимает сообщение. Выводит пронумерованный список станцый.
    # Запрашивает у пользователя выбор станции и возвращает ее.
    def choose_station(self, message):
        if self.stations:
            for index, station in enumerate(self.stations, 1):
                print(f'{index} - {station}')
            choice = self._data_input(message)
            if choice.isdigit():
                index_station = int(choice) - 1
                if index_station in range(len(self.stations)):
                    return self.stations[index_station]

    # Принимает сообщение. Выводит пронумерованный список маршрутов.
    # Запрашивает у пользователя выбор маршрута и возвращает его.
    def choose_route(self, message):
        if self.routes:
            for index, route in enumerate(self.routes, 1):
                print(f'{index} - {route}')
            choice = self._data_input(message)
            if choice.isdigit():
                index_route = int(choice) - 1
                if index_route in range(len(self.routes)):
                    return self.routes[index_route]

    # Прицепляет вагон к поезду. Если есть созданные вагоны.
    # Выбор поезда и если есть вагоны одинакого типа с поездом,
    # добавляет вагон к поезду и удаляет вагон из списка вагонов.
    def attach_wagon(self):
        if self.wagons:
            message = ['Выберете поезд, что бы прицепить вагон. Введите номер: ']
            train = self.choose_train(message)
            if train:
                for wagon in self.wagons:
                    if wagon.wagon_type == train.train_type:
                        train.attach_wagon(wagon)
                        self.wagons.remove(wagon)

    # Отцепляет вагон от поезда.
    # Выбор поезда и если у этого поезда есть вагоны отцепляет вагон и добавляет его в список вагонов.
    def detach_wagon(self):
        if self.trains:
            message = ['Выберете поезд, что бы отцепить вагон. Введите номер: ']
            train = self.choose_train(message)
            if train:
                if train.wagons:
                    wagon = train.detach_wagon()
                    self.wagons.append(wagon)

    # Созздаёт маршрут.
    # Запрашивает у пользователя выбор начальной и конечной станции и создаёт новый маршрут.
    # Добавляет в список маршрутов.
    def create_route(self):
        if len(self.stations) > 1:
            message_first = ['Выберете начальную станцию. Введите номер: ']
            message_finish = ['Выберете конечную станцию. Введите номер: ']
            first_station = self.choose_station(message_first)
            finish_station = self.choose_station(message_finish)
            if first_station and finish_station:
                if first_station != finish_station:
                    route = Route(first_station, finish_station)
                    self.routes.append(route)

    # Добавляет промежуточную станцию в маршрут.
    # Запрашивает выбор маршрута и выбор станции которую нужно добавить и добавляет в маршрут выбранную станцию.
    def add_intermediate_station(self):
        if self.routes:
            message_route = ['Выберете маршрут, в который нужно добавить промежуточную станцию. Введите номер: ']
            message_station = ['Выберете станцию, которую хотите добавить в маршрут. Введите номер: ']
            route = self.choose_route(message_route)
            if route:
                station = self.choose_station(message_station)
                if station:
                    if station not in route.stations:
                        route.add_station(station)

    # Удаляет промежуточную станцию из маршрута.
    # Запрашивает выбор маршрута, выводит список промежуточных станций.
    # Запрашивает выбор промежуточной станции для удаления и удаляет ее
    def del_intermediate_station(self):
        if self.routes:
            message_route = ['Выберете маршрут из которого нужно удалить промежуточную станцию. Введите номер: ']
            message_station = ['Выберете станцию, которую хотите удалить из маршрута. Введите номер: ']
            route = self.choose_route(message_route)
            if route:
                intermediate_stations = route.stations[1:-1]
                if intermediate_stations:
                    for index, station in enumerate(intermediate_stations, 1):
                        print(f'{index} {station}')
                    choice = self._data_input(message_station)
                    if choice.isdigit():
                        index_station = int(choice)
                        if index_station in range(len(route.stations)):
                            station = route.stations[index_station]
                            route.del_station(station)

    # Присваивает маршрут поезду.
    # Запрашивает выбор поезда которому нужно назначить маршрут.
    # Запрашивает выбор маршрута и присваивает выбранный маршрут выбранному поезду.
    def assign_route_train(self):
        if self.routes and self.trains:
            message_train = ['Выберете поезд, которому назначить маршрут. Введите номер: ']
            train = self.choose_train(message_train)
            if train:
                message_route = ['Выберете маршрут, который нужно назначить поезду. Введите номер: ']
                route = self.choose_route(message_route)
                if route:
                    train.assign_route(route)

    # Перемещает поезд по маршруту вперед.
    # Запрашивает у пользователя выбор поезда.
    # Если у поезда есть маршрут перемещает его на следущую станцию в маршруте.
    def move_train_forward(self):
        if self.trains:
            message_train = ['Выберете поезд, который хотите переместить по маршруту вперед. Введите номер: ']
            train = self.choose_train(message_train)
            if train:
                if train.route:
                    train.forward_movement()

    # Перемещает поезд по маршруту назад.
    # Запрашивает у пользователя выбор поезда.
    # Если у поезда есть маршрут перемещает его на предыдущую станцию в маршруте.
    def move_train_back(self):
        if self.trains:
            message_train = ['Выберете поезд, который хотите переместить по маршруту назад. Введите номер: ']
            train = self.choose_train(message_train)
            if train:
                if train.route:
                    train.moving_backward()

    # Печатает список станций.
    def view_station_list(self):
        print(self.stations)

    # Выводит список поездов на станции.
    # Запрашивает у пользователя выбор станции и выводит все поезда на этой станции.
    def view_list_trains_station(self):
        if self.stations:
            message_station = ['Выберете станцию, для просмотра списка поездов. Введите номер: ']
            station = self.choose_station(message_station)
            if station:
                print(station.trains)

    # Содержит методы для управления железной дорогой. Возвращает словарь.
    def dict_methods(self):
        dict_m = {'1': self.create_station, '2': self.create_passenger_train, '3': self.create_cargo_train,
                  '4': self.create_passenger_wagon, '5': self.create_cargo_wagon, '6': self.list_wagons,
                  '7': self.attach_wagon, '8': self.detach_wagon, '9': self.create_route,
                  '10': self.add_intermediate_station, '11': self.del_intermediate_station,
                  '12': self.assign_route_train, '13': self.move_train_forward, '14': self.move_train_back,
                  '15': self.view_station_list, '16': self.view_list_trains_station}
        return dict_m

    # Принимает значение из меню (menu_item) и вызывает соответствующий метод из словаря dict_m.
    def selected(self, menu_item):
        if menu_item:
            print(f"Ваш выбор: {menu_item}")
            dict_m = self.dict_methods()
            try:
                dict_m[menu_item]()
            except KeyError:
                print('Ошибка - Повторите ввод')
