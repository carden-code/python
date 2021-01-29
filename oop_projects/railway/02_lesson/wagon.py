class Wagon:
    def __init__(self, wagon_type):
        self.__wagon_type = wagon_type

    @property
    def wagon_type(self):
        return self.__wagon_type
