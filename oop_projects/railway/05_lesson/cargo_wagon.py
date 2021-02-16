from train_car import TrainCar


# Класс CargoWagon наследут поведение от класса Wagon и имеет тип при создании (cargo).
class CargoTrainCar(TrainCar):
    def __init__(self, capacity):
        super().__init__('cargo', capacity)

    def occupies_place(self, value):
        if self.capacity >= value:
            self.capacity -= value
            self.occupied += value
        else:
            raise ValueError(f'Не достаточно места. Вместимость вагона {self.capacity}')
