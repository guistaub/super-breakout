from .Command import Command
from properties import UNIT_STATUS_ALIVE, WINDOW_PROPERTIES, BALL_PROPERTIES


class ShiftBallDirectionCommand(Command):
    def __init__(self, gameState, ball, moveBallVector):
        self.gameState = gameState
        self.ball = ball
        self.moveBallVector = moveBallVector

    def run(self):
        if self.ball.status != UNIT_STATUS_ALIVE:
            return

        newBallPos = self.ball.position + self.moveBallVector

        if not self.gameState.isInsideBounds(newBallPos, self.ball):
            if (
                newBallPos.x < 0
                or newBallPos.x + BALL_PROPERTIES["width"] > WINDOW_PROPERTIES["width"]
            ):
                self.moveBallVector.x = -self.moveBallVector.x
            elif (
                newBallPos.y < 0
                or newBallPos.y + BALL_PROPERTIES["height"]
                > WINDOW_PROPERTIES["height"]
            ):
                self.moveBallVector.y = -self.moveBallVector.y
