from .Layer import Layer
import pygame
from pygame.math import Vector2
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
        self.buffer = 0

    def elementDestroyed(self, element):
        if element.type == TILE_PROPERTIES["type"]:
            self.score += 100
            if self.buffer < 1000:
                self.buffer += 100
            else:
                self.buffer = 0

            self.incrementBallSpeed()
        elif element.type == BALL_PROPERTIES["type"]:
            self.score -= 100

    def incrementBallSpeed(self):
        if self.buffer == 1000:
            for ball in self.gameState.balls:
                if ball.movementVector.x > 0 and ball.movementVector.y > 0:
                    ball.movementVector += Vector2(1, 1)
                elif ball.movementVector.x < 0 and ball.movementVector.y < 0:
                    ball.movementVector += Vector2(-1, -1)
                elif ball.movementVector.x > 0 and ball.movementVector.y < 0:
                    ball.movementVector += Vector2(1, -1)
                elif ball.movementVector.x < 0 and ball.movementVector.y > 0:
                    ball.movementVector += Vector2(-1, 1)

    def render(self, window):
        scoreSurface = self.scoreFont.render(str(self.score), True, COLORS["RED"])
        scoreX = WINDOW_PROPERTIES["width"] - scoreSurface.get_width() - 10
        scoreY = WINDOW_PROPERTIES["height"] - scoreSurface.get_height() - 10
        window.blit(scoreSurface, (scoreX, scoreY))
