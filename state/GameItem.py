from pygame.draw import rect
from pygame.math import Vector2
from pygame import Rect


class GameItem(Rect):
    def __init__(self, state, position):
        self.state = state
        self.status = "alive"
        self.position = position
        self.type = None
        self.height = 0
        self.width = 0
        self.shape = Rect(self.position, (self.width, self.height))

    def move(self, moveVector):
        raise NotImplementedError

    def render(self, color):
        rect(self.window, color, self.shape)

    def getXBounds(self):
        x = self.position.x
        return x, x + self.width

    def getYBounds(self):
        y = self.position.y
        return y, y + self.height
