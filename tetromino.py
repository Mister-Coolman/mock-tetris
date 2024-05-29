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

    def __init__(self, rotations: list[tuple[list[list[int]], int, int]], board: 'Board', x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.rotations = rotations
        self.currentRotation = 0
        self.board = board
    def moveLeft(self) -> bool:
        pass
    def moveRight(self) -> bool:
        pass
    def moveDown(self) -> bool:
        pass
    def rotateClockwise(self) -> bool:
        pass
    def rotateCounterclockwise(self) -> bool:
        pass
    
    def getBoundingMatrix(self) -> list[list[int]]:
        return self.rotations[self.currentRotation]

    def getPosition(self) -> tuple[int, int]:
        return x, y
