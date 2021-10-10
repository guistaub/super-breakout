from .GameItem import GameItem
from properties import BALL_PROPERTIES, WINDOW_PROPERTIES


class Ball(GameItem):
    def __init__(self, state, position):
        super().__init__(state, position)
        self.height = BALL_PROPERTIES["height"]
        self.width = BALL_PROPERTIES["width"]
        self.type = BALL_PROPERTIES["type"]

    def move(self, moveVector):
        newBallPos = self.position + moveVector

        if newBallPos.x < 0 or newBallPos.x + self.width > WINDOW_PROPERTIES["width"]:
            return

        if newBallPos.y < 0 or newBallPos.y + self.height > WINDOW_PROPERTIES["height"]:
            return

        self.position = newBallPos
