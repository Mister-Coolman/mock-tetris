import pygame
from tetromino import *

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
    for row in self.board:
      if all(row):
        del row
        self.board += [0] * self.cols
        count += 1
    return count
    
  def place(self, piece: 'Tetramino'):
    pass
    
