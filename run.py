import math
import random
from pprint import pprint


class Player:
    """
    Creates class for player
    """
    def __init__(self, player_name, player_dmg, player_health, player_luck):
        self.name = player_name
        self.dmg = player_dmg
        self.health = player_health
        self.luck = player_luck

    """
    Getters for player class - so you can, for example, check/return health.
    Getters and setters learned from:
    https://medium.com/@pranaygore/setters-and-getters-in-python-76b5473b3c83
    """
    def getName(self):
        return self.name
    def getDmg(self):
        return self.dmg
    def getHealth(self):
        return self.health
    def getLuck(self):
        return self.luck

    # Setters for player class - so you can update the health attribute e.g.
    def setName(self, update_name):
        self.name = update_name
    def setAp(self, update_ap):
        self.dmg = update_dmg
    def setHealth(self, update_health):
        self.health = update_health
    def setLuck(self, update_luck):
        self.luck = update_luck

class Enemy:
    """
    Creates base class for enemies
    """
    def __init__(self, enemy_name, enemy_dmg, enemy_health, enemy_luck):
        self.name = enemy_name
        self.dmg = enemy_dmg
        self.health = enemy_health
        self.luck = enemy_luck


def player_creation():
    """
    Create a character by letting the player answer some questions
    """
    print("You are once again led by three guards towards the iron gate…")
    print("The iron gate opens slowly, and you feel…")

    """
    Sets the player attributes and making sure they
    input correct data by using a while loop
    """
    player_stats = input("a) ...extra strong.\nb) ...young and athletic.\nc) ...lucky and pumped.\n").lower()
    while player_stats != "a" and player_stats != "b" and player_stats != "c":
        print("You need to type: a, b or c...")
        print("The iron gate opens slowly, and you feel…")
        player_stats = input("a) ...extra strong.\nb) …young and athletic.\nc) …lucky and pumped.\n").lower()

    if player_stats == "a":
        Player.dmg = 40
        Player.health = 80
        Player.luck = 5

    elif player_stats == "b":
        Player.dmg = 20
        Player.health = 140
        Player.luck = 5

    elif player_stats == "c":
        Player.dmg = 20
        Player.health = 100
        Player.luck = 8

    print("The guards turn to you, and you know it's time to pick a weapon...")
    print("Which one do you choose?")

    """
    Add to specific player attribute depending on their choice,
    and making sure they input correct data by using a while loop
    """
    weapon_choice = input("a) Executioner's Sword.\nb) Sword and shield.\nc) Halberd.\n").lower()
    while weapon_choice != "a" and weapon_choice != "b" and weapon_choice != "c":
        print("You need to type: a, b or c...")
        print("Which one do you choose?")
        weapon_choice = input("a) Executioner's Sword.\nb) Sword and shield.\nc) Halberd.\n").lower()

    if weapon_choice == "a":
        Player.dmg += 30

    elif weapon_choice == "b":
        Player.dmg += 10
        Player.health += 20

    elif weapon_choice == "c":
        Player.dmg += 20
        Player.luck += 2

    print("As you enter the arena, you hear the crowd goes wild...")
    Player.name = input("What is your name?\n")
    print(Player.name.upper(), "! ...echoes through the arena.")
    print("Your stats are:\n")

    return [Player.name, Player.dmg, Player.health, Player.luck]

# Save character stats as a list
character_stats = player_creation()
player_character = Player(character_stats[0], character_stats[1], character_stats[2], character_stats[3])

pprint(vars(player_character))
