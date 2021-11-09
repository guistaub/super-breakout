from .GameMode import GameMode
import pygame
from database import writePlayerData
from utils import loadFont, loadSound
from properties import CARTOON_FONT, COLORS, WINDOW_PROPERTIES, KEYBOARD_CLICKING_SOUND


class PlayerNameInputMode(GameMode):
    def __init__(self, score, gameMode):
        super().__init__()

        self.font = loadFont(CARTOON_FONT, 30)

        self.keyboardSound = loadSound(KEYBOARD_CLICKING_SOUND)
        self.keyboardSound.set_volume(0.2)

        self.gameMode = gameMode

        self.score = score
        self.name = ""

    def processInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.notifyQuitRequested()
            elif event.type == pygame.KEYDOWN:
                self.keyboardSound.play()
                if event.key == pygame.K_RETURN:
                    writePlayerData(self.name, self.score, self.gameMode)
                    self.notifyShowMenuRequested()
                if event.key == pygame.K_BACKSPACE:
                    self.name = ""
                else:
                    self.name += chr(event.key)

    def update(self):
        pass

    def render(self, window):
        surface = self.font.render("Name: ", True, COLORS["RED"])
        positionX = WINDOW_PROPERTIES["width"] // 2
        positionY = WINDOW_PROPERTIES["height"] // 2
        window.blit(surface, (positionX, positionY))

        inputSurface = self.font.render(self.name, True, COLORS["RED"])
        inputX = positionX + surface.get_width()
        window.blit(inputSurface, (inputX, positionY))
