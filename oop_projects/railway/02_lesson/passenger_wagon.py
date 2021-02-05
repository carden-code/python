from wagon import Wagon


# Класс PassengerWagon наследут поведение от класса Wagon и имеет тип при создании (passenger).
class PassengerWagon(Wagon):
    def __init__(self):
        super().__init__('passenger')
