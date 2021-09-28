import pygame

GAME_NAME = "Python Dash"
SCREEN = None

from game import Game

def main():
    # define global variables access
    global SCREEN
    # create screen using the display functiuon
    _screen = pygame.display.set_mode((1440, 900), 0, 0, 0, 1)
    pygame.display.set_caption(GAME_NAME)
    _screen.fill((0, 0, 0))
    SCREEN = _screen
    Game(SCREEN)

if __name__ == "__main__":
    main()