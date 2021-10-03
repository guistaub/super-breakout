from interface import UserInterface
import os
from pygame import quit

if __name__ == "__main__":
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    game = UserInterface()
    game.run()
    quit()
