from train import Train


class PassengerTrain(Train):
    def __init__(self, number):
        super().__init__(number, 'passenger')
