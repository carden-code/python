from train_car import TrainCar


# Класс CargoWagon наследут поведение от класса Wagon и имеет тип при создании (cargo).
class CargoTrainCar(TrainCar):
    def __init__(self, capacity):
        super().__init__('cargo', capacity)

    # Развернутое отображение объекта класса CargoTrainCar в консоли.
    def __repr__(self):
        return f" Номер: {self.number_wagon}" \
               f" (id - {str(id(self))[-3:]})" \
               f" Тип: {self.wagon_type}" \
               f" Свободное место: {self.capacity}," \
               f" Занятый объём: {self.occupied}"

    # Заполняет вагон.
    def occupies_place(self, value):
        if self.capacity >= value:
            self.capacity -= value
            self.occupied += value
        else:
            raise ValueError(f'Не достаточно места. Вместимость вагона {self.capacity}')
