from .placeable import Placeable


class Item(Placeable):
    def __init__(self, name, code, attack=0, defense=0, x=None, y=None, equipped=False):
        super().__init__(name, code, attack, defense, x, y)
        self.equipped = equipped

    def equip_item(self):
        self.equipped = True
        return self.attack, self.defense
