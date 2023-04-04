import random

from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

# Create Items
small_potion = Item("Small Potion", "potion", "Heals 50 HP", 50)
medium_potion = Item("Medium Potion", "potion", "Heals 100 HP", 100)
large_potion = Item("Large Potion", "potion", "Heals 100 HP", 500)
elixir = Item("Small Elixir", "elixir", "Restores full HP/MP of one party member", 9999)
large_elixir = Item("Large Elixir", "elixir", "Restores full HP/MP of all party members", 9999)
grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

# Create Inventory
items = [small_potion, medium_potion, large_potion, elixir, large_elixir, grenade]

# Create Black Magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("thunder", 10, 100, "black")
blizzard = Spell("blizzard", 10, 100, "black")
meteor = Spell("meteor", 20, 200, "black")
quake = Spell("quake", 14, 120, "black")

# Create White Magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

# Create Spell Book
magic = [fire, thunder, blizzard, meteor, quake, cure, cura]

# Instantiate People
player = Person(460, 65, 60, 34, magic, items)
enemy = Person(1200, 65, 45, 25, magic, items)

enemyStr = bcolors.FAIL + bcolors.BOLD + "ENEMY" + bcolors.ENDC
playerStr = bcolors.OKGREEN + bcolors.BOLD + "YOU" + bcolors.ENDC

running = True
i = 0
print(bcolors.FAIL + bcolors.BOLD + "\nAN ENEMY ATTACKS!" + bcolors.ENDC)


def use_magic():
    global choice, index
    while True:

        current_player_mp = player.get_mp()
        enough_mana = False

        for spell in player.magic:
            if current_player_mp > spell.get_spell_mp_cost():
                enough_mana = True
                break

        if not enough_mana:
            print(bcolors.FAIL + "\nMP is too low to use any spells!\n" + bcolors.ENDC)
            break

        player.choose_magic()
        choice = input("\nChoose magic or type 'b' to go back a menu :")

        if choice == "b":
            return False

        index = int(choice) - 1
        chosen_spell = player.magic[index]
        spell_cost = chosen_spell.get_spell_mp_cost()
        spell_name = chosen_spell.get_spell_name()
        spell_damage = chosen_spell.generate_damage()
        spell_type = chosen_spell.type

        if spell_cost > current_player_mp:
            print(bcolors.FAIL + "\nNot enough MP, choose another spell!\n" + bcolors.ENDC)
        else:
            player.mp -= spell_cost

            if spell_type == "white":
                heals = spell_damage
                player.heal(heals)
                print(playerStr, "healed for", heals, "points of", player.magic[index].get_spell_name(),
                      "    New HP:", player.get_hp())
            else:
                magic_damage = spell_damage
                enemy.take_damage(magic_damage)

                print(playerStr, "attacked for", magic_damage, "points of", player.magic[index].get_spell_name())
            break


def use_item():
    global choice
    player.choose_item()
    choice = input("\nChoose item or type 'b' to go back a menu :")

    if choice == "b":
        return False


def use_melee():
    damage = player.generate_damage()
    enemy.take_damage(damage)
    print(playerStr, "attacked for", damage, "points of damage.    Enemy HP:", enemy.get_hp())
    print("\nYour HP:",
          bcolors.OKGREEN + bcolors.BOLD + str(player.get_hp()) + "/" + str(player.get_maxhp()) + bcolors.ENDC)


def enemy_attack():
    global index
    enemy_choice = random.randrange(1, 2)
    index = int(enemy_choice) - 1
    if index == 0:
        enemy_damage = enemy.generate_damage()
        player.take_damage(enemy_damage)
        print(enemyStr, "attacks for", enemy_damage, "points of damage.")


while running:

    action_taken = False

    while not action_taken:

        print("\n===================================================\n")
        player.choose_action()
        choice = input("Choose action:")
        index = int(choice) - 1

        action_taken = True

        if index == 0:
            action_taken = use_melee()

        elif index == 1:
            action_taken = use_magic()

        elif index == 2:
            action_taken = use_item()

    if enemy.get_hp() == 0:
        print(enemyStr, "died! GOODJOB!!!")
        break

    enemy_attack()

    print("---------------------------------")
    print("Enemy HP:",
          bcolors.FAIL + bcolors.BOLD + str(enemy.get_hp()) + "/" + str(enemy.get_maxhp()) + bcolors.ENDC)

    print("\nYour HP:",
          bcolors.OKGREEN + bcolors.BOLD + str(player.get_hp()) + "/" + str(player.get_maxhp()) + bcolors.ENDC)
    print("Your MP:",
          bcolors.OKBLUE + bcolors.BOLD + str(player.get_mp()) + "/" + str(player.get_maxmp()) + bcolors.ENDC)

    if player.get_hp() == 0:
        print(playerStr, "\ndied! GAMEOVER!!!")
        break
