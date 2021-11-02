from .Command import Command
from properties import (
    UNIT_STATUS_ALIVE,
    WINDOW_PROPERTIES,
    UNIT_STATUS_DESTROYED,
)


class MoveBallCommand(Command):
    def __init__(self, gameState, ball):
        self.gameState = gameState
        self.ball = ball

    def run(self):
        if self.ball.status != UNIT_STATUS_ALIVE:
            return

        newBallPos = self.ball.position + self.ball.movementVector

        if not self.gameState.isInsideBounds(newBallPos, self.ball):
            return

        if newBallPos.y + self.ball.height >= WINDOW_PROPERTIES["height"]:
            self.ball.status = UNIT_STATUS_DESTROYED
            self.gameState.notifyElementDestroyed(self.ball)
            return

        self.ball.position = newBallPos
