from .GameItem import GameItem
from properties import PADDLE_PROPERTIES


class Paddle(GameItem):
    def __init__(self, state, position):
        super().__init__(state, position)
        self.height = PADDLE_PROPERTIES["height"]
        self.width = PADDLE_PROPERTIES["width"]
        self.type = PADDLE_PROPERTIES["type"]
