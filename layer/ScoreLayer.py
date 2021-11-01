from .Layer import Layer
import pygame
from properties import (
    CARTOON_FONT,
    COLORS,
    WINDOW_PROPERTIES,
    BALL_PROPERTIES,
    TILE_PROPERTIES,
)


class ScoreLayer(Layer):
    def __init__(self, gameState):
        self.gameState = gameState
        self.scoreFont = pygame.font.Font(CARTOON_FONT, 30)

        self.score = 0

    def elementDestroyed(self, element):
        if element.type == TILE_PROPERTIES["type"]:
            self.score += 100
        elif element.type == BALL_PROPERTIES["type"]:
            self.score -= 100

    def render(self, window):
        scoreSurface = self.scoreFont.render(str(self.score), True, COLORS["RED"])
        scoreX = WINDOW_PROPERTIES["width"] - scoreSurface.get_width() - 10
        scoreY = WINDOW_PROPERTIES["height"] - scoreSurface.get_height() - 10
        window.blit(scoreSurface, (scoreX, scoreY))
