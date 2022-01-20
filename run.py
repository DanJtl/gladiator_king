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

    print("\nThe guards turn to you, and you know it's time to pick a weapon...")
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

    print("\nAs you enter the arena, you hear the crowd goes wild...")
    Player.name = input("What is your name?\n")
    print(f"\n{Player.name.upper()}! ...echoes through the arena.\n")
    print("Your stats are:")

    return Player(Player.name, Player.dmg, Player.health, Player.luck)

# Create an enemy and set enemy stats
def enemy_creation(elite_enemy):
    pprint(vars(player_character))
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

# Attack function for enemies
def enemy_attack():
    print(f"{Enemy.name} is attacking you...")
    hit = random.randint(0, 10)

    if hit <= Enemy.luck:
        print("It hits you and does...")
        Player.health -= Enemy.dmg
        print(f"{Enemy.dmg} in damage!")
        return Player.health

    else:
        print(f"{Enemy.name} fumbles and misses!")
        return 0

def battle():
    print("\nIn front of you, you can see your opponent...")
    print(f"It's the {Enemy.name}.")
    print("\nIt's stats are:")
    pprint(vars(random_enemy))



# def enemy_attack():
# Save character stats as a list

player_character = player_creation()

elite_enemy = True
random_enemy = enemy_creation(elite_enemy)

battle()


