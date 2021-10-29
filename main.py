from enums import Type, Pokeball, Badge
from Pokemon import Pokemon
from Trainer import Trainer
from Gym import Gym
import random


def main():
    # Create some pokemon and trainers
    cool_pokemon = Pokemon("Darkrai", Type.DARK, Type.NONE, 100, 5, 100)
    pokemon1 = []
    for x in range(3):
        pokemon1.append(Pokemon("Pika" + str(x), Type.FIRE + x, Type.FIGHTING + x, 100, random.randint(1, 3), random.randint(80, 120)))

    pokemon2 = []
    for x in range(3):
        pokemon2.append(Pokemon("Ditto" + str(x), Type.NORMAL + x, Type.GHOST + x, 100, random.randint(1, 3), random.randint(80, 120)))

    trainers = []
    """
    for x in range(2):
        trainers.append(Trainer("Jeff" + str(x), 11 + x, pokemon1, [Pokeball.GREATBALL], [Badge.SEANTOWN, Badge.SOMEWHERE], False))
    """
    trainers.append(Trainer("Jeff", 11, pokemon1, [Pokeball.GREATBALL], [Badge.SEANTOWN, Badge.SOMEWHERE], False))
    trainers.append(Trainer("Bob", 15, pokemon2, [Pokeball.GREATBALL], [Badge.SEANTOWN, Badge.SOMEWHERE], False))

    gym = Gym("DavePlace", Badge.DAVIDCITY, trainers)

    detailed_info = input("Do you want detailed battle info? Enter y for detailed battle info, n for standard info: ")
    while detailed_info != 'y' and detailed_info != 'n':
        detailed_info = input("Please enter 'y' or 'n': ")

    # Have a battle between the predefined trainers
    if detailed_info == 'y':
        gym.battle(trainers[0], trainers[1], True)
    else:
        gym.battle(trainers[0], trainers[1], False)

    # Try to catch a pokemon
    print("")
    trainers[1].catch(cool_pokemon, trainers[1].get_pokeballs()[0])


if __name__ == "__main__":
    main()
