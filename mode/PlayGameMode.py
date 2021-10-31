from command.DeleteBallVectorCommand import DeleteBallVectorCommand
from properties import BALL_PROPERTIES, WINDOW_PROPERTIES, UNIT_STATUS_DESTROYED
from .GameMode import GameMode
from state import GameState
import pygame
from pygame import Vector2
from command import (
    MovePaddleCommand,
    MoveBallCommand,
    ShiftBallDirectionCommand,
    DeleteDestroyedCommand,
)


class PlayGameMode(GameMode):
    def __init__(self):
        super().__init__()
        self.gameState = GameState()
        self.layers = []
        self.commands = []

    def processInput(self):

        if len(self.gameState.balls) > 0 and len(self.gameState.tiles) == 0:
            self.notifyGameWon()

        if len(self.gameState.balls) == 0:
            self.notifyGameLost()

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

        for index, ball in enumerate(self.gameState.balls):
            self.commands.append(
                MoveBallCommand(self.gameState, ball, self.gameState.ballVectors[index])
            )

            if (
                ball.position.y + BALL_PROPERTIES["height"]
                >= WINDOW_PROPERTIES["height"]
            ):
                ball.status = UNIT_STATUS_DESTROYED
                self.commands.append(DeleteBallVectorCommand(self.gameState, index))

            self.commands.append(
                DeleteDestroyedCommand(self.gameState, BALL_PROPERTIES["type"])
            )
            self.commands.append(
                ShiftBallDirectionCommand(
                    self.gameState, ball, self.gameState.ballVectors[index]
                )
            )

        for tile in self.gameState.tiles:
            pass

    def update(self):
        for command in self.commands:
            command.run()
        self.commands.clear()

    def render(self, window):
        for layer in self.layers:
            layer.render(window)
