import pygame

class Block:
    coords = (0, 0)
    _size = 50
    _texture = None

    def __init__(self, c = (0, 0), size = 40, texture = "normal_block.png"):
        self.coords = c
        self._size = size
        self._texture = pygame.image.load("./sprites/blocks/" + texture)
        self._texture = pygame.transform.scale(self._texture, (self._size, self._size))

    def __del__(self):
        print("[CLASS] Block class destroyed")

    def get_size(self):
        return self._size

    def get_coords(self):
        return self.coords

    def set_coords(self, coords = (0, 0)):
        self.coords = coords

    def set_size(self, size = 10):
        self._size = size

    def get_renderer(self):
        return self._texture