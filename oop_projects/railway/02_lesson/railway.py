from station import Station


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
    def data_input(message):
        args = []
        for mess in message:
            print(mess)

        args.append(input())

    @staticmethod
    def is_dublicate_name(arr, name):
        for elem in arr:
            if elem.name == str(name):
                return False
        return True

    def create_station(self):
        message = ['Введите название станции:']
        name = self.data_input(message)

        if name != '' and not self.is_dublicate_name(self.stations, name):
            self.stations.append(Station(name))
