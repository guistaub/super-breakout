from .Command import Command


class CollisionDetectedCommand(Command):
    def __init__(self, gameState, ball, element):
        self.gameState = gameState
        self.ball = ball
        self.element = element
