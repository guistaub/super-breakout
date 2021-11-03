from .Command import Command
from state import Ball
from properties import PADDLE_PROPERTIES, TILE_PROPERTIES, UNIT_STATUS_DESTROYED, CAVITY
from pygame.math import Vector2
from random import randint


class CollisionDetectedCommand(Command):
    def __init__(self, gameState, ball, element, gameMode):
        self.gameState = gameState
        self.ball = ball
        self.element = element
        self.gameMode = gameMode

    def horizontalBallShift(self):
        self.ball.movementVector.x = -self.ball.movementVector.x

    def verticalBallShift(self):
        self.ball.movementVector.y = -self.ball.movementVector.y

    def getRelativePosition(self):
        if (
            abs(self.ball.getCenter().y - self.element.getCenter().y) <= 15
            and abs(self.ball.getCenter().x - self.element.getCenter().x) >= 70
        ):
            self.horizontalBallShift()
        elif (
            abs(self.ball.getCenter().y - self.element.getCenter().y) > 15
            and abs(self.ball.getCenter().x - self.element.getCenter().x) < 75
        ):
            self.verticalBallShift()

    def run(self):
        if self.gameState.isAabbCollision(self.ball, self.element):
            if self.element.type == PADDLE_PROPERTIES["type"]:
                if self.ball.movementVector.y > 0:
                    self.verticalBallShift()

            elif self.element.type == TILE_PROPERTIES["type"]:
                self.getRelativePosition()
                self.element.status = UNIT_STATUS_DESTROYED
                self.gameState.notifyElementDestroyed(self.element)

                if (
                    self.gameMode == CAVITY
                    and self.element.position
                    in self.gameState.cavitySpawnBallsPositions
                ):
                    vectorX = 0
                    while vectorX == 0:
                        vectorX = randint(-5, 5)
                    vectorY = 0
                    while vectorY == 0:
                        vectorY = randint(-5, 5)
                    newBallList = self.gameState.balls[:]
                    newBallList.append(
                        Ball(
                            self.gameState,
                            self.element.position,
                            Vector2(vectorX, vectorY),
                        )
                    )
                    self.gameState.balls[:] = newBallList
