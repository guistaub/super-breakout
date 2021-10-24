import pygame
from pygame import Vector2
from state import GameStateObserver


class Layer(GameStateObserver):
    def unitDestroyed(self, unit):
        pass

    def renderTile(self, window, tile, color):
        pygame.draw.rect(
            window,
            color,
            (tile.position, Vector2(tile.width, tile.height)),
        )

    def render(self, window):
        raise NotImplementedError()
