from .Layer import Layer
from utils import loadSound


class SoundLayer(Layer):
    def __init__(self, collisionSound, elementDestroyedSound):
        self.collisionSound = loadSound(collisionSound)
        self.collisionSound.set_volume(0.2)
        self.elementDestroyedSound = loadSound(elementDestroyedSound)
        self.elementDestroyedSound.set_volume(0.2)

    def elementDestroyed(self, element):
        self.elementDestroyedSound.play()

    def collisionDetected(self):
        self.collisionSound.play()

    def render(self, window):
        pass
