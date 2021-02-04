from station import Station
from passenger_train import PassengerTrain
from cargo_train import CargoTrain
from passenger_wagon import PassengerWagon
from cargo_wagon import CargoWagon
from route import Route


class Railway:
    BORDERLINE = '-' * 50

    def __init__(self):
        self.routes = list()
        self.trains = list()
        self.wagons = list()
        self.stations = list()

    @staticmethod
    def menu_items():
        messages = ['Выберите действие, введя номер из списка: ',
                    Railway.BORDERLINE,
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
                    Railway.BORDERLINE,
                    '  0 - Для выхода из программы.']

        for item in messages:
            print(item)

    @staticmethod
    def _data_input(message):
        args = []
        for mess in message:
            print(mess)

        args.append(input())
        return args[0]

    @staticmethod
    def _is_duplicate_name(arr, name):
        for elem in arr:
            if elem.name == str(name):
                return True
        return False

    def create_station(self):
        message = ['Введите название станции:']
        name = self._data_input(message)

        if name and not self._is_duplicate_name(self.stations, name):
            self.stations.append(Station(name))

    def create_passenger_train(self):
        message = ['Введите номер поезда:']
        number = self._data_input(message)

        if number and not self._is_duplicate_name(self.trains, number):
            self.trains.append(PassengerTrain(number))

    def create_cargo_train(self):
        message = ['Введите номер поезда: ']
        number = self._data_input(message)

        if number and not self._is_duplicate_name(self.trains, number):
            self.trains.append(CargoTrain(number))

    def create_passenger_wagon(self):
        self.wagons.append(PassengerWagon())

    def create_cargo_wagon(self):
        self.wagons.append(CargoWagon())

    def list_wagons(self):
        for index in range(len(self.wagons)):
            print(f'{index + 1} - {self.wagons[index]}')

    def choose_train(self, message):
        if self.trains:
            for index in range(len(self.trains)):
                print(f'{index + 1} - {self.trains[index]}')
            choice = int(self._data_input(message))
            index_train = choice - 1
            if index_train in range(len(self.trains)):
                return self.trains[index_train]

    def choose_station(self, message):
        if self.stations:
            for index in range(len(self.stations)):
                print(f'{index + 1} - {self.stations[index]}')
            choice = int(self._data_input(message))
            index_station = choice - 1
            if index_station in range(len(self.stations)):
                return self.stations[index_station]

    def attach_wagon(self):
        if self.wagons:
            message = ['Выберете поезд, что бы прицепить вагон. Введите номер: ']
            train = self.choose_train(message)
            if train:
                for wagon in self.wagons:
                    if wagon.wagon_type == train.train_type:
                        train.attach_wagon(wagon)
                        self.wagons.remove(wagon)

    def detach_wagon(self):
        if self.trains:
            message = ['Выберете поезд, что бы отцепить вагон. Введите номер: ']
            train = self.choose_train(message)
            if train:
                if train.wagons:
                    wagon = train.detach_wagon()
                    self.wagons.append(wagon)

    def create_route(self):
        if len(self.stations) > 1:
            message_first = ['Выберете начальную станцию. Введите номер: ']
            message_finish = ['Выберете конечную станцию. Введите номер: ']
            first_station = self.choose_station(message_first)
            finish_station = self.choose_station(message_finish)
            if first_station and finish_station:
                if finish_station != finish_station:
                    route = Route(first_station, finish_station)
                    self.routes.append(route)

    # def assign_route_train(self):
    #     message_train = ['Выберете поезд, которому назначить маршрут. Введите номер: ']
    #     train = self.choose_train(message_train)
    #
    #     train.assign_route(route)

    def selected(self, menu_item):
        if menu_item:
            print(f"Ваш выбор: {menu_item}")

        if menu_item == '1':
            self.create_station()
        elif menu_item == '2':
            self.create_passenger_train()
        elif menu_item == '3':
            self.create_cargo_train()
        elif menu_item == '4':
            self.create_passenger_wagon()
        elif menu_item == '5':
            self.create_cargo_wagon()
        elif menu_item == '6':
            self.list_wagons()
        elif menu_item == '7':
            self.attach_wagon()
        elif menu_item == '8':
            self.detach_wagon()
        elif menu_item == '9':
            self.create_route()

        else:
            print('Повторите ввод')
