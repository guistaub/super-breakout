from .Layer import Layer
from properties import COLORS


class PaddleLayer(Layer):
    def __init__(self, gameState):
        self.gameState = gameState

    def render(self, window):
        for paddle in self.gameState.getActivePaddles():
            self.renderElement(window, paddle, COLORS["WHITE"])
