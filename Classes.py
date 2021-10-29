# File for the classes in this program
from enum import IntEnum, Enum
import random


class Type(IntEnum):
    NORMAL = 0
    FIRE = 1
    WATER = 2
    ELECTRIC = 3
    GRASS = 4
    ICE = 5
    FIGHTING = 6
    POISON = 7
    GROUND = 8
    FLYING = 9
    PSYCHIC = 10
    BUG = 11
    ROCK = 12
    GHOST = 13
    DRAGON = 14
    DARK = 15
    STEEL = 16
    FAIRY = 17
    NONE = 18


class Pokeball(IntEnum):
    POKEBALL = 10
    GREATBALL = 20
    ULTRABALL = 30
    MASTERBALL = 100


class Badge(Enum):
    DAVIDCITY = 0
    SEANTOWN = 1
    SOMEWHERE = 2


class Pokemon:
    # Class var for all pokemon to share
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
    def __init__(self, name, type1, type2, hp):
        # Variables
        self.name = name
        self.primary_type = type1
        self.secondary_type = type2
        self.hp = hp

    # Getters
    def get_name(self):
        return self.name

    def get_primary_type(self):
        return self.primary_type

    def get_secondary_type(self):
        return self.secondary_type

    def get_hp(self):
        return self.hp

    # Setters
    def set_name(self, name):
        self.name = name

    def set_primary_type(self, primary_type):
        self.primary_type = primary_type

    def set_secondary_type(self, secondary_type):
        self.secondary_type = secondary_type

    def set_hp(self, hp):
        self.hp = hp

    # Fighting methods
    def attack(self):
        return random.randint(1, 10)

    def take_damage(self, damage, other_type):
        effectiveness = self.type_chart[other_type][self.primary_type] * self.type_chart[other_type][self.secondary_type]
        if damage * effectiveness >= self.get_hp():
            self.set_hp(0)
        print("It deals " + str(damage * effectiveness) + " damage!")
        self.set_hp(self.hp - (damage * effectiveness))


class Trainer:

    def __init__(self, name, age, pokemon, pokeballs, badges, is_leader):
        # Variables
        self.name = name
        self.age = age
        self.pokemon = pokemon
        self.pokeballs = pokeballs
        self.badges = badges
        self.is_gym_leader = is_leader

    # Getters
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_pokemon(self):
        return self.pokemon

    def get_pokeballs(self):
        return self.pokeballs

    def get_badges(self):
        return self.badges

    def get_is_gym_leader(self):
        return self.is_gym_leader

    # Setters
    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_pokemon(self, pokemon):
        self.pokemon = pokemon

    def set_pokeballs(self, pokeballs):
        self.pokeballs = pokeballs

    def set_badges(self, badges):
        self.badges = badges

    def set_is_gym_leader(self, is_leader):
        self.is_gym_leader = is_leader

    # Other
    def catch(self, pokemon, pokeball):
        # Get a random number 0 - 100
        catch_rate = random.randint(0, 100)
        # Add in the ball type
        catch_rate += pokeball
        print(self.name + " tries to throw a ball!")

        # Try to catch it
        if catch_rate >= 100:
            print(self.name + " Successfully caught " + pokemon.get_name() + "!")
            self.add_pokemon(pokemon)
            return pokemon
        else:
            print(pokemon.get_name() + " fled!")
            return None

    def add_pokemon(self, pokemon):
        # Simple list append
        self.pokemon.append(pokemon)


