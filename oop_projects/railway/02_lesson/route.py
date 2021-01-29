from station import Station


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
