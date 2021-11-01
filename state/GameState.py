from pygame.math import Vector2
from .Tile import Tile
from .Ball import Ball
from .Paddle import Paddle
from properties import (
    WINDOW_PROPERTIES,
    BALL_PROPERTIES,
    PADDLE_PROPERTIES,
    TILE_GRID_PROPERTIES,
)


class GameState:
    def __init__(self):
        self.__observers = []
        self.bounds = Vector2(WINDOW_PROPERTIES["width"], WINDOW_PROPERTIES["height"])
        self.balls = []
        self.paddles = []
        self.tiles = []

    def addObserver(self, observer):
        self.__observers.append(observer)

    def loadClassic(self):
        windowX = WINDOW_PROPERTIES["width"]

        ballXStart = (windowX - BALL_PROPERTIES["width"]) // 2
        self.balls.append(Ball(self, Vector2(ballXStart, 500), Vector2(4, -4)))
        self.balls.append(Ball(self, Vector2(ballXStart, 500), Vector2(2, -4)))
        self.balls.append(Ball(self, Vector2(ballXStart, 500), Vector2(4, 2)))

        paddlesXStart = (windowX - PADDLE_PROPERTIES["width"]) // 2
        self.paddles.append(Paddle(self, Vector2(paddlesXStart, 700)))
        self.paddles.append(Paddle(self, Vector2(paddlesXStart, 800)))

        self.drawTiles()

    def isAabbCollision(self, ball, element):
        xCollision = (ball.position.x < (element.position.x + element.width)) and (
            ball.width + ball.position.x > element.position.x
        )
        yCollision = (ball.position.y < element.position.y + element.height) and (
            ball.height + ball.position.y > element.position.y
        )
        return xCollision and yCollision

    def isInsideBounds(self, position, element):
        return (
            position.x >= 0
            and position.x + element.width <= self.bounds.x
            and position.y >= 0
            and position.y + element.height <= self.bounds.y
        )

    def drawTiles(self):
        x = TILE_GRID_PROPERTIES["X_START"]
        y = TILE_GRID_PROPERTIES["Y_START"]
        for i in range(TILE_GRID_PROPERTIES["ROWS"]):
            for j in range(TILE_GRID_PROPERTIES["COLS"]):
                tile = Tile(self, Vector2(x, y))
                self.tiles.append(tile)
                x += TILE_GRID_PROPERTIES["SPACING"] + tile.width
            y += TILE_GRID_PROPERTIES["SPACING"] + tile.height
            x = TILE_GRID_PROPERTIES["X_START"]

    def notifyBallDirectionChanged(self, ball):
        for observer in self.__observers:
            observer.ballDirectionChanged(ball)

    def notifyElementDestroyed(self, element):
        for observer in self.__observers:
            observer.elementDestroyed(element)
