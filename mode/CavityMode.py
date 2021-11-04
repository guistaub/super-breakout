from properties import CAVITY
from .PlayGameMode import PlayGameMode


class CavityMode(PlayGameMode):
    def __init__(self):
        super().__init__()

        # Game Mode
        self.gameMode = CAVITY

        # Game State
        self.gameState.loadCavity()
