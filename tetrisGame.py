import pygame
from board import *
from tetromino import *
import configs
import random
import copy

"""
This will be the object created for an instance of the game
"""

class Tetris:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.colors = copy.copy(configs.colorTiles)

    def setColorScheme(self, colors: list[pygame.image]) -> None:
        this.colors = colors
