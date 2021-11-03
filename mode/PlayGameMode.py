from properties import (
    BALL_PROPERTIES,
    TILE_PROPERTIES,
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
from layer import BallLayer, TileLayer, PaddleLayer, ScoreLayer


class PlayGameMode(GameMode):
    def __init__(self):
        super().__init__()
        # Game State
        self.gameState = GameState()
        self.layers = []

        # Game Mode
        self.gameMode = None

        # Layers
        self.layers = [
            BallLayer(self.gameState, self.gameState.balls),
            TileLayer(self.gameState, self.gameState.tiles),
            PaddleLayer(self.gameState, self.gameState.paddles),
            ScoreLayer(self.gameState),
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
            moveVector.x += 10
        elif keys[pygame.K_LEFT]:
            moveVector.x -= 10

        for paddle in self.gameState.paddles:
            self.commands.append(MovePaddleCommand(self.gameState, paddle, moveVector))

        for ball in self.gameState.balls:
            print(ball.status)
            self.commands.append(MoveBallCommand(self.gameState, ball))

            self.commands.append(ShiftBallDirectionCommand(self.gameState, ball))

            for paddle in self.gameState.paddles:
                self.commands.append(
                    CollisionDetectedCommand(
                        self.gameState, ball, paddle, self.gameMode
                    )
                )

            for tile in self.gameState.tiles:
                self.commands.append(
                    CollisionDetectedCommand(self.gameState, ball, tile, self.gameMode)
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
