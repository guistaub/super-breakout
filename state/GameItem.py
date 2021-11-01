from pygame import Rect
from properties import UNIT_STATUS_ALIVE


class GameItem(Rect):
    def __init__(self, state, position):
        self.state = state
        self.status = UNIT_STATUS_ALIVE
        self.position = position
        self.height = 0
        self.width = 0
