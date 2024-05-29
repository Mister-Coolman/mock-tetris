import pygame
from board import *
from tetromino import *
import configs
import random
import copy

"""
This will be the object created for an instance of the game
"""

def generateRandomPiece(board: Board) -> Tetromino:
    pieceRotations = None
    match random.randint(0,6):
        case 0:
            pieceRotations = Tetromino.I_pieceRotations
        case 1:
            pieceRotations = Tetromino.J_pieceRotations
        case 2:
            pieceRotations = Tetromino.L_pieceRotations
        case 3:
            pieceRotations = Tetromino.Z_pieceRotations
        case 4:
            pieceRotations = Tetromino.S_pieceRotations
        case 5:
            pieceRotations = Tetromino.T_pieceRotations
    # change 0, 0 to the center of board according to
    # piece rotations cols and board cols
    # I'm too lazy xd
    return Tetromino(pieceRotations, 0, 0)


class Tetris:
    def __init__(self, x: int, y: int, rows: int, cols: int) -> None:
        self.x = x
        self.y = y
        self.colors = copy.copy(configs.colorTiles)
        self.board = Board(rows, cols)
        self.piece = generateRandomPiece(self.board)

    def setColorScheme(self, colors: list[pygame.image]) -> None:
        this.colors = colors
    
    def update(self) -> None:
        pass
    
    def render(self) -> None:
        pass
    
    def processKeyPresses(self, keys: tuple[bool]) -> None:
        pass
