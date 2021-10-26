from .PlayGameMode import PlayGameMode
from state import GameState
import pygame
from layer import BallLayer, PaddleLayer, TileLayer
from command import MovePaddleCommand


class ClassicMode(PlayGameMode):
    def __init__(self):
        super().__init__()

        # Game State
        self.gameState.loadClassic()

        # Layers
        self.layers = [
            BallLayer(self.gameState, self.gameState.balls),
            TileLayer(self.gameState, self.gameState.tiles),
            PaddleLayer(self.gameState, self.gameState.paddles),
        ]

        # Observers
        for layer in self.layers:
            self.gameState.addObserver(layer)
