from .Command import Command
from pygame import Vector2


class MovePaddleCommand(Command):
    def __init__(self, gameState, paddle, moveVector=Vector2(0, 0)):
        self.gameState = gameState
        self.paddle = paddle
        self.moveVector = moveVector

    def run(self):
        newPos = self.paddle.position + self.moveVector
        if self.gameState.isInsideBounds(newPos, self.paddle):
            self.paddle.position = newPos
