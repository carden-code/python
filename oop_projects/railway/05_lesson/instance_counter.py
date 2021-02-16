class InstanceCounter:
    __count_instances = 0

    # Возвращает колличество созданных объектов.
    @classmethod
    def instances(cls):
        return cls.__count_instances

    # Увеличевает счётчик созданных объектов.
    def register_instance(self):
        self.__class__.__count_instances += 1
