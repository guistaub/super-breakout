from .GameItem import GameItem
from .properties import TILE_PROPERTIES


class Tile(GameItem):
    def __init__(self, state, position):
        super().__init__(state, position)
        self.height = TILE_PROPERTIES["height"]
        self.width = TILE_PROPERTIES["width"]
        self.type = TILE_PROPERTIES["type"]

    def move(self, moveVector):
        pass
