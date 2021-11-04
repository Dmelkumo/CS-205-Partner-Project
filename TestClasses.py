import unittest
from enums import Type, Pokeball, Badge
from Pokemon import Pokemon
from Trainer import Trainer
from Gym import Gym
import random


class ClassesModuleTest(unittest.TestCase):
    def setUp(self):
        self.p = Pokemon("Pl0rqachu", Type.ELECTRIC, Type.NONE, 50, 2, 88)
        self.p_ghost = Pokemon("Pl0rqachu", Type.GHOST, Type.NONE, 50, 2, 88)
        self.p_water_rock = Pokemon("Pl0rqachu", Type.WATER, Type.ROCK, 50, 2, 88)
        self.p_grass = Pokemon("Pl0rqachu", Type.GRASS, Type.NONE, 50, 2, 88)
        self.p_poison = Pokemon("Pl0rqachu", Type.POISON, Type.NONE, 50, 2, 88)
        self.p_ice = Pokemon("Pl0rqachu", Type.ICE, Type.NONE, 50, 2, 88)
        self.p_dragon_dark = Pokemon("Pl0rqachu", Type.DRAGON, Type.DARK, 50, 2, 88)
        self.g = Gym("A very interesting gym", Badge.DAVIDCITY, [Trainer("David", 10, [Pokemon("David", Type.NORMAL, Type.NONE, 10, 2, 50)], [Pokeball.GREATBALL], [Badge.SOMEWHERE], False)])
        self.t = Trainer("Sean", 42, [Pokemon("Musume", Type.WATER, Type.FAIRY, 10, 2, 60)], [Pokeball.MASTERBALL, Pokeball.GREATBALL], [Badge.SEANTOWN], True)

    # Pokemon
    def test_pokemon_get_name(self):
        self.assertEqual("Pl0rqachu", self.p.get_name())

    def test_pokemon_get_primary_type(self):
        self.assertEqual(Type.ELECTRIC, self.p.get_primary_type())
    
    def test_pokemon_get_secondary_type(self):
        self.assertEqual(Type.NONE, self.p.get_secondary_type())
    
    def test_pokemon_get_hp(self):
        self.assertEqual(50, self.p.get_hp())
    
    def test_pokemon_set_name(self):
        self.p.set_name("Pl0rqachu")
        self.assertEqual("Pl0rqachu", self.p.get_name())
    
    def test_pokemon_set_primary_type(self):
        self.p.set_primary_type(Type.WATER)
        self.assertEqual(Type.WATER, self.p.get_primary_type())
    
    def test_pokemon_set_secondary_type(self):
        self.p.set_secondary_type(Type.FIGHTING)
        self.assertEqual(Type.FIGHTING, self.p.get_secondary_type())
    
    def test_pokemon_set_hp(self):
        self.p.set_hp(10)
        self.assertEqual(10, self.p.get_hp())
    
    def test_pokemon_attack(self):
        self.assertIn(self.p.attack(), range(2, 21))
    
    def test_pokemon_take_damage(self):
        self.assertEqual(self.p_ghost.take_damage(1, Type.NORMAL), 0)
        self.assertEqual(self.p_water_rock.take_damage(1, Type.FIRE), .25)
        self.assertEqual(self.p_grass.take_damage(1, Type.ELECTRIC), .5)
        self.assertEqual(self.p_poison.take_damage(1, Type.ICE), 1)
        self.assertEqual(self.p_ice.take_damage(1, Type.FIGHTING), 2)
        self.assertEqual(self.p_dragon_dark.take_damage(1, Type.FAIRY), 4)

    # Gym
    def test_gym_get_name(self):
        self.assertEqual("A very interesting gym", self.g.get_name())
    
    def test_gym_get_badge(self):
        self.assertEqual(Badge.DAVIDCITY, self.g.get_badge())
    
    def test_gym_get_trainers(self):
        self.assertEqual(self.g.trainers, self.g.get_trainers())
    
    def test_gym_set_name(self):
        self.g.set_name("Sean's Gym")
        self.assertEqual("Sean's Gym", self.g.get_name())
    
    def test_gym_set_badge(self):
        self.g.set_badge(Badge.SEANTOWN)
        self.assertEqual(Badge.SEANTOWN, self.g.get_badge())
    
    def test_gym_set_trainers(self):
        self.g.set_trainers([Trainer("Sean", 10, [Pokemon("0rq", Type.NORMAL, Type.NONE, 10, 2, 50)], [Pokeball.GREATBALL], [Badge.SOMEWHERE], False)])
        self.assertEqual(self.g.trainers[0].get_name(), "Sean")
    
    def test_gym_battle(self):
        self.g.badge = Badge.DAVIDCITY
        t1 = Trainer("Sean", 99, [Pokemon("Pika", Type.ELECTRIC, Type.NONE, 100, 3, 50)], [Pokeball.MASTERBALL],
            [], False)
        t2 = Trainer("David", 1, [Pokemon("Weakling", Type.WATER, Type.NONE, 4, 4, 40)], [], [], True)
        self.assertEqual([Badge.DAVIDCITY], self.g.battle(t1, t2, False).badges)

    # Trainer
    def test_trainer_get_name(self):
        self.assertEqual("Sean", self.t.get_name())
    
    def test_trainer_get_age(self):
        self.assertEqual(42, self.t.get_age())
    
    def test_trainer_get_pokemon(self):
        self.assertEqual("Musume", self.t.pokemon[0].get_name())
    
    def test_trainer_get_pokeballs(self):
        self.assertEqual([Pokeball.MASTERBALL, Pokeball.GREATBALL], self.t.get_pokeballs())
    
    def test_trainer_get_badges(self):
        self.assertEqual([Badge.SEANTOWN], self.t.get_badges())

    def test_trainer_get_is_gym_leader(self):
        self.assertEqual(True, self.t.get_is_gym_leader())
    
    def test_trainer_set_name(self):
        self.t.set_name("John")
        self.assertEqual("John", self.t.get_name())
    
    def test_trainer_set_age(self):
        self.t.set_age(21)
        self.assertEqual(21, self.t.get_age())
    
    def test_trainer_set_pokemon(self):
        self.t.set_pokemon([Pokemon("0rq", Type.NORMAL, Type.NONE, 10, 2, 50)])
        self.assertEqual("0rq", self.t.pokemon[0].get_name())
    
    def test_trainer_set_pokeballs(self):
        self.t.set_pokeballs([Pokeball.GREATBALL])
        self.assertEqual(Pokeball.GREATBALL, self.t.pokeballs[0])
    
    def test_trainer_set_badges(self):
        self.t.set_badges([Badge.SOMEWHERE])
        self.assertEqual([Badge.SOMEWHERE], self.t.get_badges())

    def test_trainer_set_is_gym_leader(self):
        self.t.set_is_gym_leader(False)
        self.assertEqual(False, self.t.get_is_gym_leader())
    
    def test_trainer_catch(self):
        score = 0
        for _ in range(4):
            if self.t.catch(Pokemon("Jim", Type.NONE, Type.NONE, 10, 5, 30), Pokeball.MASTERBALL) is not None:
                score += 1
        self.assertGreater(score, 0)

    def test_trainer_add_pokemon(self):
        self.t.pokemon = [Pokemon("Jack", Type.NORMAL, Type.NONE, 10, 2, 50),
                        Pokemon("Jill", Type.NORMAL, Type.NONE, 10, 2, 50)]
        self.t.add_pokemon(Pokemon("Jeff", Type.FIGHTING, Type.NONE, 10, 2, 50))
        self.assertEqual("Jeff", self.t.pokemon[2].name)


if __name__ == '__main__':
    unittest.main()