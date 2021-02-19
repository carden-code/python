class InstanceCounter:
    count_instances = 0

    # Возвращает колличество созданных объектов.
    @classmethod
    def instances(cls):
        return cls.count_instances

    # Увеличевает счётчик созданных объектов.
    def register_instance(self):
        self.__class__.count_instances += 1
