import pygame
from pygame.locals import *
import os
import test

#Classe que inicializa o jogo

class App():

    def __init__(self) -> None:
        self.height = 500
        self.width = 500
        self._game_running = True
        self._caption = "Super PyBreakout!"
        self.icon = pygame.image.load("assets/icon.jpeg")

    def get_game_status(self) -> bool:
        return self._game_running
    
    def set_game_status(self, status) -> None:
        self._game_running = status

    def get_screen_caption(self) -> str:
        return self._caption

    def run_app(self) -> None:
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        pygame.display.set_caption(self.get_screen_caption())
        pygame.display.set_icon(self.icon)
        window = pygame.display.set_mode((self.width, self.height))



        while self._game_running:
            event_list = pygame.event.get()
            for event in event_list:
                if event.type == pygame.QUIT:
                    game_running = self.set_game_status(False)
            pygame.display.update()

        pygame.quit()


if __name__ == "__main__":
    
    test_app = App()

    test(test_app.get_game_status() == True, "Game Status Getter")
    test_app.set_game_status(False)
    test(test_app.get_game_status() == False, "Game Status Setter")

