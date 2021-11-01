from properties import (
    BALL_PROPERTIES,
    TILE_PROPERTIES,
    WINDOW_PROPERTIES,
    UNIT_STATUS_DESTROYED,
)
from .GameMode import GameMode
from state import GameState
import pygame
from pygame import Vector2
from command import (
    MovePaddleCommand,
    MoveBallCommand,
    ShiftBallDirectionCommand,
    DeleteDestroyedCommand,
    CollisionDetectedCommand,
)
from layer import BallLayer, TileLayer, PaddleLayer


class PlayGameMode(GameMode):
    def __init__(self):
        super().__init__()
        # Game State
        self.gameState = GameState()
        self.layers = []

        # Layers
        self.layers = [
            BallLayer(self.gameState, self.gameState.balls),
            TileLayer(self.gameState, self.gameState.tiles),
            PaddleLayer(self.gameState, self.gameState.paddles),
        ]

        # Observers
        for layer in self.layers:
            self.gameState.addObserver(layer)

        # Commands
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
            moveVector.x += 5
        elif keys[pygame.K_LEFT]:
            moveVector.x -= 5

        for paddle in self.gameState.paddles:
            self.commands.append(MovePaddleCommand(self.gameState, paddle, moveVector))

        for ball in self.gameState.balls:
            self.commands.append(MoveBallCommand(self.gameState, ball))

            if (
                ball.position.y + BALL_PROPERTIES["height"]
                >= WINDOW_PROPERTIES["height"]
            ):
                ball.status = UNIT_STATUS_DESTROYED

            self.commands.append(ShiftBallDirectionCommand(self.gameState, ball))

            for paddle in self.gameState.paddles:
                self.commands.append(
                    CollisionDetectedCommand(self.gameState, ball, paddle)
                )

            for tile in self.gameState.tiles:
                self.commands.append(
                    CollisionDetectedCommand(self.gameState, ball, tile)
                )

            self.commands.append(
                DeleteDestroyedCommand(self.gameState, BALL_PROPERTIES["type"])
            )
            self.commands.append(
                DeleteDestroyedCommand(self.gameState, TILE_PROPERTIES["type"])
            )

    def update(self):
        for command in self.commands:
            command.run()
        self.commands.clear()

        if len(self.gameState.balls) > 0 and len(self.gameState.tiles) == 0:
            self.notifyGameWon()

        if len(self.gameState.balls) == 0:
            self.notifyGameLost()

    def render(self, window):
        for layer in self.layers:
            layer.render(window)
