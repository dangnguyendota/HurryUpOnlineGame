from Setting import *


def Square(color, size):
    """
    Tạo một ô vuông.
    :param color: Màu của ô
    :param size: Kích thước của ô (pixel)
    :return: Trả về Surface 1 ô vuông đã được tạo
    """
    square = Surface((size, size))
    square.fill(color)
    return square


class Board:
    def __init__(self, row, column):
        """
        Lớp Board là một mảng hai chiều đại diện cho bàn di chuyển
        :param row: số ô trong 1 hàng
        :param column: số ô trong một cột
        """
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


class ColorBoard:
    def __init__(self, row, column):
        """
        Lớp Board là một mảng hai chiều đại diện cho bàn di chuyển
        :param row: số ô trong 1 hàng
        :param column: số ô trong một cột
        """
        self._row = row
        self._column = column
        self._board = []
        for y in range(row):
            self._board.append([])
            for x in range(column):
                self._board[y].append((255, 255, 255))

    def draw(self, screen, pos, size):
        for x in range(self._column):
            for y in range(self._row):
                draw.rect(screen, self.get(x, y), (pos[0] + x * size, pos[1] + y * size, size, size))

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

class History:
    def __init__(self):
        self._pointer = -1
        self._history = []

    def add(self, data):
        self._history = self._history[:self._pointer+1]
        self._history.append(data)
        self._pointer += 1

    def back(self):
        if self._pointer > 0:
            self._pointer -= 1

    def undo(self):
        """
        Ctrl + 
        :return:
        """
        if self._pointer < len(self._history):
            self._pointer += 1


class Player(sprite.Sprite):
    def __init__(self, parent, id, start_pos):
        """
        Lớp Player này chính là nhân vật của ta điều khiển
        :param parent:Là lớp cha , hay chính là màn chơi.
        :param id:Id của nhân vật, mỗi nhân vật được nhận diện bằng id khác nhau.
        :param start_pos:vị trí khởi tạo của nhân vật.
        """
        sprite.Sprite.__init__(self)
        self.flag = {"stop": True, "moving": False, "fight": False, "die": False, "myTurn": True}
        self.setting = {"last_time": time.get_ticks(), "delta_time": 300, "vx": 0, "vy": 0, "v": 2, "deltaX": 5,
                        "deltaY": 5, "nextPosition": [0, 0]}
        self.parent = parent
        self.id = id
        # nguời chơi 2 đi sau
        if id == 2:
            self.flag["myTurn"] = False
        self.image = Surface((setting.squareSize - 10, setting.squareSize - 10))
        self.image.fill(Color('green'))
        self.rect = self.image.get_rect()
        self.rect.x = start_pos[0] + self.setting['deltaX']
        self.rect.y = start_pos[1] + self.setting['deltaY']
        self.setting["nextPosition"] = [self.rect.x, self.rect.y]

    def update(self):
        if not self.parent.states["pause"]:
            self.getKey()
        self.animation()

    def getKey(self):
        keystate = key.get_pressed()
        if (keystate[K_a] and self.id == 1) or (keystate[K_LEFT] and self.id == 2):
            self.move(direction='left')
        elif (keystate[K_d] and self.id == 1) or (keystate[K_RIGHT] and self.id == 2):
            self.move(direction='right')
        elif (keystate[K_w] and self.id == 1) or (keystate[K_UP] and self.id == 2):
            self.move(direction='up')
        elif (keystate[K_s] and self.id == 1) or (keystate[K_DOWN] and self.id == 2):
            self.move(direction='down')

    def animation(self):
        if self.flag['moving']:
            self.rect.x += self.setting['vx']
            self.rect.y += self.setting['vy']
            if self.setting['vx'] != 0:
                if -self.setting['v'] < self.setting['nextPosition'][0] - self.rect.x < self.setting['v']:
                    self.rect.x = self.setting['nextPosition'][0]
                    self.flag['moving'] = False
                    self.parent.change(self.id, self.standardize(self.setting['nextPosition']))
            if self.setting['vy'] != 0:
                if -self.setting['v'] < self.setting['nextPosition'][1] - self.rect.y < self.setting['v']:
                    self.rect.y = self.setting['nextPosition'][1]
                    self.flag['moving'] = False
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
            self.parent.swapTurn()

    def standardize(self, pos):
        return [(pos[0] - self.setting["deltaX"] - setting.boardDeltaX) // setting.squareSize,
                (pos[1] - self.setting["deltaY"] - setting.boardDeltaY) // setting.squareSize]

    def swapTurn(self):
        if self.flag["myTurn"]:
            self.flag["myTurn"] = False
        else:
            self.flag["myTurn"] = True


class DrawingBoard:
    def __init__(self, parent, pos, sizeX, sizeY, squareSize):
        self.parent = parent
        self.size = {"Columns": sizeX, "Rows": sizeY}
        self.pos = {"deltaX": pos[0], "deltaY": pos[1]}
        self.squareSize = squareSize
        self._color_board = ColorBoard(sizeY, sizeX)

    def update(self):
        self.animation()
        self.getKey()

    def getKey(self):
        mouseaction = mouse.get_pressed()
        if self.mouseInsideBoard():
            pos = realPositionToBoardPosition(mouse.get_pos(), self.pos["deltaX"], self.pos["deltaY"], self.squareSize)
            display.set_caption(str(pos))
            if mouseaction[0]:
                print(self.parent.getChosenColor())
                self._color_board.set(pos[0], pos[1], self.parent.getChosenColor())
            elif mouseaction[1]:
                self._color_board.set(pos[0], pos[1], Color('white'))

    def animation(self):
        pass

    def drawBoard(self):
        """
        draw the board
        """
        self._color_board.draw(self.parent.screen, [self.pos["deltaX"], self.pos["deltaY"]], self.squareSize)
        for i in range(self.size["Rows"] + 1):
            draw.line(self.parent.screen, Color('black'),
                        (self.pos["deltaX"], self.pos["deltaY"] + i * self.squareSize),
                        (self.pos["deltaX"] + self.size["Columns"] * self.squareSize,
                         self.pos["deltaY"] + i * self.squareSize))
        for i in range(self.size["Columns"] + 1):
            draw.line(self.parent.screen, Color('black'),
                        (self.pos["deltaX"] + i * self.squareSize, self.pos["deltaY"]),
                        (self.pos["deltaX"] + i * self.squareSize,
                         self.pos["deltaY"] + self.size["Rows"] * self.squareSize))
        draw.line(self.parent.screen, Color('black'), (SCREEN_WIDTH - 190, 50),
                  (SCREEN_WIDTH - 190, SCREEN_HEIGHT - 50))

    def setSize(self, sizeX, sizeY):
        self.size["Columns"] = sizeX
        self.size["Columns"] = sizeY
        self._color_board = ColorBoard(sizeX, sizeY)

    def mouseInsideBoard(self):
        return 0 <= mouse.get_pos()[0] - self.pos["deltaX"] <= self.size["Columns"] * self.squareSize and 0 <= \
                                                                                                          mouse.get_pos()[
                                                                                                              1] - \
                                                                                                          self.pos[
                                                                                                              "deltaY"] <= \
                                                                                                          self.size[
                                                                                                              "Rows"] * self.squareSize
