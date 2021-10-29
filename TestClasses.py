import unittest
from enums import Type, Pokeball, Badge
from Pokemon import Pokemon
from Trainer import Trainer
from Gym import Gym
import random


class ClassesModuleTest(unittest.TestCase):
    def setUp(self):
        self.p = Pokemon("Pl0rqachu", Type.ELECTRIC, Type.NONE, 50, 2, 88)
    
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
    
    # Huh
    def test_pokemon_take_damage(self):
        pass


if __name__ == '__main__':
    unittest.main()