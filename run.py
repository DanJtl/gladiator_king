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

def PlayerCreation():
    """
    Create a player by letting the player answer some questions 
    """
    print("You are once again led by three guards towards the massive iron gate…")
    print("The iron gate opens slowly, and you feel…")

    bonus_attribute = input("a) ...extra strong.\nb) ...young and athletic.\nc) ...lucky and pumped.\n").lower()
    while bonus_attribute != "a" and bonus_attribute != "b" and bonus_attribute != "c":
        print("You need to type: a, b or c...")
        print("The iron gate opens slowly, and you feel…")
        bonus_attribute = input("a) ...extra strong.\nb) …young and athletic.\nc) …lucky and pumped.\n").lower()

    if bonus_attribute == "a":
        Player.ap = 40
        Player.health = 80
        Player.luck = 6

    elif bonus_attribute == "b":
        Player.ap = 20
        Player.health = 140
        Player.luck = 6

    elif bonus_attribute == "c":
        Player.ap = 20
        Player.health = 100
        Player.luck = 9









