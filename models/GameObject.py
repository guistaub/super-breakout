from pygame import Vector2, Color


class GameObject:
    def __init__(self, state, window):
        self.center = None
        self.color = None
        self.state = state
        self.window = window

    def render(self):
        raise NotImplementedError

    def setColor(self, r, g, b, a):
        self.color = Color(r, g, b, a)
