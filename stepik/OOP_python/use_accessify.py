from accessify import protected


class Car:

    @protected
    def start_engine(self):
        return "Engine's sound."

    def run(self):
        return self.start_engine()


if __name__ == '__main__':
    car = Car()

    assert "Engine's sound." == car.run()

    car.start_engine()
