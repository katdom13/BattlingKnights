from random import random

from .item import Item
from .placeable import Placeable


class Knight(Placeable):
    def __init__(self, name, code, attack=1, defense=1, x=None, y=None, item=None, status="LIVE"):
        super().__init__(name, code, attack, defense, x, y)
        self.item = item
        self.status = status

    def is_dead(self):
        if self.status in ["DEAD", "DROWNED"]:
            return True

    def die(self, status="DEAD"):
        self.code = self.code.lower()
        self.attack = 0
        self.defense = 0

        if self.item:
            self.drop_item()

        self.status = status

    def move(self, dir):
        if not self.is_dead():
            if dir == "N":
                self.x -= 1
            elif dir == "S":
                self.x += 1
            elif dir == "E":
                self.y += 1
            elif dir == "W":
                self.y -= 1

            if self.item:
                self.item.x = self.x
                self.item.y = self.y

        return self.x, self.y

    def get_item(self, item):
        if not self.is_dead() and item and isinstance(item, Item):
            self.item = item
            atk, dfs = item.equip_item()

            self.attack += atk
            self.defense += dfs

    def drop_item(self):
        self.item.equipped = False
        self.item = None

    def choose_item(self, items):
        if not self.is_dead() and not self.item and items:
            item = items[::-1][0]
            self.item = item
            atk, dfs = item.equip_item()
            self.attack += atk
            self.defense += dfs

    def do_attack(self):
        bonus = 0.5 if random() < 0.5 else 0
        return self.attack + bonus

    def do_defend(self):
        return self.defense
