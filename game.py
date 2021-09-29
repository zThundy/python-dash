import pygame, threading, sys
from pygame.locals import *

from font import Font
from player import Player
from level import Level

class Game:
    _screen = None
    _clock = pygame.time.Clock()
    _font = None
    _player = None
    _level = None
    _thread = True

    def __init__(self, SCREEN):
        self._screen = SCREEN
        self._font = Font(SCREEN)
        self._player = Player(SCREEN, (50, SCREEN.get_height() - 130))
        self._level = Level(SCREEN)
        threading.Thread(target = self.main_thread).start()
        self.event_handler()

    def main_thread(self):
        while self._thread:
            # fill screen with black background color to clear everithing
            self._screen.fill((0, 0, 0))
            # render the whole level
            self._level.draw_current_level()
            # render all fonts on screen
            self._font.draw_everything()
            # update display
            pygame.display.update()
            # limit the number of fps to 60
            self._clock.tick(256)

    def event_handler(self):
        while self._thread:
            for event in pygame.event.get():
                if event.type == QUIT:
                    # this is done to terminate all
                    # threads in the game
                    self._level.__del__()
                    self._font.__del__()
                    self._player.__del__()
                    self._thread = False
                    # terminate the program
                    pygame.quit()
                    sys.exit()
