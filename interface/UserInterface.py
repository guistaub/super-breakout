import pygame
from pygame.locals import *
from mode.MenuGameMode import MenuGameMode
from state import GameState
from pygame.math import Vector2
from properties import COLORS, WINDOW_PROPERTIES
from utils import loadImage
from mode import GameModeObserver


class UserInterface(GameModeObserver):
    def __init__(self):
        pygame.init()

        # Game State
        windowSize = Vector2(WINDOW_PROPERTIES["width"], WINDOW_PROPERTIES["height"])
        # Render properties

        # Window
        self.window = pygame.display.set_mode((int(windowSize.x), int(windowSize.y)))
        self.gameState = GameState(windowSize, self.window)
        pygame.display.set_caption("Super PyBreakout!")
        # pygame.display.set_icon(pygame.image.load("assets/icon.jpeg"))
        pygame.display.set_icon(loadImage("icon.jpeg"))
        # Loop properties
        self.clock = pygame.time.Clock()
        self.running = True
        self.moveCommand = Vector2(0, 0)
        # Game mode
        self.playGameMode = None
        self.overlayGameMode = MenuGameMode()
        self.overlayGameMode.addObserver(self)
        self.currentActiveMode = "Overlay"

    def processInput(self):
        self.moveCommand = Vector2(0, 0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.moveCommand.x = 5
        elif keys[pygame.K_LEFT]:
            self.moveCommand.x = -5
        # elif keys[pygame.K_DOWN]:
        #     self.moveCommand.y = 1
        # elif keys[pygame.K_UP]:
        #     self.moveCommand.y = -1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    break
                elif event.key == pygame.K_RIGHT:
                    self.moveCommand.x = 5
                elif event.key == pygame.K_LEFT:
                    self.moveCommand.x = -5
                # elif event.key == pygame.K_DOWN:
                #     self.moveCommand.y = 1
                # elif event.key == pygame.K_UP:
                #     self.moveCommand.y = -1

    def update(self):
        self.gameState.update(self.moveCommand)

    def renderElements(self, element, color):
        pygame.draw.rect(
            self.window,
            color,
            (element.position, Vector2(element.width, element.height)),
        )

    def render(self):
        self.window.fill(COLORS["BLACK"])
        for element in self.gameState.elements:
            if element.type == "paddle":
                self.renderElements(element, COLORS["WHITE"])
            elif element.type == "ball":
                self.renderElements(element, COLORS["RED"])
            elif element.type == "tile":
                self.renderElements(element, COLORS["GREEN"])
        # pygame.draw.rect(self.window, (255, 0, 0), (self.gameState.tilePos, (128, 40)))
        # pygame.draw.circle(self.window, (255, 0, 0), self.gameState.ballPos, 32)
        pygame.display.update()

    def run(self):
        while self.running:
            # if self.currentActiveMode == "Overlay":
            #     self.overlayGameMode.processInput()
            #     self.overlayGameMode.update()
            self.processInput()
            self.update()
            self.render()
            self.clock.tick(60)
