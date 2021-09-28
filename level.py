import pygame, json
from block import Block
from pygame.locals import *

# {
#   blocks = [
#       {
#           texture = "normal",
#           size = 40,
#           coords = (0, 0)
#       },
#       {
#           texture = "normal",
#           size = 40,
#           coords = (10, 0)
#       }
#   ],
#   level_name = "test_level",
#   colors = {
#       background = (0, 255, 0)
#   }
# }

class Level(Block):
    _currentlevel = []
    _screen = None
    _bgsprite = None
    _originalsprite = None
    _bgcolorsprite = None
    _bgname = "default_background.png"
    _sdimensions = (0, 0)

    def __init__(self, SCREEN):
        self._screen = SCREEN
        self._sdimensions = (self._screen.get_width(), self._screen.get_height())
        self._originalsprite = pygame.image.load("./sprites/" + self._bgname)
        self._originalsprite = pygame.transform.scale(self._originalsprite, (self._sdimensions[0], self._sdimensions[1]))
        self._bgsprite = self._originalsprite.copy()
        self._bgsprite.fill((255, 50, 50, 255), None, BLEND_RGBA_MULT)

    def __del__(self):
        print("[CLASS] Level class destroyed")

    def load_level(self, level_name):
        with open("./data/levels/" + level_name) as level_json:
            self._currentlevel = json.load(level_json)

    def save_level(self, level_name):
        with open("./data/levels/" + level_name, "w") as level:
            json.dump(self._currentlevel, level)

    def draw_background(self):
        self._screen.blit(self._bgsprite, (0, 0))
        pygame.draw.rect(self._screen, (230, 230, 230), (0, self._sdimensions[1] - 90, self._sdimensions[0], 1))

    def draw_current_level(self):
        self.draw_background()
