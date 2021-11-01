from .Command import Command
from properties import UNIT_STATUS_ALIVE, WINDOW_PROPERTIES, BALL_PROPERTIES


class ShiftBallDirectionCommand(Command):
    def __init__(self, gameState, ball):
        self.gameState = gameState
        self.ball = ball
        # self.ball.movementVector = ball.movementVector

    def run(self):
        if self.ball.status != UNIT_STATUS_ALIVE:
            return

        newBallPos = self.ball.position + self.ball.movementVector

        if not self.gameState.isInsideBounds(newBallPos, self.ball):
            if (
                newBallPos.x < 0
                or newBallPos.x + BALL_PROPERTIES["width"] > WINDOW_PROPERTIES["width"]
            ):
                self.ball.movementVector.x = -self.ball.movementVector.x
            elif (
                newBallPos.y < 0
                or newBallPos.y + BALL_PROPERTIES["height"]
                > WINDOW_PROPERTIES["height"]
            ):
                self.ball.movementVector.y = -self.ball.movementVector.y
