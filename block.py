import pygame

class Block:
    _coords = (0, 0)
    _size = 10
    _texture = None

    def __init__(self, c = (0, 0), size = 10, texture = "normal_block.png"):
        self._coords = c
        self._size = size
        self._texture = pygame.image.load("./sprites/blocks/" + texture)
        self._texture = pygame.image.size(self._size, self._size)

    def get_size(self):
        return self._size

    def get_coords(self):
        return self._coords

    def set_coords(self, coords = (0, 0)):
        self._coords = coords

    def set_size(self, size = 10):
        self._size = 10

    def get_renderer(self):
        return self._texture