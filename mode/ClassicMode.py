from .PlayGameMode import PlayGameMode
from properties import CLASSIC


class ClassicMode(PlayGameMode):
    def __init__(self):
        super().__init__()

        self.gameMode = CLASSIC

        # Game State
        self.gameState.loadClassic()
