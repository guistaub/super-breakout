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
from layer import BallLayer, TileLayer, PaddleLayer, ScoreLayer, SoundLayer
from properties import (
    BALL_ADDED_SOUND,
    ELEMENT_COLLISION_SOUND,
    ELEMENT_DESTROYED_SOUND,
)


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
            BallLayer(self.gameState),
            TileLayer(self.gameState),
            PaddleLayer(self.gameState),
            ScoreLayer(self.gameState),
            SoundLayer(
                ELEMENT_COLLISION_SOUND, ELEMENT_DESTROYED_SOUND, BALL_ADDED_SOUND
            ),
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
            moveVector.x += self.gameState.paddleMoventSpeed
        elif keys[pygame.K_LEFT]:
            moveVector.x -= self.gameState.paddleMoventSpeed

        for paddle in self.gameState.getActivePaddles():
            self.commands.append(MovePaddleCommand(self.gameState, paddle, moveVector))

        for ball in self.gameState.getActiveBalls():
            self.commands.append(MoveBallCommand(self.gameState, ball))

            self.commands.append(ShiftBallDirectionCommand(self.gameState, ball))

            for paddle in self.gameState.getActivePaddles():
                self.commands.append(
                    CollisionDetectedCommand(
                        self.gameState, ball, paddle, self.gameMode
                    )
                )

            for tile in self.gameState.getActiveTiles():
                self.commands.append(
                    CollisionDetectedCommand(self.gameState, ball, tile, self.gameMode)
                )

            self.commands.append(DeleteDestroyedCommand(self.gameState))

    def update(self):
        for command in self.commands:
            command.run()
        self.commands.clear()

        if (
            len(self.gameState.getActiveBalls()) > 0
            and len(self.gameState.getActiveTiles()) == 0
        ):
            self.notifyGameWon()

        if len(self.gameState.getActiveBalls()) == 0:
            self.notifyGameLost()

    def render(self, window):
        for layer in self.layers:
            layer.render(window)
