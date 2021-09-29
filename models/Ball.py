from models.GameObject import GameObject
from pygame.math import Vector2
from pygame.draw import circle


class Ball(GameObject):
    def __init__(self, state, window, x, y):
        super().__init__(state, window)
        self.radius = 25
        self.center = Vector2(x, y)

    def render(self):
        circle(self.window, self.color, self.center, self.radius)

    def update(self, state):
        self.center = Vector2(state.x, state.y)