class Gym:
    def __init__(self, name, badge, trainers):
        self.name = name
        self.badge = badge
        self.trainers = trainers

    # Getters

    # Setters

    # Battle
    def battle(self, trainer1, trainer2):
        # Create two lists of pokemon from the trainers (so any works)
        # Initialize the attacks
        attack1 = Type.NONE
        attack2 = Type.NONE
        i, j = 0, 0
        # While they still have pokemon
        while any(pokemon.get_hp() > 0 for pokemon in trainer1.pokemon) and any(pokemon.get_hp() > 0 for pokemon in trainer2.pokemon):
            # Print current hp's
            print("")
            print(trainer1.pokemon[i].get_name() + "'s hp: " + str(trainer1.pokemon[i].get_hp()))
            print(trainer2.pokemon[j].get_name() + "'s hp: " + str(trainer2.pokemon[j].get_hp()))

            # Perform the attacks
            attack1 = trainer1.pokemon[i].attack()
            attack2 = trainer2.pokemon[j].attack()
            # Randomize who gets hit first
            if random.randint(0, 1) == 1:
                print(trainer2.pokemon[j].get_name() + " attacks " + trainer1.pokemon[i].get_name())
                trainer1.pokemon[i].take_damage(attack2, trainer2.pokemon[j].get_primary_type())
                print(trainer1.pokemon[i].get_name() + " attacks " + trainer2.pokemon[j].get_name())
                trainer2.pokemon[j].take_damage(attack1, trainer1.pokemon[i].get_primary_type())
            else:
                print(trainer1.pokemon[i].get_name() + " attacks " + trainer2.pokemon[j].get_name())
                trainer2.pokemon[j].take_damage(attack1, trainer1.pokemon[i].get_primary_type())
                print(trainer2.pokemon[j].get_name() + " attacks " + trainer1.pokemon[i].get_name())
                trainer1.pokemon[i].take_damage(attack2, trainer2.pokemon[j].get_primary_type())

            # Check if trainer1's pokemon has died and they have more
            if trainer1.pokemon[i].get_hp() <= 0:
                print(trainer1.pokemon[i].get_name() + " has fainted!")
                # Pick the next pokemon
                if i < len(trainer1.get_pokemon()) - 1:
                    i += 1
            # Check if trainer2's pokemon has died and they have more
            if trainer2.pokemon[j].get_hp() <= 0:
                print(trainer2.pokemon[j].get_name() + " has fainted!")
                # Pick the next pokemon
                if j < len(trainer2.get_pokemon()) - 1:
                    j += 1

        # Check who won
        if any(pokemon.get_hp() > 0 for pokemon in trainer1.pokemon):
            print(trainer1.get_name() + " won!")
            # If the loser was a gym leader, award a badge to the winner
            if trainer2.get_is_gym_leader:
                trainer1.badges.append(self.badge)  # This is bad, directly accesses the data, sean pls fix
            return trainer1
        else:
            print(trainer2.get_name() + " won!")
            return trainer2


def main():
    # Create some pokemon and trainers
    cool_pokemon = Pokemon("Darkrai", Type.DARK, Type.NONE, 100)
    pokemon1 = []
    for x in range(3):
        pokemon1.append(Pokemon("Pika" + str(x), Type.FIRE + x, Type.FIGHTING + x, 100))

    pokemon2 = []
    for x in range(3):
        pokemon2.append(Pokemon("Ditto" + str(x), Type.NORMAL + x, Type.GHOST + x, 100))

    trainers = []
    """
    for x in range(2):
        trainers.append(Trainer("Jeff" + str(x), 11 + x, pokemon1, [Pokeball.GREATBALL], [Badge.SEANTOWN, Badge.SOMEWHERE], False))
    """
    trainers.append(Trainer("Jeff", 11, pokemon1, [Pokeball.GREATBALL], [Badge.SEANTOWN, Badge.SOMEWHERE], False))
    trainers.append(Trainer("Bob", 15, pokemon2, [Pokeball.GREATBALL], [Badge.SEANTOWN, Badge.SOMEWHERE], False))

    gym = Gym("DavePlace", Badge.DAVIDCITY, trainers)

    # Have a battle between the predefined trainers
    gym.battle(trainers[0], trainers[1])

    # Try to catch a pokemon
    print("")
    trainers[1].catch(cool_pokemon, trainers[1].get_pokeballs()[0])


if __name__ == "__main__":
    main()
