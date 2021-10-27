from .Layer import Layer
from properties import COLORS


class BallLayer(Layer):
    def __init__(self, gameState, balls):
        self.gameState = gameState
        self.balls = balls

    def ballDirectionChanged(self, ball):
        pass

    def render(self, window):
        for ball in self.balls:
            self.renderElement(window, ball, COLORS["RED"])
