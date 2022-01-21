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


def create_player():
    """
    Create a character by letting the player answer some questions.
    It also sets the player attributes and making sure they
    input correct data by using a while loop.
    """
    print("You are once again led by three guards towards the iron gate…")
    print("The iron gate opens slowly, and you feel…")

    player_stats = input("""
        a) ...extra strong.
        b) ...young and athletic.
        c) ...lucky and pumped.\n""").lower()

    while player_stats != "a" and player_stats != "b" and player_stats != "c":
        print("You need to type: a, b or c...")
        print("The iron gate opens slowly, and you feel…")
        player_stats = input("""
            a) ...extra strong.
            b) …young and athletic.
            c) …lucky and pumped.\n""").lower()

    if player_stats == "a":
        Player.dmg = 40
        Player.health = 80
        Player.luck = random.randint(3, 8)

    elif player_stats == "b":
        Player.dmg = 20
        Player.health = 140
        Player.luck = random.randint(3, 8)

    elif player_stats == "c":
        Player.dmg = 20
        Player.health = 100
        Player.luck = random.randint(5, 8)

    print("\nThe guards turn to you...")
    print("\n...and you know it's time to pick a weapon...")
    print("Which one do you choose?")

    weapon = input("""
        a) Executioner's Sword.
        b) Sword and shield.
        c) Halberd.\n""").lower()

    while weapon != "a" and weapon != "b" and weapon != "c":
        print("You need to type: a, b or c...")
        print("Which one do you choose?")
        weapon = input("""
            a) Executioner's Sword.
            b) Sword and shield.
            c) Halberd.\n""").lower()

    if weapon == "a":
        Player.dmg += 30

    elif weapon == "b":
        Player.dmg += 10
        Player.health += 20

    elif weapon == "c":
        Player.dmg += 20
        Player.luck += 2

    print("\nAs you enter the arena, you hear the crowd goes wild...")
    Player.name = input("What is your name?\n")
    print(f"\n{Player.name.upper()}! ...echoes through the arena.\n")
    print("Your stats are:")

    return Player(Player.name, Player.dmg, Player.health, Player.luck)

def create_enemy():
    """
    Create an enemy and set enemy stats
    """
    enemy_first = (
            "Angry", "Big", "Aggresive", "Furious", "Crazy",
            "Creepy", "Dangerous", "Evil", "Powerful", "Scary"
        )
    enemy_last = (
            "Goblin", "Troll", "Undead", "Monster", "Orc",
            "Zombie", "Skeleton", "Cyclop", "Dragon", "Ghoul"
        )

    Enemy.name = random.choice(enemy_first)+" "+random.choice(enemy_last)

    elite_enemy = random.randint(0, 10)

    if elite_enemy >= 7:
        elite_enemy = True
    else:
        elite_enemy = False

    if elite_enemy is True:
        Enemy.dmg = random.randint(15, 30)
        Enemy.health = random.randint(120, 200)
        Enemy.luck = random.randint(3, 10)
        Enemy.special = random.randint(40, 60)

        return Elite(
                Enemy.name, Enemy.dmg, Enemy.health,
                Enemy.luck, Enemy.special
            )

    else:
        Enemy.dmg = random.randint(1, 15)
        Enemy.health = random.randint(50, 120)
        Enemy.luck = random.randint(1, 6)

        return Enemy(Enemy.name, Enemy.dmg, Enemy.health, Enemy.luck)


def enemy_attack():
    """
    Attack function for enemies
    """
    print(f"\n{Enemy.name} rushes towards you and attacks...")
    hit = random.randint(0, 10)

    if hit <= Enemy.luck:
        print("It hits you and does...")
        Player.health -= Enemy.dmg
        print(f"{Enemy.dmg} in damage!")
        return Player.health

    else:
        print(f"{Enemy.name} fumbles and misses!")


def player_attack():
    """
    Attack function for player
    """
    print("\nIn front of you, you can see your opponent...")
    print(f"It's the {Enemy.name}.")
    print("\nIt's stats are:")
    pprint(vars(enemy))
    print("\nYou look at the enemy and decides to do a...")
    attack = input("""
        a) Fast attack.
        b) Normal attack.
        c) Charge attack.\n""").lower()

    while attack != "a" and attack != "b" and attack != "c":
        print("You need to type: a, b or c...")
        print("\nYou look at the enemy and decide to do a...")
        attack = input("""
            a) Fast attack.
            b) Normal attack.
            c) Charge attack.\n""").lower()

    if attack == "a":
        print("You raise your wepaon...")
        print(f"and attack the {Enemy.name} with a fast attack")
        
    elif attack == "b":
        print("You raise your wepaon...")
        print(f"and attack the {Enemy.name} with a normal attack")

    elif attack == "c":
        print("You raise your wepaon...")
        print(f"and attack the {Enemy.name} with a charge attack")

    hit = random.randint(0, 10)

    if hit <= Player.luck:
        print("You hit it and do...")
        Enemy.health -= Player.dmg
        print(f"{Player.dmg} in damage!")
        return Enemy.health

    else:
        print("You fumble and miss!")

# Battle function
def battle():

    while Player.health > 0 and Enemy.health > 0:

        player_attack()
        print(f"\n{Enemy.name}'s health is now {Enemy.health}.")
        if Enemy.health <= 0:
            print(f"You killed the {Enemy.name}!\n")
            print(f"Everyone in the arena is shouting your name... {Player.name.upper()}!")
            print(f"Your health is now {Player.health}...")
        else:
            enemy_attack()
            print(f"\nYour Health is now {Player.health}.")
        if Player.health <= 0:
            print("You fought your hardest...")
            print("...but it wasn't enough.")


player = None
enemy = None

player = create_player()
pprint(vars(player))
enemy = create_enemy()
battle()
