from .Command import Command
from properties import PADDLE_PROPERTIES, TILE_PROPERTIES, UNIT_STATUS_DESTROYED


class CollisionDetectedCommand(Command):
    def __init__(self, gameState, ball, element):
        self.gameState = gameState
        self.ball = ball
        self.element = element

    def horizontalBallShift(self):
        self.ball.movementVector.x = -self.ball.movementVector.x

    def verticalBallShift(self):
        self.ball.movementVector.y = -self.ball.movementVector.y

    def run(self):
        if self.gameState.isAabbCollision(self.ball, self.element):
            if self.element.type == PADDLE_PROPERTIES["type"]:
                self.verticalBallShift()
            elif self.element.type == TILE_PROPERTIES["type"]:
                self.element.status = UNIT_STATUS_DESTROYED
