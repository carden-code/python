from train_car import TrainCar


# Класс CargoWagon наследут поведение от класса Wagon и имеет тип при создании (cargo).
class CargoTrainCar(TrainCar):
    def __init__(self):
        super().__init__('cargo')
