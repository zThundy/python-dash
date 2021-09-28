import pygame
from block import Block

class Player(Block):
    def __init__(self, coords = (0, 0)):
        super().__init__(coords, 10, "../player.png")