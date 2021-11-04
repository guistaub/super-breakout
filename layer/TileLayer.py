from .Layer import Layer
from properties import COLORS


class TileLayer(Layer):
    def __init__(self, gameState):
        self.gameState = gameState

    def render(self, window):
        for tile in self.gameState.getActiveTiles():
            self.renderElement(window, tile, COLORS["GREEN"])
