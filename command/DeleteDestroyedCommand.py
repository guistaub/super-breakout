from .Command import Command
from properties import (
    BALL_PROPERTIES,
    TILE_PROPERTIES,
    UNIT_STATUS_ALIVE,
    UNIT_STATUS_DESTROYED,
)


class DeleteDestroyedCommand(Command):
    def __init__(self, gameState, elementType):
        self.gameState = gameState
        self.elementType = elementType

    def run(self):
        if self.elementType == BALL_PROPERTIES["type"]:
            self.gameState.balls[:] = [
                ball
                for ball in self.gameState.balls
                if ball.status == UNIT_STATUS_ALIVE
            ]
        elif self.elementType == TILE_PROPERTIES["type"]:
            self.gameState.tiles[:] = [
                tile
                for tile in self.gameState.tiles
                if tile.status == UNIT_STATUS_ALIVE
            ]
