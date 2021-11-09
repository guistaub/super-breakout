from .PlayGameMode import PlayGameMode
from properties import PROGRESSIVE


class ProgressiveMode(PlayGameMode):
    def __init__(self):
        super().__init__()

        self.gameMode = PROGRESSIVE

        self.gameState.loadProgressive()

    def update(self):
        for command in self.commands:
            command.run()
        self.commands.clear()

        if len(self.gameState.getActiveTiles()) == 30:
            self.gameState.setPaddleMovementSpeed(5)

        if (
            len(self.gameState.getActiveBalls()) > 0
            and len(self.gameState.getActiveTiles()) == 0
        ):
            self.gameState.drawTiles()

            # Plays sound for adding new tiles
            self.gameState.notifyNewBallAdded()

        if len(self.gameState.getActiveBalls()) == 0:
            self.notifyGameLost()
