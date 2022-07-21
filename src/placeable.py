class Placeable(object):
    def __init__(self, name, code, attack=0, defense=0, x=None, y=None):
        self.name = name
        self.code = code
        self.attack = attack
        self.defense = defense
        self.x = x
        self.y = y

    def __repr__(self):
        return self.name
