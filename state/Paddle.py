from .GameItem import GameItem
from properties import PADDLE_PROPERTIES


class Paddle(GameItem):
    def __init__(self, state, position):
        super().__init__(state, position)
        self.height = PADDLE_PROPERTIES["height"]
        self.width = PADDLE_PROPERTIES["width"]
        self.type = PADDLE_PROPERTIES["type"]

    def move(self, moveVector):
        newPaddlePos = self.position + moveVector

        if newPaddlePos.x < 0 or newPaddlePos.x >= self.state.bounds.x - self.width:
            return

        self.position = newPaddlePos
