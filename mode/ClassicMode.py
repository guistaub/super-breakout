from .GameMode import GameMode
import pygame


class ClassicMode(GameMode):
    def __init__(self):
        super().__init__()

    def processInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.notifyQuitRequested()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.notifyShowMenuRequested()

    def update(self):
        pass

    def render(self, window):
        pygame.draw.circle(window, (255, 255, 255), (200, 200), 40)
