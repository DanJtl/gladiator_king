import math
import random

class Player:
    """
    Creates base class for player
    """
    def __init__(self, player_name, player_ap, player_health, player_luck):
        self.name = player_name
        self.ap = player_ap
        self.health = player_health
        self.luck = player_luck

    # Getters for player class - so you can, for example, check/return health 
    # (getters and setters learned from:) https://medium.com/@pranaygore/setters-and-getters-in-python-76b5473b3c83
    def getName(self):
        return self.name

    def getAp(self):
        return self.ap

    def getHealth(self):
        return self.health
    
    def getLuck(self):
        return self.luck

    # Setters for player class - so you can, for example, update the health attribute
    def setName(self, update_name):
        self.name = update_name

    def setAp(self, update_ap):
        self.ap = update_ap)

    def setHealth(self, update_health):
        self.health = update_health
    
    def setLuck(self, update_luck):
        self.luck = update_luck

def player_creation():
    """
    Create a player by letting the player answer some questions 
    """
    print("You are once again led by three guards towards the massive iron gate…")
    print("The iron gate opens slowly, and you feel…")

    # Sets the player attributes and making sure they input correct data by using a while loop
    bonus_attribute = input("a) ...extra strong.\nb) ...young and athletic.\nc) ...lucky and pumped.\n").lower()
    while player_stats != "a" and player_stats != "b" and player_stats != "c":
        print("You need to type: a, b or c...")
        print("The iron gate opens slowly, and you feel…")
        player_stats = input("a) ...extra strong.\nb) …young and athletic.\nc) …lucky and pumped.\n").lower()

    if player_stats == "a":
        Player.ap = 40
        Player.health = 80
        Player.luck = 5

    elif player_stats == "b":
        Player.ap = 20
        Player.health = 140
        Player.luck = 5

    elif player_stats == "c":
        Player.ap = 20
        Player.health = 100
        Player.luck = 8

    print("The guards turn to you, and you know it's time to pick a weapon")
    print("Which one do you choose?")
    
    # Add to specific player attribute depending on their choice and making sure they input correct data by using a while loop
    weapon_choice = input("a) Executioner's Sword.\nb) Sword and shield.\nc) Halberd.\n").lower()
    while weapon_choice != "a" and weapon_choice != "b" and weapon_choice != "c":
        print("You need to type: a, b or c...")
        print("Which one do you choose?")
        weapon_choice = input("a) Executioner's Sword.\nb) Sword and shield.\nc) Halberd.\n").lower()
    
    if weapon_choice == "a":
        Player.ap += 30

    elif weapon_choice == "b":
        Player.ap += 10
        Player.health += 20

    elif weapon_choice == "c":
        Player.ap += 20 
        Player.luck += 2 

    print("As you enter the arena, you hear the crowd goes wild...")
    Player.name = input("what is your name?")
    print(Player.name.upper(), "! echoes through the arena")









