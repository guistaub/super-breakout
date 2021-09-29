from views import GameView
import os

if __name__ == "__main__":
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    game = GameView()
    game.run()
