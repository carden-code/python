from train_car import TrainCar


# Класс PassengerWagon наследут поведение от класса Wagon и имеет тип при создании (passenger).
class PassengerTrainCar(TrainCar):
    def __init__(self, capacity):
        super().__init__('passenger', capacity)

    # Развернутое отображение объекта класса PassengerTrainCar в консоли.
    def __repr__(self):
        return f" Номер: {self.number_wagon}" \
               f" (id - {str(id(self))[-3:]})" \
               f" Тип: {self.wagon_type}" \
               f" Свободных мест: {self.capacity}," \
               f" Занятых мест: {self.occupied}"

    def occupies_place(self):
        if self.capacity:
            self.capacity -= 1
            self.occupied += 1
        else:
            raise ValueError(f'Не достаточно места. Вместимость вагона {self.capacity}')
