# Модуль Company содержит методы которые могут
# указывать название компании-производителя и получать его.
class ModuleCompany:
    # Принимает в виде параметра название компании и сохраняет его.
    def __init__(self):
        self.name_company = None

    def name_company(self, name):
        self.name_company = name

    # Возвращает название компании.
    def return_company(self):
        return self.name_company
