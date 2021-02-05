from train import Train


# Класс PassengerTrain наследут поведение от класса Train и имеет тип при создании (passenger).
class PassengerTrain(Train):
    def __init__(self, number):
        super().__init__(number, 'passenger')
