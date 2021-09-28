import pygame, json
from block import Block

class Level(Block):
    _current_level = []

    def __init__(self):
        print("level init")

    def load_level(self, level_name):
        with open("./levels/" + level_name) as level_json:
            self._current_level = json.load(level_json)

    def save_level(self, level_name):
        with open("./levels/" + level_name, "w") as level:
            json.dump(self._current_level, level)
