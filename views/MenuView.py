import pygame


class MenuView:
    def __init__(self, window):
        self.title = "Super PyBreakout"
        self.window = window
        self.gameFont = pygame.font.Font("assets/BD_Cartoon_Shout.ttf", 48)
        self.x = 1280 / 3

    def renderTitle(self):
        return self.gameFont.render("SUPER PY BREAKOUT!!", True, (0, 200, 0), (0, 0, 0))

    def renderClassicMode(self):
        return self.gameFont.render("Classic Mode", True, (0, 200, 0), (0, 0, 0))

    def renderCavityMode(self):
        return self.gameFont.render("Classic Mode", True, (0, 200, 0), (0, 0, 0))

    def renderProgressiveMode(self):
        return self.gameFont.render("Classic Mode", True, (0, 200, 0), (0, 0, 0))

    def renderScoreboard(self):
        return self.gameFont.render("Scoreboard", True, (0, 200, 0), (0, 0, 0))

    def render(self):
        self.window.blit(self.renderTitle(), (self.x, 100))
        self.window.blit(self.renderClassicMode(), (self.x, 150))
        self.window.blit(self.renderCavityMode(), (self.x, 200))
        self.window.blit(self.renderProgressiveMode(), (self.x, 250))
        self.window.blit(self.renderScoreboard(), (self.x, 300))
