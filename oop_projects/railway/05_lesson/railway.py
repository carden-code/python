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
        self.routes = []
        self.trains = []
        self.wagons = []
        self.stations = []

    # Статический метод принимает сообщение и печатает его,
    # запрашивает значение у пользователя и возвращает его.
    @staticmethod
    def __data_input(message):
        args = []
        for mess in message:
            print(mess)

        args.append(input())
        return args[0]

    # Принимает список и строку и проверяет есть ли совпадения в списке.
    # Если есть возвращает True если нет False
    @staticmethod
    def __is_duplicate_name(arr, name):
        for elem in arr:
            if elem.name == str(name):
                return True
        return False

    # Принимает экземпляр класса и выводит сообщение с названием класса.
    @staticmethod
    def __print_object_created_successfully(instance):
        print(f'Объект {instance.__class__.__name__} успешно создан.')

    # Принимает экземпляр класса и выводит сообщение об ошибке.
    @staticmethod
    def __print_unsuccessful(exception):
        print(f'Ошибка - {exception}')

    # Сообщает о успешном совершении действия.
    @staticmethod
    def __print_successfully():
        print('Действие выполнено успешно.')

    # Запрашивает у пользователя название станции и создаёт станцию, добавляет ее в атрибут stations.
    def create_station(self):
        message = ['Введите название станции(Формат: больше 2х букв или цифр.):']
        name = self.__data_input(message)

        if name and not self.__is_duplicate_name(self.stations, name):
            try:
                station = Station(name)
            except ValueError as val:
                self.__print_unsuccessful(val)
            else:
                self.stations.append(station)
                self.__print_object_created_successfully(station)

    # Запрашивает у пользователя номер поезда и создаёт пассажирский поезд, добавляет его в атрибут trains.
    def create_passenger_train(self):
        message = ['Введите номер поезда(Формат: 123-AA; 123456):']
        number = self.__data_input(message)

        if number and not self.__is_duplicate_name(self.trains, number):
            try:
                passenger_train = PassengerTrain(number)
            except ValueError as val:
                self.__print_unsuccessful(val)
            else:
                self.trains.append(passenger_train)
                self.__print_object_created_successfully(passenger_train)

    # Запрашивает у пользователя номер поезда и создаёт грузовой поезд, добавляет его в атрибут trains.
    def create_cargo_train(self):
        message = ['Введите номер поезда(Формат: 123-AA; 123456): ']
        number = self.__data_input(message)

        if number and not self.__is_duplicate_name(self.trains, number):
            try:
                cargo_train = CargoTrain(number)
            except ValueError as val:
                self.__print_unsuccessful(val)
            else:
                self.trains.append(cargo_train)
                self.__print_object_created_successfully(cargo_train)

    # Созздаёт маршрут.
    # Запрашивает у пользователя выбор начальной и конечной станции и создаёт новый маршрут.
    # Добавляет в список маршрутов.
    def create_route(self):
        if len(self.stations) > 1:
            message_first = ['Выберете начальную станцию. Введите номер: ']
            message_finish = ['Выберете конечную станцию. Введите номер: ']
            first_station = self.choose_station(message_first)
            finish_station = self.choose_station(message_finish)
            try:
                route = Route(first_station, finish_station)
            except ValueError as val:
                self.__print_unsuccessful(val)
            except AttributeError as atr:
                self.__print_unsuccessful(atr)
            else:
                self.routes.append(route)
                self.__print_object_created_successfully(route)

    # Создаёт пассажирский вагон, добавляет его в атрибут wagons.
    def create_passenger_wagon(self):
        message = ['Введите колличество мест в вагоне: ']
        capacity = self.__data_input(message)
        try:
            passenger_wagon = PassengerTrainCar(capacity)
        except ValueError as val:
            self.__print_unsuccessful(val)
        else:
            self.wagons.append(passenger_wagon)
            self.__print_object_created_successfully(passenger_wagon)

    # Создаёт грузовой вагон, добавляет его в атрибут wagons.
    def create_cargo_wagon(self):
        message = ['Введите объём вагона: ']
        capacity = self.__data_input(message)
        try:
            cargo_wagon = CargoTrainCar(capacity)
        except ValueError as val:
            self.__print_unsuccessful(val)
        else:
            self.wagons.append(cargo_wagon)
            self.__print_object_created_successfully(cargo_wagon)

    # Принимает сообщение. Выводит пронумерованный список поездов.
    # Запрашивает у пользователя выбор поезда и возвращает его.
    def choose_train(self, message):
        if not self.trains:
            return
        for index, train in enumerate(self.trains, 1):
            print(f'{index} - {train}')
        choice = self.__data_input(message)
        if not choice.isdigit():
            return
        index_train = int(choice) - 1
        if index_train in range(len(self.trains)):
            return self.trains[index_train]

    # Принимает сообщение. Выводит пронумерованный список станцый.
    # Запрашивает у пользователя выбор станции и возвращает ее.
    def choose_station(self, message):
        if not self.stations:
            return
        for index, station in enumerate(self.stations, 1):
            print(f'{index} - {station}')
        choice = self.__data_input(message)
        if not choice.isdigit():
            return
        index_station = int(choice) - 1
        if index_station in range(len(self.stations)):
            return self.stations[index_station]

    # Принимает сообщение. Выводит пронумерованный список маршрутов.
    # Запрашивает у пользователя выбор маршрута и возвращает его.
    def choose_route(self, message):
        if not self.routes:
            return
        for index, route in enumerate(self.routes, 1):
            print(f'{index} - {route}')
        choice = self.__data_input(message)
        if not choice.isdigit():
            return
        index_route = int(choice) - 1
        if index_route in range(len(self.routes)):
            return self.routes[index_route]

    # Выводит список промежуточных станций.
    # Запрашивает выбор пользователя.
    # И возвращает выбранную станцию.
    def choose_intermediate_station(self, route, message):
        intermediate_stations = route.stations[1:-1]
        if not intermediate_stations:
            return
        for index, station in enumerate(intermediate_stations, 1):
            print(f'{index} {station}')
        choice = self.__data_input(message)
        if not choice.isdigit():
            return
        index_station = int(choice)
        if index_station in range(len(route.stations)):
            return route.stations[index_station]

    # Принимает сообщение. Выводит пронумерованный список вагонов.
    # Запрашивает у пользователя выбор вагона и возвращает его.
    def choose_train_car(self, message):
        if not self.wagons:
            return
        for index, wagon in enumerate(self.wagons, 1):
            print(f'{index} {wagon}')
        choice = self.__data_input(message)
        if not choice.isdigit():
            return
        index_wagon = int(choice) - 1
        if index_wagon in range(len(self.wagons)):
            return self.wagons[index_wagon]

    # Прицепляет вагон к поезду. Если есть созданные вагоны.
    # Выбор поезда и если есть вагоны одинакого типа с поездом,
    # добавляет вагон к поезду и удаляет вагон из списка вагонов.
    def attach_wagon(self):
        if not self.wagons:
            return
        message = ['Выберете поезд, что бы прицепить вагон. Введите номер: ']
        train = self.choose_train(message)
        if not train:
            return
        for wagon in self.wagons:
            if wagon.wagon_type == train.train_type:
                train.attach_wagon(wagon)
                self.wagons.remove(wagon)
                self.__print_successfully()

    # Отцепляет вагон от поезда.
    # Выбор поезда и если у этого поезда есть вагоны отцепляет вагон и добавляет его в список вагонов.
    def detach_wagon(self):
        if not self.trains:
            return
        message = ['Выберете поезд, что бы отцепить вагон. Введите номер: ']
        train = self.choose_train(message)
        if not train or not train.wagons:
            return
        wagon = train.detach_wagon()
        self.wagons.append(wagon)
        self.__print_successfully()

    # Добавляет промежуточную станцию в маршрут.
    # Запрашивает выбор маршрута и выбор станции которую нужно добавить и добавляет в маршрут выбранную станцию.
    def add_intermediate_station(self):
        if not self.routes:
            return
        message_route = ['Выберете маршрут, в который нужно добавить промежуточную станцию. Введите номер: ']
        message_station = ['Выберете станцию, которую хотите добавить в маршрут. Введите номер: ']
        route = self.choose_route(message_route)
        if not route:
            return
        station = self.choose_station(message_station)
        if not station:
            return
        try:
            route.add_station(station)
            self.__print_successfully()
        except ValueError as val:
            self.__print_unsuccessful(val)

    # Удаляет промежуточную станцию из маршрута.
    # Запрашивает выбор маршрута, выводит список промежуточных станций.
    # Запрашивает выбор промежуточной станции для удаления и удаляет ее
    def del_intermediate_station(self):
        if not self.routes:
            return
        message_route = ['Выберете маршрут из которого нужно удалить промежуточную станцию. Введите номер: ']
        message_station = ['Выберете станцию, которую хотите удалить из маршрута. Введите номер: ']
        route = self.choose_route(message_route)
        if not route:
            return
        station = self.choose_intermediate_station(route, message_station)
        route.del_station(station)
        self.__print_successfully()

    # Присваивает маршрут поезду.
    # Запрашивает выбор поезда которому нужно назначить маршрут.
    # Запрашивает выбор маршрута и присваивает выбранный маршрут выбранному поезду.
    def assign_route_train(self):
        if not self.routes or not self.trains:
            return
        message_train = ['Выберете поезд, которому назначить маршрут. Введите номер: ']
        train = self.choose_train(message_train)
        if not train:
            return
        message_route = ['Выберете маршрут, который нужно назначить поезду. Введите номер: ']
        route = self.choose_route(message_route)
        if not route:
            return
        train.assign_route(route)
        self.__print_successfully()

    # Перемещает поезд по маршруту вперед.
    # Запрашивает у пользователя выбор поезда.
    # Если у поезда есть маршрут перемещает его на следущую станцию в маршруте.
    def move_train_forward(self):
        if not self.trains:
            return
        message_train = ['Выберете поезд, который хотите переместить по маршруту вперед. Введите номер: ']
        train = self.choose_train(message_train)
        if not train or not train.route:
            return

        try:
            train.forward_movement()
            self.__print_successfully()
        except IndexError as i:
            self.__print_unsuccessful(i)

    # Перемещает поезд по маршруту назад.
    # Запрашивает у пользователя выбор поезда.
    # Если у поезда есть маршрут перемещает его на предыдущую станцию в маршруте.
    def move_train_back(self):
        if not self.trains:
            return
        message = ['Выберете поезд, который хотите переместить по маршруту назад. Введите номер: ']
        train = self.choose_train(message)
        if not train or not train.route:
            return

        try:
            train.moving_backward()
            self.__print_successfully()
        except IndexError as i:
            self.__print_unsuccessful(i)

    # Занять место в вагоне
    def fill_train_car(self):
        if not self.wagons:
            return
        message = ['Выберете вагон, который хотите заполнить. Введите номер: ']
        wagon = self.choose_train_car(message)
        if not wagon:
            return
        if wagon.wagon_type == 'passenger':
            try:
                wagon.occupies_place()
                self.__print_successfully()
            except ValueError as val:
                self.__print_unsuccessful(val)
        else:
            try:
                capacity = input(f'Введите количество объёма на который хотите заполнить вагон.'
                                 f' Доступно {wagon.capacity}: ')
                if capacity.isdigit():
                    wagon.occupies_place(int(capacity))
                    self.__print_successfully()
                else:
                    raise ValueError('Попробуйте снова. Значение должно быть положительным целым числом.')
            except ValueError as val:
                self.__print_unsuccessful(val)

    # Выводит пронумерованный список созданных вагонов.
    def list_wagons(self):
        for index, wagon in enumerate(self.wagons, 1):
            print(f'{index} - {wagon}')

    # Печатает список станций.
    def view_station_list(self):
        print(f'Список станций - {self.stations}')

    # Выводит список поездов на станции.
    # Запрашивает у пользователя выбор станции и выводит все поезда на этой станции.
    def view_list_trains_station(self):
        if not self.stations:
            return
        message = ['Выберете станцию, для просмотра списка поездов. Введите номер: ']
        station = self.choose_station(message)
        if not station:
            return
        for train in enumerate(station.generate_trains(), 1):
            print(*train)

    # Выводит список вагонов у поезда.
    # Запрашивает у пользователя выбор поезда и выводит все вагоны у поезда.
    def view_list_wagons_train(self):
        if not self.trains:
            return
        message = ['Выберете поезд, для просмотра списка вагонов. Введите номер: ']
        train = self.choose_train(message)
        if not train:
            return
        for wagon in enumerate(train.generate_wagons(), 1):
            print(*wagon)

    def __dict_create_methods(self):
        dict_m = {'1': self.create_station, '2': self.create_passenger_train, '3': self.create_cargo_train,
                  '4': self.create_passenger_wagon, '5': self.create_cargo_wagon, '6': self.create_route}
        return dict_m

    def __dict_actions_methods(self):
        dict_m = {'1': self.attach_wagon, '2': self.detach_wagon, '3': self.fill_train_car,
                  '4': self.add_intermediate_station, '5': self.del_intermediate_station,
                  '6': self.assign_route_train, '7': self.move_train_forward, '8': self.move_train_back}
        return dict_m

    def __dict_info_methods(self):
        dict_m = {'1': self.list_wagons, '2': self.view_station_list,
                  '3': self.view_list_trains_station, '4': self. view_list_wagons_train}
        return dict_m

    def main_menu_items(self):
        messages = ['Выберете действие, введя номер из списка.',
                    self.__BORDERLINE,
                    '1 - Создать объект.',
                    '2 - Произвести действие над объектом.',
                    '3 - Информация об объектах.',
                    '0 - Для выхода из программы.']
        for item in messages:
            print(item)

    def create_menu_items(self):
        messages = ['Выберите действие, введя номер из списка: ',
                    self.__BORDERLINE,
                    '1 - Создать станцию.',
                    '2 - Создать пассажирский поезд.',
                    '3 - Создать грузовой поезд.',
                    '4 - Создать пассажирский вагон.',
                    '5 - Создать грузовой вагон.',
                    '6 - Создать маршрут.',
                    self.__BORDERLINE,
                    '0 - Для возврата в предыдущее меню.']
        for item in messages:
            print(item)

    def perform_actions_objects_menu(self):
        messages = ['Выберите действие, введя номер из списка: ',
                    self.__BORDERLINE,
                    '1 - Прицепить вагон к поезду.',
                    '2 - Отцепить вагон от поезда.',
                    '3 - Заполнить вагон.',
                    '4 - Добавить промежуточную станцию в маршрут.',
                    '5 - Удалить промежуточную станцию из маршрута.',
                    '6 - Назначить маршрут поезду.',
                    '7 - Переместить поезд по маршруту вперед.',
                    '8 - Переместить поезд по маршруту назад.',
                    self.__BORDERLINE,
                    '0 - Для возврата в предыдущее меню.']
        for item in messages:
            print(item)

    def view_information_objects_menu(self):
        messages = ['Выберите действие, введя номер из списка: ',
                    self.__BORDERLINE,
                    '1 - Посмотреть список вагонов.',
                    '2 - Посмотреть список станций.',
                    '3 - Посмотреть список поездов на станции.',
                    '4 - Посмотреть список вагонов у поезда.',
                    self.__BORDERLINE,
                    '0 - Для возврата в предыдущее меню.']
        for item in messages:
            print(item)

    # Принимает значение из меню (menu_item) и вызывает соответствующий метод из словаря dict_m.
    def selected(self, menu_item, number_menu):
        if not menu_item:
            return
        print(f"Ваш выбор: {menu_item}")
        dict_m = None
        if number_menu == '1':
            dict_m = self.__dict_create_methods()
        elif number_menu == '2':
            dict_m = self.__dict_actions_methods()
        elif number_menu == '3':
            dict_m = self.__dict_info_methods()

        try:
            dict_m[menu_item]()
        except KeyError:
            print('Ошибка - Повторите ввод')
