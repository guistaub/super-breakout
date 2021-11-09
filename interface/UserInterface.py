import pygame
from mode.ScoreboardMode import ScoreboardMode
from properties import (
    MENU_MUSIC,
    GAME_START_MESSAGE,
    GAME_WON_JINGLE,
    GAME_LOST_JINGLE,
    GAME_WON_MESSAGE,
    GAME_LOST_MESSAGE,
    CLASSIC,
    PROGRESSIVE,
    CAVITY,
    SCOREBOARD,
)
from pygame.locals import *
from mode import (
    MenuGameMode,
    GameModeObserver,
    ClassicMode,
    CavityMode,
    ProgressiveMode,
    MessageGameMode,
    PlayerNameInputMode,
)
from pygame.math import Vector2
from properties import *
from utils import loadImage, loadSound


class UserInterface(GameModeObserver):
    def __init__(self):
        pygame.init()
        # TODO change window resolution
        windowSize = Vector2(WINDOW_PROPERTIES["width"], WINDOW_PROPERTIES["height"])

        # Window
        self.window = pygame.display.set_mode((int(windowSize.x), int(windowSize.y)))
        pygame.display.set_caption("Super PyBreakout!")
        pygame.display.set_icon(loadImage("icon.jpeg"))

        # Loop properties
        self.clock = pygame.time.Clock()
        self.running = True

        # Game mode
        self.playGameMode = None
        self.playGameModes = [CLASSIC, CAVITY, PROGRESSIVE, SCOREBOARD]
        self.overlayGameMode = MessageGameMode(GAME_START_MESSAGE)
        self.overlayGameMode.addObserver(self)
        self.currentActiveMode = OVERLAY

        # Music
        self.menuMusic = loadSound(MENU_MUSIC)
        self.menuMusic.set_volume(0.1)
        self.menuMusic.play()

        self.gameWonJingle = loadSound(GAME_WON_JINGLE)
        self.gameWonJingle.set_volume(0.2)

        self.gameLostJingle = loadSound(GAME_LOST_JINGLE)
        self.gameLostJingle.set_volume(0.2)

    def showMenuRequested(self):
        self.menuMusic.stop()
        self.currentActiveMode = OVERLAY
        self.overlayGameMode = MenuGameMode()
        self.overlayGameMode.addObserver(self)

    def gameWon(self):
        self.gameWonJingle.play()
        self.currentActiveMode = OVERLAY
        self.overlayGameMode = MessageGameMode(
            GAME_WON_MESSAGE, self.playGameMode.gameMode
        )
        self.overlayGameMode.addObserver(self)

    def gameLost(self):
        self.gameLostJingle.play()
        self.currentActiveMode = OVERLAY
        self.overlayGameMode = MessageGameMode(
            GAME_LOST_MESSAGE, self.playGameMode.gameMode
        )
        self.overlayGameMode.addObserver(self)

    def getPlayerInfo(self):
        self.currentActiveMode = OVERLAY
        score = self.playGameMode.gameState.score
        mode = self.playGameMode.gameMode
        self.overlayGameMode = PlayerNameInputMode(score, mode)
        self.overlayGameMode.addObserver(self)

    def loadClassicRequested(self):
        self.currentActiveMode = CLASSIC
        self.playGameMode = ClassicMode()
        self.playGameMode.addObserver(self)

    def loadCavityRequested(self):
        self.currentActiveMode = CAVITY
        self.playGameMode = CavityMode()
        self.playGameMode.addObserver(self)

    def loadProgressiveRequested(self):
        self.currentActiveMode = PROGRESSIVE
        self.playGameMode = ProgressiveMode()
        self.playGameMode.addObserver(self)

    def showScoreboardRequested(self):
        self.currentActiveMode = SCOREBOARD
        self.playGameMode = ScoreboardMode()
        self.playGameMode.addObserver(self)

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
