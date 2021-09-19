import pygame
from pygame.locals import *
import os

#Classe que inicializa o jogo

class App():

    def __init__(self) -> None:
        self.height = 500
        self.width = 500
        self._game_running = True
        self._caption = "Super PyBreakout!"
        self.icon = pygame.image.load("assets/icon.jpeg")
        self._frame_rate = 60
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        pygame.display.set_caption(self.get_screen_caption())
        pygame.display.set_icon(self.icon)
        self.window = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

    def get_game_frame_rate(self):
        return self._frame_rate

    def get_game_status(self) -> bool:
        return self._game_running
    
    def set_game_status(self, status) -> None:
        self._game_running = status

    def get_screen_caption(self) -> str:
        return self._caption

    def run_app(self) -> None:
        while self._game_running:
            self.processInput()
            self.update()
            self.render()
            self.clock.tick(self.get_game_frame_rate())

        pygame.quit()

    def render(self):
        pygame.display.update()

    def update(self):
        pass

    def processInput(self):
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                game_running = self.set_game_status(False)

