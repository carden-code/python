from module_company import ModuleCompany


# Класс Wagon (Вагон):
#  - Имеет тип(passenger/cargo), эти данные указываются при создании экземпляра класса.
#  - Может возвращать тип вагона.
class TrainCar(ModuleCompany):

    #  Иницилизация объекта. Создаёт атрибуты объекта.
    def __init__(self, wagon_type, capacity):
        self.__wagon_type = wagon_type
        self.capacity = capacity
        self.__is_valid()
        self.occupied = 0

    # Развернутое отображение объекта класса Wagon(отображает тип вагона и id) в консоли.
    def __repr__(self):
        return f"Тип: {self.wagon_type}(id - {str(id(self))[-3:]})"

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
    def __validate(self):
        if self.capacity.isdigit():
            if int(self.capacity) > 0:
                return True
            else:
                return False
        else:
            return False

    # Проверка объекта на валидность. В случае не валидности выбросит исключение.
    def __is_valid(self):
        if self.__validate():
            return True
        else:
            raise ValueError('Значение может быть только положительное цело число!')
