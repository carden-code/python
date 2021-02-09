from train_car import TrainCar


# Класс PassengerWagon наследут поведение от класса Wagon и имеет тип при создании (passenger).
class PassengerTrainCar(TrainCar):
    def __init__(self):
        super().__init__('passenger')
