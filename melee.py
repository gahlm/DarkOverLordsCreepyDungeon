import random

class Dice:
    def __init__(self, dice, value):
        self.dice = dice
        self.value = value

    def get_dice(self):
        return random.randrange(1, int(self.value + 1))


d2 = Dice("d2", 2)
d4 = Dice("d4", 4)
d6 = Dice("d6", 6)
d8 = Dice("d8", 8)
d10 = Dice("d10", 10)

dice = [d2, d4, d6, d8, d10]

class Melee:
    def __init__(self, name, dices):
        self.name = name
        self.dices = dices

    def get_atk_damage(self):
        return sum(dice.get_dice() for dice in self.dices)


short_sword = Melee("short sword", [d4, d4, d4, d2])
long_sword = Melee("long sword", [d6, d6])
knife = Melee("knife", [d2, d2, d2, d2, d4])

print(str(long_sword.get_atk_damage()), str(short_sword.get_atk_damage()), str(knife.get_atk_damage()))