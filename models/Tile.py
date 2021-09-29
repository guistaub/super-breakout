from .GameObject import GameObject
from pygame.draw import rect
from pygame import Rect


class Tile(GameObject):
    def __init__(self, state, window, left, top):
        super().__init__(state, window)
        self.width = 100
        self.height = 30
        self.left = left
        self.top = top

    def render(self):
        rect(
            self.window, self.color, Rect(self.left, self.top, self.width, self.height)
        )
