from wagon import Wagon


# Класс CargoWagon наследут поведение от класса Wagon и имеет тип при создании (cargo).
class CargoWagon(Wagon):
    def __init__(self):
        super().__init__('cargo')
