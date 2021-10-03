class GameItem:
    def __init__(self, state, position):
        self.state = state
        self.status = "alive"
        self.position = position
        self.type = None

    def move(self, moveVector):
        raise NotImplementedError

    def getType(self):
        return self.type
