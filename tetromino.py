from board import *

"""
pieces will inherit tetramino
position will be the top left corner
rotate will change both matrix and position

notes:
it may be better to implement the move left/right/down in the Tetramino class
it is highly uncertain how this works and is highly subjected to possible changes
these classes outlined should never draw anything on the board
"""

class Tetramino:
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

    def __init__(self, rotations: list[tuple[list[list[int]], int, int]] board: 'Board', x: int, y: int) -> None:
        self.x = x
        self.y = y
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
    def drop(self) -> bool:
        pass
    def getMatrix(self) -> list[list[int]]:
        pass
    def getPosition(self) -> tuple[int, int]:
        pass
