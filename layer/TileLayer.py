from .Layer import Layer
from properties import COLORS


class TileLayer(Layer):
    def __init__(self, gameState, tiles):
        self.gameState = gameState
        self.tiles = tiles

    def render(self, window):
        for tile in self.tiles:
            self.renderElement(window, tile, COLORS["GREEN"])
