import os
from pathlib import Path

from .arena import Arena
from .item import Item
from .knight import Knight

BASE_DIR = Path(__file__).parent.parent


class World(object):
    def __init__(self):
        # Initialize arena
        self.arena = Arena()
        self.knights = []
        self.items = []

        self.initialize_knights()
        self.initialize_items()
        self.initialize_places()

    def initialize_knights(self):
        self.knights += [
            Knight("red", "R", x=0, y=0),
            Knight("blue", "B", x=7, y=0),
            Knight("green", "G", x=7, y=7),
            Knight("yellow", "Y", x=0, y=7),
        ]

    def initialize_items(self):
        self.items += [
            Item("magic_staff", "M", attack=1, defense=1, x=5, y=2),
            Item("helmet", "H", defense=1, x=5, y=5),
            Item("dagger", "D", attack=1, x=2, y=5),
            Item("axe", "A", attack=2, x=2, y=2),
        ]

    def initialize_places(self):
        self.arena.place_object(self.knights[0])
        self.arena.place_object(self.knights[1])
        self.arena.place_object(self.knights[2])
        self.arena.place_object(self.knights[3])

        self.arena.place_object(self.items[0])
        self.arena.place_object(self.items[1])
        self.arena.place_object(self.items[2])
        self.arena.place_object(self.items[3])

    def endgame(self):
        result = {}

        for knight in self.knights:
            result[knight.name] = [
                [knight.x, knight.y] if (knight.x >= 0 and knight.y >= 0) else None,
                knight.status,
                knight.item,
                knight.attack,
                knight.defense,
            ]

        for item in self.items:
            result[item.name] = [[item.x, item.y], item.equipped]

        return result
        # return self.arena.field

    def start_game(self):
        # return self.endgame()
        filename = os.path.join(BASE_DIR, "moves.txt")
        with open(filename) as f:
            line = f.readline().strip()

            if line.lower().endswith("start"):
                line = f.readline().strip()

                while not line.lower().endswith("end"):
                    code, instruction = line.split(":")

                    knight = next(knight for knight in self.knights if knight.code == code)
                    item = knight.item
                    self.arena.remove_object(knight, knight.x, knight.y)

                    prev_x, prev_y = knight.x, knight.y
                    x, y = knight.move(instruction)

                    try:
                        self.arena.place_object(knight, x, y)
                    except IndexError:
                        if item:
                            self.arena.remove_object(item, item.x, item.y)
                            self.arena.place_object(item, prev_x, prev_y)
                        knight.die(status="DROWNED")

                    line = f.readline().strip()

                return self.endgame()
            else:
                print("Invalid starting line, should be 'GAME-START'")
