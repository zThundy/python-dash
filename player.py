import threading, pygame
from block import Block
from utils import Utils

class Player(Block, Utils):
    _screen = None
    _dimensions = (0, 0)
    _sdimensions = (0, 0)
    _velocity = (10, 0)
    _playerthread = True
    _thread = True
    _clock = pygame.time.Clock()

    def __init__(self, SCREEN, coords = (0, 0)):
        self._screen = SCREEN
        super().__init__(coords, 40, "../player.png")
        self._dimensions = (self._texture.get_width(), self._texture.get_height())
        self._sdimensions = (self._screen.get_width(), self._screen.get_height())

        self._thread = threading.Thread(target = self.calculate_movement)
        self._playerthread = threading.Thread(target = self.render_player)
        self._thread.start()
        self._playerthread.start()

    def __del__(self):
        print("[CLASS] Player class destroyed")
        self._thread = False
        self._playerthread = False

    def get_velocity(self):
        return self._velocity

    def set_velocity(self, v = (0, 0)):
        self._velocity = v

    def render_player(self):
        while self._playerthread:
            self._screen.blit(self._texture, (self.coords[0], self.coords[1]))

    def calculate_movement(self):
        while self._thread:
            # calculate vertical velocity while falling down
            if self._sdimensions[1] - 130 > self.coords[1]:
                if self._velocity[1] < 30:
                    self.set_velocity((self._velocity[0], self._velocity[1] + 1))
            else:
                self.set_velocity((self._velocity[0], 0))
            if self.mouseClickEvent():
                self.set_velocity((self._velocity[0], -13))
            self.set_coords((self.coords[0] + self._velocity[0], self.coords[1] + self._velocity[1]))
            self._clock.tick(60)