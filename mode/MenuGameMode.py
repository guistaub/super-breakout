from properties import COLORS
from .GameMode import GameMode
import pygame
from pygame import Vector2


class MenuGameMode(GameMode):
    def __init__(self):
        super().__init__()
        # Font
        self.titleFont = pygame.font.Font("assets/BD_Cartoon_Shout.ttf", 72)
        self.itemFont = pygame.font.Font("assets/BD_Cartoon_Shout.ttf", 48)

        # Menu items
        self.menuItems = [
            {"title": "Classic Mode", "action": self.notifyLoadClassicRequested},
            {"title": "Cavity Mode", "action": self.notifyLoadCavityRequested},
            {
                "title": "Progressive Mode",
                "action": self.notifyLoadProgressiveRequested,
            },
            {"title": "Scoreboard", "action": self.notifyShowScoreboardRequested},
            {"title": "Quit", "action": self.notifyQuitRequested},
        ]

        self.currentMenuItem = 0
        self.cursorRadius = 30

    def processInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.notifyQuitRequested()
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.notifyQuitRequested()
                    break
                elif event.key == pygame.K_DOWN:
                    if self.currentMenuItem < len(self.menuItems) - 1:
                        self.currentMenuItem += 1
                    else:
                        self.currentMenuItem = 0
                elif event.key == pygame.K_UP:
                    if self.currentMenuItem > 0:
                        self.currentMenuItem -= 1
                    else:
                        self.currentMenuItem = 4
                elif event.key == pygame.K_RETURN:
                    menuItem = self.menuItems[self.currentMenuItem]
                    menuItem["action"]()

    def update(self):
        pass

    def showCursor(self, window, x, y):
        pygame.draw.circle(window, COLORS["GREEN"], Vector2(x, y), self.cursorRadius)

    def render(self, window):
        # Initial y position
        y = 150

        titleSurface = self.titleFont.render("SUPER BREAKOUT!", True, COLORS["RED"])
        titleX = (window.get_width() - titleSurface.get_width()) // 2
        window.blit(titleSurface, (titleX, y))
        y += (3 * titleSurface.get_height()) // 2

        for index, item in enumerate(self.menuItems):
            itemSurface = self.itemFont.render(item["title"], True, COLORS["RED"])
            y += (3 * itemSurface.get_height()) // 2
            itemX = (window.get_width() - itemSurface.get_width()) // 2
            window.blit(itemSurface, (itemX, y))

            if index == self.currentMenuItem:
                cursorX = itemX - 2 * self.cursorRadius
                cursorY = y + itemSurface.get_height() // 2
                self.showCursor(window, cursorX, cursorY)
