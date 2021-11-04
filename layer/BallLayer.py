from .Layer import Layer
from properties import COLORS


class BallLayer(Layer):
    def __init__(self, gameState):
        self.gameState = gameState

    def render(self, window):
        for ball in self.gameState.getActiveBalls():
            self.renderElement(window, ball, COLORS["RED"])
