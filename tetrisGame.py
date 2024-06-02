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
    match random.randint(0,5):
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
    return Tetromino(pieceRotations, board, 0, 0)


class Tetris:
    def __init__(self, x: int, y: int, rows: int, cols: int, gravity: int) -> None:
        self.x = x
        self.y = y
        self.colors = [pygame.transform.scale_by(i, 1.75) for i in configs.colorTiles]
        self.board = Board(rows, cols)
        self.rows = rows
        self.cols = cols
        self.piece = generateRandomPiece(self.board)
        self.next = generateRandomPiece(self.board)
        self.gravity = gravity
        self.gravityCounter = 0
        self.level = 0
        self.score = 0
        self.gameEnd = False

    def setColorScheme(self, colors: list[pygame.Surface]) -> None:
        self.colors = colors
    
    def update(self) -> None:
        self.gravityCounter += 1
        if self.gravityCounter >= self.gravity:
            if not self.piece.moveDown():
                self.board.place(self.piece)
                self.piece = self.next
                self.next = generateRandomPiece(self.board)
                if not self.board.validatePlacement(self.piece):
                    self.gameEnd = True
            self.gravityCounter = 0
        match (self.board.clearRows()):
            case 1:
                self.score += 100 * (1+self.level) #idk?
                
    
    def render(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, (127,127,127), pygame.Rect((self.x, self.y, (self.cols+1) * 28, (self.rows + 1) * 28)))
        pygame.draw.rect(surface, (0,0,0), pygame.Rect((self.x+14, self.y+14, (self.cols) * 28, (self.rows) * 28)))
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board.board[i][j]:
                    surface.blit(self.colors[self.board.board[i][j]-1], (self.x+14+28*j, self.y+14+28*i))
    
        row, col = self.piece.getPosition()
        matrix = self.piece.getBoundingMatrix()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]:
                    surface.blit(self.colors[matrix[i][j]-1], (self.x+14+28*(j+col), self.y+14+28*(i+row)))
        
    def processKeyPresses(self, keys: tuple[bool]) -> None:
        pass
