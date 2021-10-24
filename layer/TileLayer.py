from .Layer import Layer
from properties import COLORS


class TileLayer(Layer):
    def __init__(self, gameState, units):
        self.gameState = gameState
        self.units = units

    def render(self, window):
        for unit in self.units:
            if unit.type == "paddle":
                self.renderTile(window, unit, COLORS["WHITE"])
            elif unit.type == "tile":
                self.renderTile(window, unit, COLORS["GREEN"])
