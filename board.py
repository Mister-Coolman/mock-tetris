import pygame
from tetromino import *
import os

class Board:
    def __init__(self, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols
        self.board = [[0]*cols for i in range(rows)]
    
    def setPosition(self, row: int, col: int, color: int) -> None:
        assert(row >= 0 and row < self.rows)
        assert(col >= 0 and col < self.cols)
        self.board[row][col] = color
    
    def clearRows(self) -> int:
        count = 0
        for row in reversed(self.board):
            if all(row):
                self.board.remove(row)
                self.board = [[0] * self.cols] + self.board
                count += 1
        return count
    
    def validatePlacement(self, piece: 'Tetromino') -> bool:
        row, col = piece.getPosition()
        if row < 0 or col < 0:
            return False
        matrix = piece.getBoundingMatrix()
        try:
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] and self.board[row+i][col+j]:
                        return False
        except:
            return False
        return True

    def place(self, piece: 'Tetromino') -> None:
        row, col = piece.getPosition()
        matrix = piece.getBoundingMatrix()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]:
                    self.board[row+i][col+j] = matrix[i][j]
