import unittest
from enums import Type, Pokeball, Badge
from Pokemon import Pokemon
from Trainer import Trainer
from Gym import Gym
import random

class ClassesModuleTest(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_pokemon_get_name(self):
        p = Pokemon("Pogachu", Type.ELECTRIC, Type.NONE, 50)
        self.assertEqual("Pogachu", p.get_name())

    def test_pokemon_get_primary_type(self):
        p = Pokemon("Pogachu", Type.ELECTRIC, Type.NONE, 50)
        self.assertEqual(Type.ELECTRIC, p.get_primary_type())
    
    def test_pokemon_get_secondary_type(self):
        p = Pokemon("Pogachu", Type.ELECTRIC, Type.NONE, 50)
        self.assertEqual(Type.NONE, p.get_secondary_type())
    
    def test_pokemon_get_hp(self):
        p = Pokemon("Pogachu", Type.ELECTRIC, Type.NONE, 50)
        self.assertEqual(50, p.get_hp())
    
    def test_pokemon_set_name(self):
        p = Pokemon("Pogachu", Type.ELECTRIC, Type.NONE, 50)
        p.set_name("Pikachu")
        self.assertEqual("Pikachu", p.get_name())
    
    def test_pokemon_set_primary_type(self):
        p = Pokemon("Pogachu", Type.ELECTRIC, Type.NONE, 50)
        p.set_primary_type(Type.WATER)
        self.assertEqual(Type.WATER, p.get_primary_type())
    
    def test_pokemon_set_secondary_type(self):
        p = Pokemon("Pogachu", Type.ELECTRIC, Type.NONE, 50)
        p.set_secondary_type(Type.FIGHTING)
        self.assertEqual(Type.FIGHTING, p.get_secondary_type())
    
    def test_pokemon_set_hp(self):
        p = Pokemon("Pogachu", Type.ELECTRIC, Type.NONE, 50)
        p.set_hp(10)
        self.assertEqual(10, p.get_hp())
    
    def test_pokemon_attack(self):
        p = Pokemon("Pogachu", Type.ELECTRIC, Type.NONE, 50)
        self.assertIn(p.attack(), range(11))
    
    # Huh
    def test_pokemon_take_damage(self):
        pass

if __name__ == '__main__':
    unittest.main()