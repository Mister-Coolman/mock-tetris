import pygame
from copy import deepcopy

colorTiles = [
  pygame.image.load("./bmps/Blue.bmp"),
  pygame.image.load("./bmps/Cyan.bmp"),
  pygame.image.load("./bmps/Green.bmp),
  pygame.image.load("./bmps/Magenta.bmp"),
  pygame.image.load("./bmps/Orange.bmp"),
  pygame.image.load("./bmps/Yellow.bmp)
]

levelColorTiles = deepcopy(colorTiles)
