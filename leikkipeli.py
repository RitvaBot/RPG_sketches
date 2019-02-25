

import random

class Person():
    def __init__(self, name, hp, mp, atk, action):
        self.name = name
        self.hp = hp
        self.maxmp = mp
        self.atk_high = atk + 10
        self.atk_low = atk - 10
        self.action = ("Physical Attack")

    def stats(self):
        print(self.name)
        print(f"{self.hp}/{self.maxhp}")
        print(f"{self.mp}/{self.maxhp}")

    def generate_atk_damage(self):
        dmg = random.randint(self.atk_low, self.atk_high)
        return dmg

    def take_damage(self, dmg):
        self.hp = self.hp - dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp
        print("You died!")

    def choose_action(self):
        index = 1
        print("ACTIONS: ")
        for index in self.action:
            print(f"{index}. {value}")
        #for element in self.action:
            #print("{}. {}".format(index, element))
            #index = index + 1








#generate_dmg() #return a attack damage value, randomly between atk_high and atk_low
#take_dmg() #take into a damage value and calculate the HP loss and return new HP points
#choose_action() #print out all the action options in the action list, at this stage is to print out from ["Attack"]

#Game Play:

#
#
# def take_damage(self, dmg):
#     self.hp = self.hp - dmg
#     if self.hp < 0:
#         self.hp = 0
#     return self.hp
#
# def choose_action(self):
#     number = 1
#     print("\t\tACTIONS: ")
#     for element in self.action:
#         print(f"\t\t\t{number}: {element}")
#         number = number + 1
#
# def get_stat(self):
#     print(f"\t\t {self.name.upper()}")
#     print(f"\t\t\t {self.hp}/{self.maxhp}")
#     print(f"\t\t\t {self.mp}/{self.maxmp}")
