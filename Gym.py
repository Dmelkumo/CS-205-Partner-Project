from enums import Type
from Trainer import Trainer


class Gym:
    def __init__(self, name, badge, trainers):
        self.name = name
        self.badge = badge
        self.trainers = trainers

    # Getters
    def get_name(self):
        return self.name

    def get_badge(self):
        return self.badge

    def get_trainers(self):
        return self.trainers

    # Setters
    def set_name(self, name):
        self.name = name

    def set_badge(self, badge):
        self.badge = badge

    def set_trainers(self, trainers):
        self.trainers = trainers

    # Battle
    def battle(self, trainer1, trainer2, detailed_output):
        # Create two lists of pokemon from the trainers (so any works)
        # Initialize the attacks
        attack1 = Type.NONE
        attack2 = Type.NONE
        i, j = 0, 0

        # For the short version
        if not detailed_output:
            print("")
            print(trainer1.pokemon[i].get_name() + "'s hp: " + str(trainer1.pokemon[i].get_hp()))
            print(trainer2.pokemon[j].get_name() + "'s hp: " + str(trainer2.pokemon[j].get_hp()))

        # While they still have pokemon
        while any(pokemon.get_hp() > 0 for pokemon in trainer1.pokemon) and any(pokemon.get_hp() > 0 for pokemon in trainer2.pokemon):
            if detailed_output:
                # Print current hp's
                print("")
                print(trainer1.pokemon[i].get_name() + "'s hp: " + str(trainer1.pokemon[i].get_hp()))
                print(trainer2.pokemon[j].get_name() + "'s hp: " + str(trainer2.pokemon[j].get_hp()))

            # Perform the attacks
            attack1 = trainer1.pokemon[i].attack()
            attack2 = trainer2.pokemon[j].attack()
            # Determine who attacks first by their speeds
            if trainer1.pokemon[i].get_spd() < trainer2.pokemon[j].get_spd():
                if detailed_output:
                    print(trainer2.pokemon[j].get_name() + " attacks " + trainer1.pokemon[i].get_name())
                dmg = trainer1.pokemon[i].take_damage(attack2, trainer2.pokemon[j].get_primary_type())
                if detailed_output:
                    print("It deals " + str(int(dmg)) + " damage!")
                # Check to see if the other pokemon is dead
                if trainer1.pokemon[i].get_hp() > 0:
                    if detailed_output:
                        print(trainer1.pokemon[i].get_name() + " attacks " + trainer2.pokemon[j].get_name())
                    dmg = trainer2.pokemon[j].take_damage(attack1, trainer1.pokemon[i].get_primary_type())
                    if detailed_output:
                        print("It deals " + str(int(dmg)) + " damage!")
            else:
                if detailed_output:
                    print(trainer1.pokemon[i].get_name() + " attacks " + trainer2.pokemon[j].get_name())
                dmg = trainer2.pokemon[j].take_damage(attack1, trainer1.pokemon[i].get_primary_type())
                if detailed_output:
                    print("It deals " + str(int(dmg)) + " damage!")
                # Check to see if the other pokemon is dead
                if trainer2.pokemon[j].get_hp() > 0:
                    if detailed_output:
                        print(trainer2.pokemon[j].get_name() + " attacks " + trainer1.pokemon[i].get_name())
                    dmg = trainer1.pokemon[i].take_damage(attack2, trainer2.pokemon[j].get_primary_type())
                    if detailed_output:
                        print("It deals " + str(int(dmg)) + " damage!")

            # Check if trainer1's pokemon has died and they have more
            if trainer1.pokemon[i].get_hp() <= 0:
                if detailed_output:
                    print(trainer1.pokemon[i].get_name() + " has fainted!")
                # Pick the next pokemon
                if i < len(trainer1.get_pokemon()) - 1:
                    i += 1
            # Check if trainer2's pokemon has died and they have more
            if trainer2.pokemon[j].get_hp() <= 0:
                if detailed_output:
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
