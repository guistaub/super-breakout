from tests.test import validate
from views.app import App

test_app = App()
validate(test_app.get_game_status() == True, "Game Status Getter")
test_app.set_game_status(False)
validate(test_app.get_game_status() == False, "Game Status Setter")
