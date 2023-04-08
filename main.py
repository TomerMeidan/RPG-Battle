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
inventory = [{"name": small_potion, "quantity": 5}, {"name": medium_potion, "quantity": 1},
             {"name": large_potion, "quantity": 0}, {"name": elixir, "quantity": 0},
             {"name": large_elixir, "quantity": 0}, {"name": grenade, "quantity": 1}]

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
magic_book = [fire, thunder, blizzard, meteor, quake, cure, cura]

# Instantiate Players, Enemies and NPCs
player1 = Person("Extaza", 1460, 65, 60, 34, magic_book, inventory)
player2 = Person("Kelroy", 1720, 20, 60, 34, magic_book, inventory)
player3 = Person("Skadii", 1300, 95, 60, 34, magic_book, inventory)
enemy = Person("Wild Homeless", 3200, 65, 245, 25, [], [])

party = [player1, player2, player3]

enemyStr = bcolors.FAIL + bcolors.BOLD + "ENEMY" + bcolors.ENDC
playerStr = bcolors.OKGREEN + bcolors.BOLD + "YOU" + bcolors.ENDC


# Initiate The Game
running = True
action_taken = False
print(bcolors.FAIL + bcolors.BOLD + "\nAN ENEMY ATTACKS!" + bcolors.ENDC)


def use_magic():
    global action_taken
    while True:

        current_player_mp = player1.get_mp()
        enough_mana = False

        for spell in player1.magic:
            if current_player_mp > spell.get_spell_mp_cost():
                enough_mana = True
                break

        if not enough_mana:
            print(bcolors.FAIL + "MP is too low to use any spells!" + bcolors.ENDC)
            action_taken = False
            return

        player1.choose_magic()
        item_choice = input("Choose magic or type '0' to go back a menu :")
        index = int(item_choice) - 1

        if index == -1:
            action_taken = False
            return

        chosen_spell = player1.magic[index]
        spell_cost = chosen_spell.get_spell_mp_cost()
        spell_damage = chosen_spell.generate_damage()
        spell_type = chosen_spell.type

        if spell_cost > current_player_mp:
            print(bcolors.FAIL + "Not enough MP, choose another spell!" + bcolors.ENDC)
        else:
            player1.mp -= spell_cost

            if spell_type == "white":
                heals = spell_damage
                player1.heal(heals)
                print(playerStr, "healed for", heals, "points of", player1.magic[index].get_spell_name(),
                      "    New HP:", player1.get_hp())
            else:
                magic_damage = spell_damage
                enemy.take_damage(magic_damage)

                print(playerStr, "attacked for", magic_damage, "points of", player1.magic[index].get_spell_name())
            return


def use_item():
    global action_taken
    player1.choose_item()
    item_choice = int(input("Choose item or type '0' to go back a menu :"))

    index = int(item_choice) - 1

    if index == -1:
        action_taken = False
        return

    item = player1.items[index]["name"]
    item_quantity = player1.items[index]["quantity"]

    if item_quantity == 0:
        action_taken = False
        print(bcolors.FAIL + "You don't have a", item.name, "in your inventory! choose another item!" + bcolors.ENDC)
        return

    if item.type == "potion":
        player1.heal(item.prop)
        print(playerStr, "healed for", str(item.prop), "points with a", item.name)
    elif item.type == "elixir":
        player1.hp = player1.maxhp
        player1.mp = player1.maxmp
        print(playerStr, "healed and refilled mana", "with a", item.name)
    elif item.type == "attack":
        enemy.take_damage(item.prop)
        print(playerStr, "dealt damage equal to", str(item.prop), "using a", item.name)

        player1.items[index]["quantity"] -= 1

def use_melee():
    damage = player1.generate_damage()
    enemy.take_damage(damage)
    print(playerStr, "attacked for", damage, "points of damage.    Enemy HP:", enemy.get_hp())


def enemy_attack():
    global index
    enemy_choice = random.randrange(1, 2)
    index = int(enemy_choice) - 1
    if index == 0:
        player = random.choice(party)
        enemy_damage = enemy.generate_damage()
        player.take_damage(enemy_damage)
        print(enemyStr, "attacks", player.name, "for", enemy_damage, "points of damage.")


if __name__ == "__main__":

    while running:

        for player in party:
            player.show_stats()

        for player in party:

            print("\n")
            print("NAME                 HP                                 MP")
            player.show_stats()

            action_taken = False

            while not action_taken:

                print("===================================================")
                player.choose_action()
                item_choice = input("Choose action:")
                print("\n")
                index = int(item_choice) - 1

                action_taken = True

                if index == 0:
                    use_melee()

                elif index == 1:
                    use_magic()

                elif index == 2:
                    use_item()

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
