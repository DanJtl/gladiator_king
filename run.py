import math
import random
from pprint import pprint


class Player:
    """
    Creates class for player
    """
    def __init__(self, name, dmg, health, luck):
        self.name = name
        self.dmg = dmg
        self.health = health
        self.luck = luck

class Enemy:
    """
    Creates base class for enemies
    """
    def __init__(self, name, dmg, health, luck):
        self.name = name
        self.dmg = dmg
        self.health = health
        self.luck = luck

class Elite(Enemy):
    """
    Create elite enemies by inherit from enemy class
    """
    def __init__(self, name, dmg, health, luck, special):
        super().__init__(name, dmg, health, luck)
        self.special = special

# Create a character by letting the player answer some questions
def player_creation():
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

# Create an enemy and set enemy stats
def enemy_creation(elite_enemy):
    enemy_name_first = ("Angry", "Big", "Aggresive", "Furious", "Crazy", "Creepy", "Dangerous", "Evil", "Powerful", "Scary")
    enemy_name_last = ("Goblin", "Troll", "Undead", "Monster", "Orc", "Zombie", "Skeleton", "Cyclop", "Dragon", "Ghoul")

    Enemy.name = random.choice(enemy_name_first)+" "+random.choice(enemy_name_last)
    
    if elite_enemy is True:
        Enemy.dmg = random.randint(15, 30)
        Enemy.health = random.randint(80, 160)
        Enemy.luck = random.randint(3, 10)
        Enemy.special = random.randint(40, 60)

        return Elite(Enemy.name, Enemy.dmg, Enemy.health, Enemy.luck, Enemy.special)

    else:
        Enemy.dmg = random.randint(1, 15)
        Enemy.health = random.randint(20, 80)
        Enemy.luck = random.randint(1, 6)
        
        return Enemy(Enemy.name, Enemy.dmg, Enemy.health, Enemy.luck)

def enemy_attack():

elite_enemy = False

random_enemy = enemy_creation(elite_enemy)

pprint(vars(random_enemy))


# Save character stats as a list
#character_stats = player_creation()
#player_character = Player(character_stats[0], character_stats[1], character_stats[2], character_stats[3])

#pprint(vars(player_character))
