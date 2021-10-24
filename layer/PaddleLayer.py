from .Layer import Layer
from properties import COLORS


class PaddleLayer(Layer):
    def __init__(self, gameState, paddles):
        self.gameState = gameState
        self.paddles = paddles

    def render(self, window):
        for paddle in self.paddles:
            self.renderElement(window, paddle, COLORS["WHITE"])
