class GameStateController:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
        self.stepX = 10
        self.stepY = 10
        self.ball = None
        self.tileGroup = None

    def updateBallPosition(self):
        if self.x > self.width - 25 or self.x < 0:
            self.stepX = -self.stepX
        if self.y > self.height - 25 or self.y < 0:
            self.stepY = -self.stepY
        self.x += self.stepX
        self.y += self.stepY

    def setBall(self, ball):
        self.ball = ball
