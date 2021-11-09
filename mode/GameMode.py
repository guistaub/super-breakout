class GameMode:
    def __init__(self):
        self.__observers = []

    def addObserver(self, observer):
        self.__observers.append(observer)

    def notifyLoadClassicRequested(self):
        for observer in self.__observers:
            observer.loadClassicRequested()

    def notifyLoadCavityRequested(self):
        for observer in self.__observers:
            observer.loadCavityRequested()

    def notifyLoadProgressiveRequested(self):
        for observer in self.__observers:
            observer.loadProgressiveRequested()

    def notifyShowMenuRequested(self):
        for observer in self.__observers:
            observer.showMenuRequested()

    def notifyShowScoreboardRequested(self):
        for observer in self.__observers:
            observer.showScoreboardRequested()

    def notifyGetPlayerInfoRequested(self):
        for observer in self.__observers:
            observer.getPlayerInfo()

    def notifyGameWon(self):
        for observer in self.__observers:
            observer.gameWon()

    def notifyGameLost(self):
        for observer in self.__observers:
            observer.gameLost()

    def notifyQuitRequested(self):
        for observer in self.__observers:
            observer.quitRequested()

    def processInput(self):
        raise NotImplementedError()

    def update(self):
        raise NotImplementedError()

    def render(self, window):
        raise NotImplementedError()
