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
    def __init__(self, board: 'Board') -> None:
        pass
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
