from .Layer import Layer
from utils import loadSound


class SoundLayer(Layer):
    def __init__(self, collisionSound, elementDestroyedSound, newBallAddedSound):
        self.collisionSound = loadSound(collisionSound)
        self.collisionSound.set_volume(0.2)
        self.elementDestroyedSound = loadSound(elementDestroyedSound)
        self.elementDestroyedSound.set_volume(0.2)
        self.newBallAddedSound = loadSound(newBallAddedSound)
        self.newBallAddedSound.set_volume(0.2)

    def newBallAdded(self):
        self.newBallAddedSound.play()

    def elementDestroyed(self, element):
        self.elementDestroyedSound.play()

    def collisionDetected(self):
        self.collisionSound.play()

    def render(self, window):
        pass
