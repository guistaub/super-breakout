import pygame
from pygame import Vector2
from state import GameStateObserver


class Layer(GameStateObserver):
    def unitDestroyed(self, unit):
        pass

    def renderElement(self, window, element, color):
        pygame.draw.rect(
            window,
            color,
            (element.position, Vector2(element.width, element.height)),
        )

    def render(self, window):
        raise NotImplementedError()
