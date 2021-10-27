from .Command import Command
from properties import UNIT_STATUS_ALIVE


class MoveBallCommand(Command):
    def __init__(self, gameState, ball, moveVector):
        self.gameState = gameState
        self.ball = ball
        self.moveVector = moveVector

    def run(self):
        if self.ball.status != UNIT_STATUS_ALIVE:
            return

        newBallPos = self.ball.position + self.moveVector

        if not self.gameState.isInsideBounds(newBallPos, self.ball):
            return

        self.ball.position = newBallPos
