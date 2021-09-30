from models import Ball, Tile
import pygame
from pygame.locals import *
from controllers import GameStateController
from .MenuView import MenuView

RED = (255, 0, 0, 255)
TILE_SPACING = 10


class GameView:
    def __init__(self):
        self.width = 1280
        self.height = 720

        # Game Window
        pygame.init()
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Super PyBreakout!")
        pygame.display.set_icon(pygame.image.load("assets/icon.jpeg"))

        # State Initialization
        self.menu = MenuView(self.window)
        self.state = GameStateController(self.width, self.height)
        self.ball = Ball(self.state, self.window, 640, 360)
        self.ball.setColor(255, 0, 0, 255)
        self.state.setBall(self.ball)
        # Game Modes

        # Loop
        self.clock = pygame.time.Clock()
        self.running = True
        self.isPlaying = False

    def quitRequested(self):
        self.running = False

    def showMenuRequested(self):
        self.isPlaying = False

    def playGameRequested(self):
        self.isPlaying = True

    def drawTileGroup(self, numberOfRows, numberOfColumns):
        tile = None
        top = 0
        left = 0
        for i in range(numberOfRows):
            left = 0
            top += 30 + TILE_SPACING
            for j in range(numberOfColumns):
                left += 100 + TILE_SPACING
                tile = Tile(self.state, self.window, left, top)
                tile.setColor(0, 200, 0, 255)
                tile.render()

    def processInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quitRequested()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    self.showMenuRequested()
                elif event.key == pygame.K_p:
                    self.playGameRequested()

    def update(self):
        self.state.updateBallPosition()
        self.ball.update(self.state)

    def render(self):
        self.window.fill((0, 0, 0))
        if self.isPlaying:
            self.ball.render()
            self.drawTileGroup(4, 9)
        else:
            self.menu.render()
        pygame.display.update()

    def run(self):
        while self.running:
            self.processInput()
            self.update()
            self.render()
            self.clock.tick(60)
        pygame.quit()
