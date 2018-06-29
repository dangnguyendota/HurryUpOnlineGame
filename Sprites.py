from pynguyen.ninit import *

def Square(color, size):
    square = Surface((size, size))
    square.fill(color)
    return square

class Setting:
    def __init__(self):
        option(WIDTH=700, HEIGHT=500, FPS=60)
        self.gameRow = 9  # y
        self.gameColumn = 12  # x
        self.boardDeltaX = 10
        self.boardDeltaY = 50
        self.squareSize = 40

class Board:
    def __init__(self, row, column):
        self._row = row
        self._column = column
        self._board = []
        for y in range(row):
            self._board.append([])
            for x in range(column):
                self._board[y].append(0)

    def get(self, x, y):
        try:
            return self._board[y][x]
        except:
            raise IndexError

    def set(self, x, y, value):
        try:
            self._board[y][x] = value
        except:
            raise IndexError

    def getPos(self, id):
        for y in range(self._row):
            for x in range(self._column):
                if self._board[y][x] == id:
                    return [x, y]
        return [-1, -1]

    def printToConsole(self):
        for row in self._board:
            print(row)