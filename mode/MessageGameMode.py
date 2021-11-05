from .GameMode import GameMode
from utils import loadFont
from properties import CARTOON_FONT, COLORS
import pygame


class MessageGameMode(GameMode):
    def __init__(self, message):
        super().__init__()

        # Fonts
        self.font = loadFont(CARTOON_FONT, 30)
        self.message = message

    def processInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.notifyQuitRequested()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.notifyQuitRequested()
                elif event.key == pygame.K_RETURN:
                    self.notifyShowMenuRequested()

    def update(self):
        pass

    def render(self, window):
        surface = self.font.render(self.message, True, COLORS["RED"])
        x = (window.get_width() - surface.get_width()) // 2
        y = (window.get_height() - surface.get_height()) // 2
        window.blit(surface, (x, y))
