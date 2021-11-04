from .Command import Command


class DeleteDestroyedCommand(Command):
    def __init__(
        self,
        gameState,
    ):
        self.gameState = gameState

    def run(self):
        self.gameState.removeDestroyedBalls()
        self.gameState.removeDestroyedTiles()
