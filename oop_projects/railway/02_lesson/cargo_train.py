from train import Train


class CargoTrain(Train):
    def __init__(self, number):
        super().__init__(number, 'cargo')
