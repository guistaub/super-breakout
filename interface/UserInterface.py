import pygame
from pygame.locals import *
from mode.MenuGameMode import MenuGameMode
from state import GameState
from pygame.math import Vector2
from properties import COLORS, WINDOW_PROPERTIES, GAME_MODES
from utils import loadImage
from mode import GameModeObserver


class UserInterface(GameModeObserver):
    def __init__(self):
        pygame.init()
        windowSize = Vector2(WINDOW_PROPERTIES["width"], WINDOW_PROPERTIES["height"])

        # Window
        self.window = pygame.display.set_mode((int(windowSize.x), int(windowSize.y)))
        self.gameState = GameState(windowSize, self.window)
        pygame.display.set_caption("Super PyBreakout!")
        pygame.display.set_icon(loadImage("icon.jpeg"))

        # Loop properties
        self.clock = pygame.time.Clock()
        self.running = True

        # Game mode
        self.playGameMode = None
        self.overlayGameMode = MenuGameMode()
        self.overlayGameMode.addObserver(self)
        self.currentActiveMode = GAME_MODES["OVERLAY"]

    def quitRequested(self):
        self.running = False

    def run(self):
        while self.running:
            self.window.fill(COLORS["BLACK"])
            if self.currentActiveMode == GAME_MODES["OVERLAY"]:
                self.overlayGameMode.processInput()
                self.overlayGameMode.update()
                self.overlayGameMode.render(self.window)

            pygame.display.update()
            self.clock.tick(60)
