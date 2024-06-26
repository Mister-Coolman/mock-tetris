import pygame
from board import *
from tetromino import *
import configs
import random

pygame.font.init()

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
        case 6:
            pieceRotations = Tetromino.O_pieceRotations
    # change 0, 0 to the center of board according to
    # piece rotations cols and board cols
    # I'm too lazy xd
    return Tetromino(pieceRotations, board, 0, int(len(board.board[0])/2-len(pieceRotations[0][0][0])/2), 0)


class Tetris:
    font = pygame.font.SysFont("Times New Roman", 30)
    def __init__(self, x: int, y: int, rows: int, cols: int) -> None:
        self.x = x
        self.y = y
        self.colors = [pygame.transform.scale_by(i, 1.75) for i in configs.colorTiles]
        self.outlinedColors = [pygame.transform.scale_by(i, 1.75) for i in configs.outlinedTiles]
        self.board = Board(rows, cols)
        self.rows = rows
        self.cols = cols
        self.piece = generateRandomPiece(self.board)
        self.next = generateRandomPiece(self.board)
        self.level = 0
        self.score = 0
        self.rowsCleared = 0
        self.gameEnd = False
        self.endAnimation = self.rows * 10 - 1

    def setColorScheme(self, colors: list[pygame.Surface]) -> None:
        self.colors = colors
    
    def update(self) -> int:
        if not self.piece.moveDown():
            self.board.place(self.piece)
            self.piece = self.next
            self.next = generateRandomPiece(self.board)
            if not self.board.validatePlacement(self.piece):
                self.gameEnd = True
        rowsClear = self.board.clearRows()
        match (rowsClear):
            case 1:
                self.score += 40*(self.level+1)
            case 2:
                self.score += 100*(self.level+1)
            case 3:
                self.score += 300*(self.level+1)
            case 4:
                self.score += 1200*(self.level+1)
        self.rowsCleared += rowsClear
        if (self.rowsCleared // 10) > self.level:
            self.level = self.rowsCleared // 10
            return 1
        return 0
                
    
    def render(self, surface: pygame.Surface) -> None:
        #draws the board
        pygame.draw.rect(surface, (127,127,127), pygame.Rect((self.x, self.y, (self.cols+1) * 28, (self.rows + 1) * 28)))
        pygame.draw.rect(surface, (0,0,0), pygame.Rect((self.x+14, self.y+14, (self.cols) * 28, (self.rows) * 28)))
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board.board[i][j]:
                    surface.blit(self.colors[self.board.board[i][j]-1], (self.x+14+28*j, self.y+14+28*i))
        row, col = self.piece.getPosition()
        matrix = self.piece.getBoundingMatrix()

        #outlines where piece will fall
        fallPiece = Tetromino(self.piece.rotations, self.board, row, col, self.piece.currentRotation)
        fallRow = row
        while fallPiece.moveDown():
            fallRow += 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]:
                    surface.blit(self.outlinedColors[matrix[i][j]-1], (self.x+14+28*(j+col), self.y+14+28*(i+fallRow)))
        
        #draws the current piece

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]:
                    surface.blit(self.colors[matrix[i][j]-1], (self.x+14+28*(j+col), self.y+14+28*(i+row)))
        if self.gameEnd:
            for i in range(self.rows):
                for j in range(self.cols):
                    if self.board.board[i][j]:
                        surface.blit(self.colors[self.board.board[i][j]-1], (self.x+14+28*j, self.y+14+28*i))
     
        #next piece
        
        pygame.draw.rect(surface, (127,127,127), pygame.Rect((self.x+(self.cols+1)*28, self.y+self.rows*28/3, 28*6, 28*4)))
        pygame.draw.rect(surface, (0,0,0), pygame.Rect((self.x+(self.cols+1)*28+14, self.y+self.rows*28/3+14, 28*5, 28*3)))
        matrix = self.next.getBoundingMatrix()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]:
                    surface.blit(self.colors[matrix[i][j]-1], (self.x+(self.cols+2+j)*28, self.y+self.rows*28/3 + (i+1)*28))
                    
        #score display
        
        pygame.draw.rect(surface, (127,127,127), pygame.Rect((self.x+(self.cols+1)*28, self.y, 200, 78)))
        pygame.draw.rect(surface, (0,0,0), pygame.Rect((self.x+(self.cols+1)*28+14, self.y+14, 200-28, 78-28)))
        text = Tetris.font.render(str(self.score), False, (255,255,255))
        surface.blit(text, (self.x+(self.cols+1)*28+14+5, self.y+14+5))

        ##level display

        pygame.draw.rect(surface, (127, 127, 127), pygame.Rect((self.x + (self.cols + 1) * 28, self.y + self.rows * 56/3, 200, 78)))
        pygame.draw.rect(surface, (0, 0, 0), pygame.Rect((self.x + (self.cols + 1) * 28 + 14, self.y + self.rows * 56/3 + 14, 200 - 28, 50)))
        text = Tetris.font.render("Level: " + str(self.level + 1), False, (255, 255, 255))
        surface.blit(text, (self.x + (self.cols + 1) * 28 + 14 + 5, self.y + self.rows * 56/3 + 14 + 5))
