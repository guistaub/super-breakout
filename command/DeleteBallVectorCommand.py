from .Command import Command


class DeleteBallVectorCommand(Command):
    def __init__(self, gameState, index):
        self.gameState = gameState
        self.index = index

    def run(self):
        try:
            self.gameState.ballVectors.pop(self.index)
        except:
            pass
