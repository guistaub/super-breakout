import pygame
from .GameMode import GameMode
from database import getPlayerData
from properties import (
    CARTOON_FONT,
    CLASSIC,
    CAVITY,
    COLORS,
    PROGRESSIVE,
    WINDOW_PROPERTIES,
)
from utils import loadFont


class ScoreboardMode(GameMode):
    def __init__(self):
        super().__init__()

        self.font = loadFont(CARTOON_FONT, 15)

        self.classicScores = getPlayerData(CLASSIC)

        self.cavityScores = getPlayerData(CAVITY)

        self.progressiveScores = getPlayerData(PROGRESSIVE)

    def renderClassicScores(self, window):
        titleSurface = self.font.render(CLASSIC, True, COLORS["RED"])
        x = WINDOW_PROPERTIES["width"] // 6 - titleSurface.get_width()
        y = 100
        window.blit(titleSurface, (x, y))
        for index, score in enumerate(self.classicScores):
            if index == 10:
                break
            scoreString = score[0] + " - " + str(score[1])
            scoreSurface = self.font.render(scoreString, True, COLORS["RED"])
            y += titleSurface.get_height() * 2
            window.blit(scoreSurface, (x, y))

    def renderCavityScores(self, window):
        titleSurface = self.font.render(CAVITY, True, COLORS["RED"])
        x = WINDOW_PROPERTIES["width"] // 2 - titleSurface.get_width()
        y = 100
        window.blit(titleSurface, (x, y))
        for index, score in enumerate(self.cavityScores):
            if index == 10:
                break
            scoreString = score[0] + " - " + str(score[1])
            scoreSurface = self.font.render(scoreString, True, COLORS["RED"])
            y += titleSurface.get_height() * 2
            window.blit(scoreSurface, (x, y))

    def renderProgressiveScores(self, window):
        titleSurface = self.font.render(PROGRESSIVE, True, COLORS["RED"])
        x = WINDOW_PROPERTIES["width"] // 6 * 5 - titleSurface.get_width()
        y = 100
        window.blit(titleSurface, (x, y))
        for index, score in enumerate(self.progressiveScores):
            if index == 10:
                break
            scoreString = score[0] + " - " + str(score[1])
            scoreSurface = self.font.render(scoreString, True, COLORS["RED"])
            y += titleSurface.get_height() * 2
            window.blit(scoreSurface, (x, y))

    def processInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.notifyQuitRequested()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.notifyShowMenuRequested()

    def update(self):
        pass

    def render(self, window):
        self.renderClassicScores(window)
        self.renderCavityScores(window)
        self.renderProgressiveScores(window)
