import random

class Dice:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def get_dice(self):
        return random.randrange(1, int(self.value + 1))


d2 = Dice("d2", 2)
d4 = Dice("d4", 4)
d6 = Dice("d6", 6)
d8 = Dice("d8", 8)
d10 = Dice("d10", 10)

dice = [d2, d4, d6, d8, d10]

