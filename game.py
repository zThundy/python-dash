import pygame, threading, sys
from pygame.locals import *

from font import Font

class Game:
    _screen = None
    _clock = pygame.time.Clock()
    _font = None

    def __init__(self, SCREEN):
        self._screen = SCREEN
        self._font = Font(SCREEN)
        threading.Thread(target = self.main_thread).start()
        self.event_handler()

    def main_thread(self):
        while True:
            # fill screen with black background color to clear everithing
            self._screen.fill((0, 0, 0))
            # render all fonts on screen
            self._font.draw_everything()
            # update display
            pygame.display.update()
            # limit the number of fps to 60
            self._clock.tick(60)

    def event_handler(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
