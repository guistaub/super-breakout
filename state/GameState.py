from pygame.math import Vector2
from .Tile import Tile
from .Ball import Ball
from .Paddle import Paddle
from properties import (
    WINDOW_PROPERTIES,
    BALL_PROPERTIES,
    PADDLE_PROPERTIES,
    TILE_GRID_PROPERTIES,
    UNIT_STATUS_ALIVE,
)
from random import randint


class GameState:
    def __init__(self):
        self.__observers = []
        self.bounds = Vector2(WINDOW_PROPERTIES["width"], WINDOW_PROPERTIES["height"])
        self._balls = []
        self._paddles = []
        self._tiles = []
        self.cavitySpawnBallsPositions = []
        self.paddleMoventSpeed = 0

    def addObserver(self, observer):
        self.__observers.append(observer)

    def getActiveBalls(self):
        return self._balls

    def addTile(self, position):
        self._tiles.append(Tile(self, position))

    def addBall(self, position, movementVector):
        self._balls.append(Ball(self, position, movementVector))

    def removeDestroyedBalls(self):
        self._balls = [ball for ball in self._balls if ball.status == UNIT_STATUS_ALIVE]

    def getActiveTiles(self):
        return self._tiles

    def removeDestroyedTiles(self):
        self._tiles = [tile for tile in self._tiles if tile.status == UNIT_STATUS_ALIVE]

    def getActivePaddles(self):
        return self._paddles

    def addPaddle(self, position):
        self._paddles.append(Paddle(self, position))

    def setPaddleMovementSpeed(self, value):
        self.paddleMoventSpeed += value

    def loadBaseGame(self):
        ballXStart = (self.bounds.x - BALL_PROPERTIES["width"]) // 2
        self.addBall(Vector2(ballXStart, 500), Vector2(4, -4))
        paddlesXStart = (self.bounds.x - PADDLE_PROPERTIES["width"]) // 2
        self.addPaddle(Vector2(paddlesXStart, 800))
        self.drawTiles()
        self.paddleMoventSpeed = 10

    def loadClassic(self):
        self.loadBaseGame()
        paddlesXStart = (self.bounds.x - PADDLE_PROPERTIES["width"]) // 2
        self.addPaddle(Vector2(paddlesXStart, 700))

    def loadCavity(self):
        self.loadBaseGame()
        paddlesXStart = (self.bounds.x - PADDLE_PROPERTIES["width"]) // 2
        self.addPaddle(Vector2(paddlesXStart, 700))
        indexes = []
        for _ in range(2):
            selectedIndex = -1
            while selectedIndex not in indexes and selectedIndex < 0:
                selectedIndex = randint(0, len(self.getActiveTiles()) - 1)
            self.cavitySpawnBallsPositions.append(
                self.getActiveTiles()[
                    randint(0, len(self.getActiveTiles()) - 1)
                ].position
            )

    def loadProgressive(self):
        self.loadBaseGame()

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
                self._tiles.append(tile)
                x += TILE_GRID_PROPERTIES["SPACING"] + tile.width
            y += TILE_GRID_PROPERTIES["SPACING"] + tile.height
            x = TILE_GRID_PROPERTIES["X_START"]

    def notifyElementDestroyed(self, element):
        for observer in self.__observers:
            observer.elementDestroyed(element)

    def notifyCollisionDetected(self):
        for observer in self.__observers:
            observer.collisionDetected()

    def notifyNewBallAdded(self):
        for observer in self.__observers:
            observer.newBallAdded()
