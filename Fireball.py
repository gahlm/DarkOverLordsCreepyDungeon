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


class Spell:
    def __init__(self, name, dices):
        self.name = name
        self.dices = dices

    def get_spell_damage(self):
        return sum(dice.get_dice() for dice in self.dices)


fire = Spell("fire", [d8, d2])
ice = Spell("ice", [d8, d4])
wind = Spell("wind", [d10])

print(str(ice.get_spell_damage()), str(fire.get_spell_damage()), str(wind.get_spell_damage()))

print("Cast Fire! Fireball hits for", str(fire.get_spell_damage()), "damage!")

