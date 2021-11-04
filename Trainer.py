from enums import Pokeball, Badge
from Pokemon import Pokemon
import random


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

    def catch_incorrect(self, pokemon, pokeball):
        # Get a random number 0 - 100
        catch_rate = random.randint(0, 100)
        # Add in the ball type
        catch_rate += pokeball
        print(self.name + " tries to throw a ball!")

        # Try to catch it
        if catch_rate < 100:  # This part is wrong
            print(self.name + " Successfully caught " + pokemon.get_name() + "!")
            self.add_pokemon(pokemon)
            return pokemon
        else:
            print(pokemon.get_name() + " fled!")
            return None

    def add_pokemon(self, pokemon):
        # Simple list append
        self.pokemon.append(pokemon)
