import pygame
from pygame.math import Vector2
from .Tile import Tile
from .Paddle import Paddle
from properties import *
from .Ball import Ball


class GameState:
    def __init__(self, bounds, window):
        self.bounds = bounds
        self.window = window
        screenCenterX = int(self.bounds.x / 2)
        halfPaddleWidth = PADDLE_PROPERTIES["width"] / 2
        halfBallWidth = BALL_PROPERTIES["width"] / 2
        self.gridSize = [2, 2]
        self.tileSpacing = 10
        self.tiles = []
        self.createTiles()
        self.elements = [
            Paddle(self, Vector2(screenCenterX - halfPaddleWidth, 700)),
            Paddle(self, Vector2(screenCenterX - halfPaddleWidth, 800)),
            Ball(self, Vector2(screenCenterX - halfBallWidth, 500)),
        ]
        self.elements.extend(self.tiles)
        # self.balls = [element for element in self.elements if element.type == "ball"]
        self.paddles = [
            element for element in self.elements if element.type == "paddle"
        ]
        self.moveBallVector = Vector2(4, -4)

    def update(self, moveCommand):
        collision = False
        for element in self.elements:
            if element.type == "paddle":
                element.move(moveCommand)
            elif element.type == "ball":
                for paddle in self.paddles:
                    collision = False
                    if self.isAabbCollision(element, paddle):
                        collision = True
                        if self.shouldBallShiftYDirection(element, paddle):
                            self.moveBallVector.y = -self.moveBallVector.y
                        element.move(self.moveBallVector)
                        break
                tileIndex = 0
                for tile in self.tiles:
                    collision = False
                    if self.isAabbCollision(element, tile):
                        collision = True
                        if self.shouldBallShiftXDirection(element, tile):
                            self.moveBallVector.x = -self.moveBallVector.x
                        if self.shouldBallShiftYDirection(element, tile):
                            self.moveBallVector.y = -self.moveBallVector.y
                        self.tiles.pop(tileIndex)
                        self.elements.pop(tileIndex + 3)
                        element.move(self.moveBallVector)
                    tileIndex += 1
                if not collision:
                    self.updateBallTrajectory(element)
                    element.move(self.moveBallVector)
                collision = False
            elif element.type == "tile":
                break

    def updateBallTrajectory(self, ball):
        newBallPos = ball.position + self.moveBallVector

        if newBallPos.x < 0 or newBallPos.x + ball.width > WINDOW_PROPERTIES["width"]:
            self.moveBallVector.x = -self.moveBallVector.x

        if newBallPos.y < 0 or newBallPos.y + ball.height > WINDOW_PROPERTIES["height"]:
            self.moveBallVector.y = -self.moveBallVector.y

    def isAabbCollision(self, obj1, obj2):
        xCollision = (obj1.position.x < (obj2.position.x + obj2.width)) and (
            obj1.width + obj1.position.x > obj2.position.x
        )
        yCollision = (obj1.position.y < obj2.position.y + obj2.height) and (
            obj1.height + obj1.position.y > obj2.position.y
        )
        return xCollision and yCollision

    def shouldBallShiftXDirection(self, obj1, obj2):
        # Right side cases

        # Obj1 is above obj2
        if (
            obj1.getCenter().x >= obj2.getCenter().x
            and obj1.getCenter().y <= obj2.getCenter().y - obj2.height / 2
        ):
            return False
        # Obj1 is on the upper right of obj2
        elif (
            obj1.getCenter().x >= obj2.getCenter().x
            and obj1.getCenter().y <= obj2.getCenter().y
        ):
            return True
        # Obj1 is below obj2
        elif (
            obj1.getCenter().x >= obj2.getCenter().x
            and obj1.getCenter().y > obj2.getCenter().y + obj2.height / 2
        ):
            return False
        # Obj1 is on the bottom right of obj2
        elif (
            obj1.getCenter().x >= obj2.getCenter().x
            and obj1.getCenter().y > obj2.getCenter().y
        ):
            return True

        # Left side cases

        # Obj1 is above obj2
        if (
            obj1.getCenter().x < obj2.getCenter().x
            and obj1.getCenter().y < obj2.getCenter().y - obj2.height / 2
        ):
            return False
        # Obj1 is on the upper left of obj2
        elif (
            obj1.getCenter().x < obj2.getCenter().x
            and obj1.getCenter().y < obj2.getCenter().y
        ):
            return True
        # Obj1 is below obj2
        elif (
            obj1.getCenter().x < obj2.getCenter().x
            and obj1.getCenter().y > obj2.getCenter().y + obj2.height / 2
        ):
            return False
        # Obj1 is on the bottom left of obj2
        elif (
            obj1.getCenter().x > obj2.getCenter().x
            and obj1.getCenter().y > obj2.getCenter().y
        ):
            return True

    def shouldBallShiftYDirection(self, obj1, obj2):
        # Right side cases

        # Obj1 is above obj2
        if (
            obj1.getCenter().x > obj2.getCenter().x
            and obj1.getCenter().y < obj2.getCenter().y - obj2.height / 2
        ):
            return True
        # Obj1 is on the upper right of obj2
        elif (
            obj1.getCenter().x > obj2.getCenter().x
            and obj1.getCenter().y < obj2.getCenter().y
        ):
            return False
        # Obj1 is below obj2
        elif (
            obj1.getCenter().x > obj2.getCenter().x
            and obj1.getCenter().y > obj2.getCenter().y + obj2.height / 2
        ):
            return True
        # Obj1 is on the bottom right of obj2
        elif (
            obj1.getCenter().x > obj2.getCenter().x
            and obj1.getCenter().y > obj2.getCenter().y
        ):
            return False

        # Left side cases

        # Obj1 is above obj2
        if (
            obj1.getCenter().x < obj2.getCenter().x
            and obj1.getCenter().y < obj2.getCenter().y - obj2.height / 2
        ):
            return True
        # Obj1 is on the upper left of obj2
        elif (
            obj1.getCenter().x < obj2.getCenter().x
            and obj1.getCenter().y < obj2.getCenter().y
        ):
            return False
        # Obj1 is below obj2
        elif (
            obj1.getCenter().x < obj2.getCenter().x
            and obj1.getCenter().y > obj2.getCenter().y + obj2.height / 2
        ):
            return True
        # Obj1 is on the bottom left of obj2
        elif (
            obj1.getCenter().x > obj2.getCenter().x
            and obj1.getCenter().y > obj2.getCenter().y
        ):
            return False

    def createTiles(self):
        def generatePosition(x, y):
            return Vector2(x, y)

        x = TILE_GRID_PROPERTIES["X_START"]
        y = TILE_GRID_PROPERTIES["Y_START"]
        for i in range(TILE_GRID_PROPERTIES["ROWS"]):
            for j in range(TILE_GRID_PROPERTIES["COLS"]):
                tile = Tile(self, generatePosition(x, y))
                self.tiles.append(tile)
                x += TILE_GRID_PROPERTIES["SPACING"] + tile.width
            y += TILE_GRID_PROPERTIES["SPACING"] + tile.height
            x = TILE_GRID_PROPERTIES["X_START"]
