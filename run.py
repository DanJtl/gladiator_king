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

    """ 
    Getters for player class
    Learned from: https://www.geeksforgeeks.org/getter-and-setter-in-python/ 
    """
    def get_name(self):
        return self._name

    def get_ap(self):
        return self._ap

    def get_health(self):
        return self._health
    
    def get_luck(self):
        return self._luck











