from board import *

class Tetromino:
    """pieces are encoded as
    list[tuple(matrix, row offset, col offset)]
    
    or
    list[tuple[list[list[int]], int, int]]
    
    where the matrix is the bounding box of the tetromino

    offset is the offset from the top left corner of the
    square version of the bounding box of the tetromino
    
    rotations will transform coordinate
        -> top left corner of square matrix
    and then transform that point
        -> top left corner of bounding box matrix using offset
    """
    I_pieceRotations = [
        ([[1,1,1,1]], 0, 2),
        ([[1],[1],[1],[1]], 2, 0)
    ]
    J_pieceRotations = [
        ([[2,2,2],[0,0,2]], 0, 1),
        ([[0,2],[0,2],[2,2]], 0, 0),
        ([[2,0,0],[2,2,2]], 0, 0),
        ([[2,2],[2,0],[2,0]], 1, 0)
    ]
    L_pieceRotations = [
        ([[3,3,3],[3,0,0]], 0, 1),
        ([[3,3],[0,3],[0,3]], 0, 0),
        ([[0,0,3],[3,3,3]], 0, 0),
        ([[3,0],[3,0],[3,3]], 1, 0)
    ]
    Z_pieceRotations = [
        ([[0,4,4],[4,4,0]], 0, 1),
        ([[4,0],[4,4],[0,4]], 1, 0)
    ]
    S_pieceRotations = [
        ([[5,5,0],[0,5,5]], 0, 1),
        ([[0,5],[5,5],[5,0]], 1, 0)
    ]
    T_pieceRotations = [
        ([[6,6,6],[0,6,0]], 0, 1),
        ([[0,6],[6,6],[0,6]], 0, 0),
        ([[0,6,0],[6,6,6]], 0, 0),
        ([[6,0],[6,6],[6,0]], 1, 0)
    ]
    O_pieceRotations = [
        ([[7,7],[7,7]], 0, 0)
    ]

    def __init__(self, rotations: list[tuple[list[list[int]], int, int]], board: 'Board', row: int, col: int, currentRotation: int) -> None:
        self.row = row
        self.col = col
        self.rotations = rotations
        self.currentRotation = currentRotation
        self.board = board
    
    def moveLeft(self) -> bool:
        if self.col == 0:
            return False
        self.col -= 1
        if not self.board.validatePlacement(self):
            self.col += 1
            return False
        return True
    
    def moveRight(self) -> bool:
        if self.col + len(self.getBoundingMatrix()[0]) >= len(self.board.board[0]):
            return False
        self.col += 1
        if not self.board.validatePlacement(self):
            self.col -= 1
            return False
        return True
    
    def moveDown(self) -> bool:
        if self.row + len(self.getBoundingMatrix()) >= len(self.board.board):
            return False
        self.row += 1
        if not self.board.validatePlacement(self):
            self.row -= 1
            return False
        return True
    
    def rotateClockwise(self) -> bool:
        self.col -= self.rotations[self.currentRotation][1]
        self.row -= self.rotations[self.currentRotation][2]
        self.currentRotation += 1
        if self.currentRotation >= len(self.rotations):
            self.currentRotation = 0
        self.col += self.rotations[self.currentRotation][1]
        self.row += self.rotations[self.currentRotation][2]
        if not self.board.validatePlacement(self):
            self.col -= self.rotations[self.currentRotation][1]
            self.row -= self.rotations[self.currentRotation][2]
            self.currentRotation -= 1
            if self.currentRotation < 0:
                self.currentRotation = len(self.rotations) - 1
            self.col += self.rotations[self.currentRotation][1]
            self.row += self.rotations[self.currentRotation][2]
            return False
        return True
    
    def rotateCounterclockwise(self) -> bool:
        self.col -= self.rotations[self.currentRotation][1]
        self.row -= self.rotations[self.currentRotation][2]
        self.currentRotation -= 1
        if self.currentRotation < 0:
            self.currentRotation = len(self.rotations) - 1
        self.col += self.rotations[self.currentRotation][1]
        self.row += self.rotations[self.currentRotation][2]
        if not self.board.validatePlacement(self):
            self.col -= self.rotations[self.currentRotation][1]
            self.row -= self.rotations[self.currentRotation][2]
            self.currentRotation += 1
            if self.currentRotation >= len(self.rotations):
                self.currentRotation = 0
            self.col += self.rotations[self.currentRotation][1]
            self.row += self.rotations[self.currentRotation][2]
            return False
        return True
    
    def getBoundingMatrix(self) -> list[list[int]]:
        return self.rotations[self.currentRotation][0]

    def getPosition(self) -> tuple[int, int]:
        return self.row, self.col

    def __repr__(self) -> str:
        return str(self.row) + " " + str(self.col) + "\n" + str(self.getBoundingMatrix())
