class Wagon:
    def __init__(self, wagon_type):
        self.__wagon_type = wagon_type

    def __repr__(self):
        return f"Тип - {self.wagon_type}(id - {str(id(self))[-3:]})"

    @property
    def wagon_type(self):
        return self.__wagon_type
