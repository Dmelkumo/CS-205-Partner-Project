import random


class Pokemon:
    # Class var for all pokemon to share, this is the type effectiveness
    type_chart = [
        [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, .5, 2, 1, .5, .5, 1, 1, 2, 1, 1, .5, 2, 1, 1, 1, .5, .5, 1],
        [1, .5, .5, 2, 2, .5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, .5, 1, 1],
        [1, 1, 1, .5, 1, 1, 1, 1, 2, .5, 1, 1, 1, 1, 1, 1, .5, 1, 1],
        [1, 2, .5, .5, .5, 2, 1, 2, .5, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 1, 1, 1, .5, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, .5, .5, 1, 1, .5, 1, 2, 1],
        [1, 1, 1, 1, .5, 1, .5, .5, 2, 1, 2, .5, 1, 1, 1, 1, 1, .5, 1],
        [1, 1, 2, 0, 2, 2, 1, .5, 1, 1, 1, 1, .5, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 2, .5, 2, .5, 1, 0, 1, 1, .5, 2, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, .5, 1, 1, 1, .5, 2, 1, 2, 1, 2, 1, 1, 1],
        [1, 2, 1, 1, .5, 1, .5, 1, .5, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1],
        [.5, .5, 2, 1, 2, 1, 2, .5, 2, .5, 1, 1, 1, 1, 1, 1, 2, 1, 1],
        [0, 1, 1, 1, 1, 1, 0, .5, 1, 1, 1, .5, 1, 2, 1, 2, 1, 1, 1],
        [1, .5, .5, .5, .5, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1],
        [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 0, 2, 1, .5, 1, .5, 1, 2, 1],
        [.5, 2, 1, 1, .5, .5, 2, 0, 2, .5, .5, .5, .5, 1, .5, 1, .5, .5, 1],
        [1, 1, 1, 1, 1, 1, .5, 2, 1, 1, 1, .5, 1, 1, 0, .5, 2, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    # Initializer
    def __init__(self, name, type1, type2, hp, atk, spd):
        # Variables
        self.name = name
        self.primary_type = type1
        self.secondary_type = type2
        self.hp = hp
        self.atk = atk
        self.spd = spd

    # Getters
    def get_name(self):
        return self.name

    def get_primary_type(self):
        return self.primary_type

    def get_secondary_type(self):
        return self.secondary_type

    def get_hp(self):
        return self.hp

    def get_atk(self):
        return self.atk

    def get_spd(self):
        return self.spd

    # Setters
    def set_name(self, name):
        self.name = name

    def set_primary_type(self, primary_type):
        self.primary_type = primary_type

    def set_secondary_type(self, secondary_type):
        self.secondary_type = secondary_type

    def set_hp(self, hp):
        self.hp = hp

    def set_atk(self, atk):
        self.atk = atk

    def set_spd(self, spd):
        self.spd = spd

    # Fighting methods
    def attack(self):
        return int(random.randint(1, 10) * self.atk)

    def take_damage(self, damage, other_type, detailed_output):
        effectiveness = self.type_chart[other_type][self.primary_type] * self.type_chart[other_type][self.secondary_type]
        if detailed_output:
            print("It deals " + str(int(damage * effectiveness)) + " damage!")
        if int(damage * effectiveness) >= self.get_hp():
            self.set_hp(0)
        else:
            self.set_hp(self.hp - int(damage * effectiveness))