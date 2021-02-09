from instance_counter import InstanceCounter


# Класс Route (Маршрут):
#   - Имеет начальную и конечную станцию, а также список промежуточных станций.
#       Начальная и конечная станции указываютсся при создании маршрута, а промежуточные могут добавляться между ними.
#   - Может добавлять промежуточную станцию в список.
#   - Может удалять промежуточную станцию из списка.
#   - Может выводить список всех станций по-порядку от начальной до конечной.
class Route(InstanceCounter):
    #  Иницилизация объекта. Создаёт атрибуты объекта.
    def __init__(self, first_station, finish_station):
        self.__stations = [first_station, finish_station]
        self.register_instance()

    # Развернутое отображение объекта класса Route(отображает станции в маршруте и id) в консоли.
    def __repr__(self):
        return f'Маршрут - {self.stations}(id:{str(id(self))[-3:]})'

    # Возвращает защищенный атрибут __stations (Список станций).
    @property
    def stations(self):
        return self.__stations

    # Добавляет уникальную промежуточную станцию в маршрут.
    def add_station(self, station):
        if station not in self.stations:
            self.__stations.insert(-1, station)

    # Удаляет промежуточную станцию из маршрута.
    def del_station(self, station):
        if station != self.__stations[0] and station != self.__stations[-1]:
            self.__stations.remove(station)
