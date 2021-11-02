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

    def getRelativePosition(self):
        if (
            abs(self.ball.getCenter().y - self.element.getCenter().y) <= 15
            and abs(self.ball.getCenter().x - self.element.getCenter().x) >= 70
        ):
            self.horizontalBallShift()
        elif (
            abs(self.ball.getCenter().y - self.element.getCenter().y) > 15
            and abs(self.ball.getCenter().x - self.element.getCenter().x) < 70
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
