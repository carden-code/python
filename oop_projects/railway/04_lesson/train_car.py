from module_company import ModuleCompany


# Класс Wagon (Вагон):
#  - Имеет тип(passenger/cargo), эти данные указываются при создании экземпляра класса.
#  - Может возвращать тип вагона.
class TrainCar(ModuleCompany):

    #  Иницилизация объекта. Создаёт атрибуты объекта.
    def __init__(self, wagon_type):
        self.__wagon_type = wagon_type

    # Развернутое отображение объекта класса Wagon(отображает тип вагона и id) в консоли.
    def __repr__(self):
        return f"Тип: {self.wagon_type}(id - {str(id(self))[-3:]})"

    # Возвращает защищенный атрибут __wagon_type (Тип вагона).
    @property
    def wagon_type(self):
        return self.__wagon_type
