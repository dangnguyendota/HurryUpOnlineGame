from pynguyen.ninit import *

class Setting:
    def __init__(self):
        option(WIDTH=700, HEIGHT=500, FPS=60)
        self.gameRow = 9  # y
        self.gameColumn = 12  # x
        self.boardDeltaX = 10
        self.boardDeltaY = 50
        self.squareSize = 40

setting = Setting()
