import pygame
from pygame.locals import *
from mode import (
    MenuGameMode,
    GameModeObserver,
    ClassicMode,
    CavityMode,
    ProgressiveMode,
)
from state import GameState
from pygame.math import Vector2
from properties import *
from utils import loadImage


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
        self.playGameModes = [CLASSIC, CAVITY, PROGRESSIVE]
        self.overlayGameMode = MenuGameMode()
        self.overlayGameMode.addObserver(self)
        self.currentActiveMode = OVERLAY

        # TODO add scoreboard game mode

    def showMenuRequested(self):
        self.currentActiveMode = OVERLAY

    def loadClassicRequested(self):
        self.currentActiveMode = CLASSIC
        self.playGameMode = ClassicMode()
        self.playGameMode.addObserver(self)

    def loadCavityRequested(self):
        # TODO implement cavity mode
        pass

    def loadProgressiveRequested(self):
        # TODO implement progressive mode
        pass

    def showScoreboardRequested(self):
        # TODO implement scoreboard
        pass

    def quitRequested(self):
        self.running = False

    def run(self):
        while self.running:
            self.window.fill(COLORS["BLACK"])
            if self.currentActiveMode == OVERLAY:
                self.overlayGameMode.processInput()
                self.overlayGameMode.update()
                self.overlayGameMode.render(self.window)
            elif self.currentActiveMode in self.playGameModes:
                self.playGameMode.processInput()
                self.playGameMode.update()
                self.playGameMode.render(self.window)
            # TODO add scoreboard game mode processing

            pygame.display.update()
            self.clock.tick(60)
