# Модуль Company содержит методы которые могут
# указывать название компании-производителя и получать его.
class ModuleCompany:
    # Принимает в виде параметра название компании и сохраняет его.
    def __init__(self):
        self.__name_company = None

    # Возвращает название компании.
    @property
    def name_company(self):
        return self.__name_company

    # Принимает название компании и записывает его в атрибут.
    @name_company.setter
    def name_company(self, name):
        self.__name_company = name

