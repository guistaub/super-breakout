import pygame
from pygame import event
from pygame.locals import *

class App():

    def __init__(self) -> None:
        self.height = 500
        self.width = 500
        self._game_running = True

    def get_game_status(self):
        return self._game_running
    
    def set_game_status(self, status):
        self._game_running = status

    def run_app(self):
        pygame.init()
        window = pygame.display.set_mode((self.width, self.height))

        while self._game_running:
            event_list = pygame.event.get()
            for event in event_list:
                if event.type == pygame.QUIT:
                    game_running = self.set_game_status(False)
            pygame.display.update()

        pygame.quit()
