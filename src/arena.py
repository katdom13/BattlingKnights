from .item import Item
from .knight import Knight


class Arena(object):
    def __init__(self, width=8, height=8):
        self.width = width
        self.height = height
        self.field = [[[] for i in range(self.width)] for j in range(self.height)]

    def remove_object(self, obj, x, y):
        cell = self.field[x][y]
        if x >= 0 and y >= 0:
            # Remove a knight's item as well
            if isinstance(obj, Knight) and obj.item:
                cell.remove(obj.item)
            cell.remove(obj)

    def place_object(self, obj, x=None, y=None):
        if x is None and y is None:
            x, y = obj.x, obj.y

        cell = self.field[x][y]
        if obj not in cell:
            if x >= 0 and y >= 0:
                cell.append(obj)
            obj.x = x
            obj.y = y

        if isinstance(obj, Knight):
            if x < 0 or y < 0:
                raise IndexError()

            # There are items present in the cell
            # Pick up an item
            items = [item for item in cell if isinstance(item, Item) and not item.equipped]
            if items:
                obj.choose_item(items)

            # There's another knignt present
            defender = next(
                (item for item in cell if isinstance(item, Knight) and not item.is_dead() and item != obj), None
            )
            if defender:
                attacker = obj
                self.battle(attacker, defender)

            # Finally, place the item in the same place as the knight
            if obj.item:
                self.place_object(obj.item, x, y)

    def battle(self, knight_a, knight_b):
        attack_value = knight_a.do_attack()
        defense_value = knight_b.do_defend()

        if attack_value > defense_value:
            knight_b.die()
        elif attack_value < defense_value:
            knight_a.die()
        else:
            knight_a.die()
            knight_b.die()
