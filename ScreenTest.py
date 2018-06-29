from pygame import *
from pynguyen.nskeleton import *
import sys


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


class Player(sprite.Sprite):
    def __init__(self, parent, id, start_pos):
        sprite.Sprite.__init__(self)
        self.flag = {"stop": True, "moving": False, "fight": False, "die": False, "myTurn": True}
        self.setting = {"last_time": time.get_ticks(), "delta_time": 300, "vx": 0, "vy": 0, "v": 2, "deltaX": 5,
                        "deltaY": 5, "nextPosition": [0, 0]}
        self.parent = parent
        self.id = id
        self.image = Surface((setting.squareSize - 10, setting.squareSize - 10))
        self.image.fill(Color('green'))
        self.rect = self.image.get_rect()
        self.rect.x = start_pos[0] + self.setting['deltaX']
        self.rect.y = start_pos[1] + self.setting['deltaY']
        self.setting["nextPosition"] = [self.rect.x, self.rect.y]

    def update(self):
        self.getKey()
        self.animation()

    def getKey(self):
        keystate = key.get_pressed()
        if keystate[K_a] or keystate[K_LEFT]:
            self.move(direction='left')
        elif keystate[K_d] or keystate[K_RIGHT]:
            self.move(direction='right')
        elif keystate[K_w] or keystate[K_UP]:
            self.move(direction='up')
        elif keystate[K_s] or keystate[K_DOWN]:
            self.move(direction='down')

    def animation(self):
        if self.flag['moving']:
            self.rect.x += self.setting['vx']
            self.rect.y += self.setting['vy']
            if self.setting['vx'] != 0:
                if -self.setting['v'] < self.setting['nextPosition'][0] - self.rect.x < self.setting['v']:
                    self.rect.x = self.setting['nextPosition'][0]
                    self.flag['moving'] = False
                    # self.flag['myTurn'] = False
                    self.parent.change(self.id, self.standardize(self.setting['nextPosition']))
            if self.setting['vy'] != 0:
                if -self.setting['v'] < self.setting['nextPosition'][1] - self.rect.y < self.setting['v']:
                    self.rect.y = self.setting['nextPosition'][1]
                    self.flag['moving'] = False
                    # self.flag['myTurn'] = False
                    self.parent.change(self.id, self.standardize(self.setting['nextPosition']))

    def move(self, **kwargs):
        if kwargs['direction']:
            if self.flag['moving'] or not self.flag['myTurn'] or not self.parent.checkMove(self.id,
                                                                                           kwargs['direction']):
                return
            if kwargs['direction'] == 'left':
                self.setting['vx'] = -self.setting['v']
                self.setting['vy'] = 0
                self.setting['nextPosition'][0] = self.rect.x - setting.squareSize
            elif kwargs['direction'] == 'right':
                self.setting['vx'] = self.setting['v']
                self.setting['vy'] = 0
                self.setting['nextPosition'][0] = self.rect.x + setting.squareSize
            elif kwargs['direction'] == 'up':
                self.setting['vy'] = -self.setting['v']
                self.setting['vx'] = 0
                self.setting["nextPosition"][1] = self.rect.y - setting.squareSize
            elif kwargs['direction'] == 'down':
                self.setting['vy'] = self.setting['v']
                self.setting['vx'] = 0
                self.setting["nextPosition"][1] = self.rect.y + setting.squareSize
            self.flag['moving'] = True

    def standardize(self, pos):
        return [(pos[0] - self.setting["deltaX"] - setting.boardDeltaX) // setting.squareSize,
                (pos[1] - self.setting["deltaY"] - setting.boardDeltaY) // setting.squareSize]


class Screen(classical_skeleton):
    def __init__(self, setting=None):
        classical_skeleton.__init__(self)
        self.setting = setting
        self.constValue = {"nothing": 0, "player1": 1, "player2": 2, "player1_went_through": 3,
                           "player2_went_through": 4, "banned" :[1, 2, 3, 4], "player1_start_pos": (0, 0),
                           "player2_start_pos": (self.setting.gameColumn - 1, self.setting.gameRow - 1)}
        display.set_caption("** Online **")

    def new(self):
        """refresh game sprites, upload, delete, change,... game status, creates new sprites, somethings like that..."""
        self.realboard = Board(self.setting.gameRow, self.setting.gameColumn)
        self.players = sprite.Group()
        self.addPlayer(1, self.constValue['player1_start_pos'])
        # self.addPlayer(2, self.constValue['player2_start_pos'])

    def event(self, e):
        """handle the events like mouse moving, key pressing,.."""
        pass

    def update(self):
        """update sprites status"""
        self.players.update()

    def draw(self):
        """draw sprites, effects, enviroment,... on the screen"""
        self.screen.fill(Color("white"))
        self.drawBoard()
        self.drawTheSquares()
        self.players.draw(self.screen)

    def drawBoard(self):
        """draw the board"""
        for i in range(self.setting.gameRow + 1):
            draw.aaline(self.screen, Color('black'),
                        (self.setting.boardDeltaX, self.setting.boardDeltaY + i * self.setting.squareSize),
                        (self.setting.boardDeltaX + self.setting.gameColumn * self.setting.squareSize,
                         self.setting.boardDeltaY + i * self.setting.squareSize))
        for i in range(self.setting.gameColumn + 1):
            draw.aaline(self.screen, Color('black'),
                        (self.setting.boardDeltaX + i * self.setting.squareSize, self.setting.boardDeltaY),
                        (self.setting.boardDeltaX + i * self.setting.squareSize,
                         self.setting.boardDeltaY + self.setting.gameRow * self.setting.squareSize))

    def drawTheSquares(self):
        for x in range(self.setting.gameColumn):
            for y in range(self.setting.gameRow):
                pos = self.boardPositionToRealPosition([x, y])
                if self.realboard.get(x, y) == self.constValue["player1_went_through"]:
                    self.screen.blit(Square(Color('red'), 30), [pos[0] + 5, pos[1] + 5])
                elif self.realboard.get(x, y) == self.constValue["player2_went_through"]:
                    self.screen.blit(Square(Color('yellow'), 30), [pos[0] + 5, pos[1] + 5])

    def addPlayer(self, num, pos):
        """Add a new player with position: pos and id: num"""
        poss = [self.setting.boardDeltaX + pos[0] * self.setting.squareSize,
                self.setting.boardDeltaY + pos[1] * self.setting.squareSize]
        self.players.add(Player(self, num, poss))
        self.realboard.set(pos[0], pos[1], num)

    def checkMove(self, id, direction):
        """Check the move is invalid or not"""
        for x in range(self.setting.gameColumn):
            if self.realboard.get(x, 0) == id:
                if direction == "up":
                    return False
            elif self.realboard.get(x, self.setting.gameRow - 1) == id:
                if direction == "down":
                    return False
        for y in range(self.setting.gameRow):
            if self.realboard.get(0, y) == id:
                if direction == "left":
                    return False
            elif self.realboard.get(self.setting.gameColumn - 1, y) == id:
                if direction == "right":
                    return False
        current_pos = self.realboard.getPos(id)
        if direction == "up":
            if self.realboard.get(current_pos[0], current_pos[1]-1) in self.constValue["banned"]:
                return False
        elif direction == "down":
            if self.realboard.get(current_pos[0], current_pos[1]+1) in self.constValue["banned"]:
                return False
        elif direction == "left":
            if self.realboard.get(current_pos[0]-1, current_pos[1]) in self.constValue["banned"]:
                return False
        elif direction == "right":
            if self.realboard.get(current_pos[0]+1, current_pos[1]) in self.constValue["banned"]:
                return False
        return True

    def change(self, id, pos):
        """mark the player with id: id through the last position and now is in the new position: pos"""
        poss = self.realboard.getPos(id)
        if id == self.constValue["player1"]:
            self.realboard.set(poss[0], poss[1], self.constValue["player1_went_through"])
            self.realboard.set(pos[0], pos[1], self.constValue["player1"])
        elif id == self.constValue["player2"]:
            self.realboard.set(poss[0], poss[1], self.constValue["player2_went_through"])
            self.realboard.set(pos[0], pos[1], self.constValue["player2"])
        else:
            return

    def boardPositionToRealPosition(self, boardPos):
        x = boardPos[0] * self.setting.squareSize + self.setting.boardDeltaX
        y = boardPos[1] * self.setting.squareSize + self.setting.boardDeltaY
        return [x, y]


# TEST
setting = Setting()
s = Screen(setting)
s.new()
s.run()
