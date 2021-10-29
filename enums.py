# File for the enums in this program
from enum import IntEnum, Enum


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
