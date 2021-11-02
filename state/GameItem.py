from pygame import Rect
from pygame.math import Vector2
from properties import UNIT_STATUS_ALIVE


class GameItem(Rect):
    def __init__(self, state, position):
        self.state = state
        self.status = UNIT_STATUS_ALIVE
        self.position = position
        self.height = 0
        self.width = 0

    def getCenter(self):
        x = self.position.x + (self.width // 2)
        y = self.position.y + (self.height // 2)
        return Vector2(x, y)
