## Related classes for the RPG game

import random
from math import ceil

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:

    def __init__(self, name , hp, mp, atk, df, magic, items):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def generate_magic_damage(self, i):
        magicLow = self.magic[i]["damage"] - 5
        magicHigh = self.magic[i]["damage"] + 5

        return random.randrange(magicLow, magicHigh)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0


    def heal(self, heal):
        self.hp += heal
        if self.hp > self.maxhp:
            self.hp = self.maxhp

        return self.hp

    def get_hp(self):
        return self.hp

    def get_mp(self):
        return self.mp

    def get_maxhp(self):
        return self.maxhp

    def get_maxmp(self):
        return self.maxmp

    def reduce_mp(self,cost):
        self.mp -= cost


    def choose_action(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD + "Actions" + bcolors.ENDC)
        for item in self.actions:
            print("   " + str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "Magic" + bcolors.ENDC)
        for spell in self.magic:
            print("   " + str(i) + ":", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1
        print("\n")

    def choose_item(self):
        i = 1
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "Items" + bcolors.ENDC)
        for item in self.items:
            print("   " + str(i) + ":", item["name"].name, ":", item["name"].description, ": x" + str(item["quantity"]))
            i += 1
        print("\n")

    def show_enemy_stats(self):

        max_health_blocks = 100

        stats_string = bcolors.BOLD + self.name + ":      "

        health_string = str(self.hp) + "/" + str(self.maxhp)
        stats_string += self.reset_white_spaces(health_string) + " |" + bcolors.FAIL

        health_blocks_left = int(ceil((self.hp / self.maxhp) * max_health_blocks))

        for i in range(health_blocks_left):
            stats_string += "█"

        for i in range(max_health_blocks - health_blocks_left):
            stats_string += " "

        stats_string += bcolors.ENDC + "|  "

        print(stats_string)


    def show_stats(self):

        max_health_blocks = 25
        max_mana_blocks = 10

        stats_string = bcolors.BOLD + self.name + ":      "

        health_string = str(self.hp) + "/" + str(self.maxhp)
        stats_string += self.reset_white_spaces(health_string) + " |" + bcolors.OKGREEN

        health_blocks_left = int(ceil((self.hp / self.maxhp) * max_health_blocks))

        for i in range(health_blocks_left):
            stats_string += "█"

        for i in range(max_health_blocks - health_blocks_left):
            stats_string += " "

        stats_string += bcolors.ENDC + "|  "

        mana_string = str(self.mp) + "/" + str(self.maxmp)
        stats_string += self.reset_white_spaces(mana_string) + "|" + bcolors.OKBLUE
        number_of_mana_block = int(ceil((self.mp / self.maxmp) * max_mana_blocks))

        for i in range(number_of_mana_block):
            stats_string += "█"

        for i in range(max_mana_blocks - number_of_mana_block):
            stats_string += " "

        stats_string += bcolors.ENDC + "|"

        print(stats_string)

    def reset_white_spaces(self, string):
        current_hp = ""
        if len(string) < 9:
            decreased = 9 - len(string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += string
        else:
            current_hp = string
        return current_hp






