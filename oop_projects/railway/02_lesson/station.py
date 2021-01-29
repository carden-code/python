from train import Train


class Station:
    def __init__(self, name):
        self.__name = name
        self.__trains = list()

    def __repr__(self):
        return f'Название станции - {self.name}'

    @property
    def name(self):
        return self.__name

    @property
    def trains(self):
        return self.__trains

    def arrival(self, train):
        if isinstance(train, Train):
            self.trains.append(train)

    def train_type(self, train_type):
        trains = []
        for train in self.__trains:
            if train.train_type == train_type:
                trains.append(train)
        return trains

    def send_train(self, train):
        self.__trains.remove(train)
