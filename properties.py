# COLORS

COLORS = {
    "BLUE": (0, 0, 200),
    "RED": (200, 0, 0),
    "GREEN": (0, 200, 0),
    "BLACK": (0, 0, 0),
    "WHITE": (255, 255, 255),
}

# GAME ELEMENT PROPERTIES

PADDLE_PROPERTIES = {"width": 130, "height": 20, "type": "paddle"}

TILE_PROPERTIES = {"width": 130, "height": 20, "type": "tile"}

BALL_PROPERTIES = {"width": 20, "height": 20, "type": "ball"}

WINDOW_PROPERTIES = {"width": 1600, "height": 900}

TILE_GRID_PROPERTIES = {
    "ROWS": 6,
    "COLS": 11,
    "SPACING": 10,
    "X_START": 32,
    "Y_START": 32,
}

# GAME MODES

OVERLAY = "OVERLAY"

CLASSIC = "CLASSIC"

CAVITY = "CAVITY"

PROGRESSIVE = "PROGRESSIVE"

SCOREBOARD = "SCOREBOARD"

# UNIT STATUS

UNIT_STATUS_ALIVE = "ALIVE"

UNIT_STATUS_DESTROYED = "DESTROYED"

# FILE PATHS

CARTOON_FONT = "BD_Cartoon_Shout.ttf"

MENU_MUSIC = "menu_sound.mp3"

MENU_NAVIGATION_SOUND = "270315__littlerobotsoundfactory__menu-navigate-03.wav"

ELEMENT_COLLISION_SOUND = "270327__littlerobotsoundfactory__hit-00.wav"

ELEMENT_DESTROYED_SOUND = "270343__littlerobotsoundfactory__shoot-01.wav"

GAME_WON_JINGLE = "270319__littlerobotsoundfactory__jingle-win-01.wav"

GAME_LOST_JINGLE = "270329__littlerobotsoundfactory__jingle-lose-00.wav"

BALL_ADDED_SOUND = "270330__littlerobotsoundfactory__jingle-achievement-01.wav"

KEYBOARD_CLICKING_SOUND = (
    "Mechanical-Keyboard-single-button-presses-1-www.FesliyanStudios.com.mp3"
)

# MESSAGES

GAME_START_MESSAGE = "SUPER PY BREAKOUT - PRESS ENTER TO CONTINUE"

GAME_WON_MESSAGE = "VICTORY! - PRESS ENTER TO CONTINUE"

GAME_LOST_MESSAGE = "GAME LOST... - PRESS ENTER TO CONTINUE"

# DATABASE CONNECTION

CONNECTION = "database/database.db"
