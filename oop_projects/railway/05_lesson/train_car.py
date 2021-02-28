from module_company import ModuleCompany
from instance_counter import InstanceCounter


# Класс Wagon (Вагон):
#  - Имеет тип(passenger/cargo), эти данные указываются при создании экземпляра класса.
#  - Может возвращать тип вагона.
class TrainCar(ModuleCompany, InstanceCounter):

    #  Иницилизация объекта. Создаёт атрибуты объекта.
    def __init__(self, wagon_type, capacity):
        self.__wagon_type = wagon_type
        self._is_valid(capacity)
        self.capacity = int(capacity)
        self.register_instance()
        self.number_wagon = self.count_instances
        self.occupied = 0

    # Возвращает защищенный атрибут __wagon_type (Тип вагона).
    @property
    def wagon_type(self):
        return self.__wagon_type

    # Возвращает свободное место в вагоне.
    def return_available_seats(self):
        return self.capacity

    # Возвращает занятое место в вагоне.
    def return_occupied_places(self):
        return self.occupied

    # Проверка на положительное число больше 0.
    @staticmethod
    def _validate(capacity):
        if not capacity.isdigit():
            return False
        if int(capacity) > 0:
            return True

    # Проверка объекта на валидность. В случае не валидности выбросит исключение.
    def _is_valid(self, capacity):
        if self._validate(capacity):
            return True
        raise ValueError('Значение может быть только положительнм целым числом!')
