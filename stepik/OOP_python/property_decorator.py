class Money:
    def __init__(self, dollars, cents):
        self.total_cents = (dollars * 100) + cents

    def __str__(self):
        dollars = self.total_cents // 100
        cents = self.total_cents % 100
        return f"Ваше состояние составляет {dollars} долларов {cents} центов"

    @property
    def dollars(self):
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, value):
        if isinstance(value, int):
            cents = self.total_cents % 100
            dollars = value * 100
            self.total_cents = dollars + cents
        else:
            print("Error dollars")

    @property
    def cents(self):
        return self.total_cents % 100

    @cents.setter
    def cents(self, value):
        if isinstance(value, int) and value < 100:
            dollars = (self.total_cents // 100) * 100
            cents = value
            self.total_cents = cents + dollars
        else:
            print("Error cents")
