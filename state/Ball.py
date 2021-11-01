from pygame import Vector2
from .GameItem import GameItem
from properties import BALL_PROPERTIES


class Ball(GameItem):
    def __init__(self, state, position, movementVector):
        super().__init__(state, position)
        self.height = BALL_PROPERTIES["height"]
        self.width = BALL_PROPERTIES["width"]
        self.type = BALL_PROPERTIES["type"]
        self.movementVector = movementVector
