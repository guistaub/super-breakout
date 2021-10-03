from pygame.math import Vector2

from state.properties import PADDLE_PROPERTIES
from .Paddle import Paddle
from .properties import *


class GameState:
    def __init__(self, bounds):
        self.bounds = bounds
        paddleX = int(self.bounds.x / 2)
        paddleWidth = PADDLE_PROPERTIES["width"]
        self.elements = [
            Paddle(self, Vector2(paddleX - paddleWidth, 700)),
            Paddle(self, Vector2(paddleX - paddleWidth, 800)),
        ]

    def update(self, moveCommand):
        for element in self.elements:
            element.move(moveCommand)
