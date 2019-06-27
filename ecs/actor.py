import constants
from map.game_map import GameMap

class ObjActor:
    def __init__(self, x, y, name_object, sprite, creature=None, ai=None):
        self.x = x  # map address
        self.y = y  # map address
        self.sprite = sprite

        self.creature = creature
        if creature:
            creature.owner = self

        self.ai = ai
        if ai:
            ai.owner = self

    def draw(self, surface_main):
        surface_main.blit(self.sprite, (self.x * constants.CELL_WIDTH, self.y * constants.CELL_HEIGHT))

    def move(self, directions):
        dx, dy = directions
        self.x += dx
        self.y += dy
