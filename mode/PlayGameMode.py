from .GameMode import GameMode
from state import GameState
import pygame
from pygame import Vector2
from command import MovePaddleCommand


class PlayGameMode(GameMode):
    def __init__(self):
        super().__init__()
        self.gameState = GameState()
        self.layers = []
        self.commands = []

    def processInput(self):
        moveVector = Vector2(0, 0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.notifyQuitRequested()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.notifyShowMenuRequested()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            moveVector.x += 20
        elif keys[pygame.K_LEFT]:
            moveVector.x -= 20

        for paddle in self.gameState.paddles:
            self.commands.append(MovePaddleCommand(self.gameState, paddle, moveVector))

    def update(self):
        for command in self.commands:
            command.run()
        self.commands.clear()

    def render(self, window):
        for layer in self.layers:
            layer.render(window)
