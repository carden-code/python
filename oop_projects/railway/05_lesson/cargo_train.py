from train import Train


# Класс CargoTrain наследут поведение от класса Train и имеет тип при создании (cargo).
class CargoTrain(Train):
    def __init__(self, number):
        super().__init__(number, 'cargo')
