from ecs.movement.movement_component import MovementComponent
from ecs.fov.fov_component import FovComponent
from constants import *
import pysnooper


class MovementSystem:
    def __init__(self, game_map):
        self.game_map = game_map

    def update(self, entities):
        for e in entities:
            self.move(e)

    def move(self, e):
        try:
            wall = self.game_map[e.get(MovementComponent).x][e.get(MovementComponent).y].block_path
            if e.get(MovementComponent).y < 0:
                wall = True
            if e.get(MovementComponent).x < 0:
                wall = True
        except IndexError:
            wall = True
        if not wall:
            e.get(FovComponent).fov_recalculate = True
            e.get(MovementComponent).cur_x = e.get(MovementComponent).x
            e.get(MovementComponent).cur_y = e.get(MovementComponent).y
        else:
            e.get(MovementComponent).x = e.get(MovementComponent).cur_x
            e.get(MovementComponent).y = e.get(MovementComponent).cur_y

