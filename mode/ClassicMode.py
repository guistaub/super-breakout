from .PlayGameMode import PlayGameMode
from state import GameState
import pygame
from layer import BallLayer, PaddleLayer, TileLayer


class ClassicMode(PlayGameMode):
    def __init__(self):
        super().__init__()

        # Game State
        self.gameState.loadClassic()
