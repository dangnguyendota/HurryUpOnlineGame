from Sprites import *
from UI import *


class Screen_AI_solo(classical_skeleton):
    def __init__(self, setting=None):
        classical_skeleton.__init__(self)
        self.setting = setting
        display.set_caption("** Online **")

    def new(self):
        """
        Tạo mới màn chơi
        :return:
        """
        self.constValue = {"nothing": 0, "player1": 1, "player2": 2, "player1_went_through": 3,
                           "player2_went_through": 4, "banned": [1, 2, 3, 4], "player1_start_pos": (0, 0),
                           "player2_start_pos": (self.setting.gameColumn - 1, self.setting.gameRow - 1)}
        self._game_mode = {"AI-solo": True, "Multiplayer": False, "Pixel-art": False}
        self.states = {"pause":False, "main":True}
        self.realboard = Board(self.setting.gameRow, self.setting.gameColumn)
        self.players = sprite.Group()
        self.addPlayer(1, self.constValue['player1_start_pos'])
        self.addPlayer(2, self.constValue['player2_start_pos'])
        self.buttons = sprite.Group()
        self.buttons.add(NewGame(self, [SCREEN_WIDTH - 170, 30]))
        self.buttons.add(PauseGame(self, [SCREEN_WIDTH - 170, 100]))
        self.buttons.add(Exit(self, [SCREEN_WIDTH - 120, SCREEN_HEIGHT - 70]))
        self.sizeX = ScrollBar(self, (SCREEN_WIDTH - 180, 200), self.setting.gameColumn, 25, "Number of columns")
        self.buttons.add(self.sizeX)
        self.sizeY = ScrollBar(self, (SCREEN_WIDTH - 180, 250), self.setting.gameRow, 15, "Number of rows")
        self.buttons.add(self.sizeY)
        self.colorbar = ColorBar(self, ((SCREEN_WIDTH - 180, 300)))
        self.buttons.add(self.colorbar)


    def event(self, e):
        """handle the events like mouse moving, key pressing,.."""
        pass

    def update(self):
        """update sprites status"""
        self.players.update()
        self.buttons.update()

    def draw(self):
        """
        draw sprites, effects, enviroment,... on the screen
        """
        self.screen.fill(Color("white"))
        self.drawBoard()
        self.drawTheSquares()
        self.players.draw(self.screen)
        self.buttons.draw(self.screen)

    def drawBoard(self):
        """
        draw the board
        """
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
        draw.line(self.screen, Color('black'), (SCREEN_WIDTH - 200, 50), (SCREEN_WIDTH - 200, SCREEN_HEIGHT - 50))

    def drawTheSquares(self):
        for x in range(self.setting.gameColumn):
            for y in range(self.setting.gameRow):
                pos = self.boardPositionToRealPosition([x, y])
                if self.realboard.get(x, y) == self.constValue["player1_went_through"]:
                    self.screen.blit(Square(Color('red'), 30), [pos[0] + 5, pos[1] + 5])
                elif self.realboard.get(x, y) == self.constValue["player2_went_through"]:
                    self.screen.blit(Square(Color('yellow'), 30), [pos[0] + 5, pos[1] + 5])

    def addPlayer(self, num, pos):
        """
        Add a new player with position: pos and id: num
        """
        poss = [self.setting.boardDeltaX + pos[0] * self.setting.squareSize,
                self.setting.boardDeltaY + pos[1] * self.setting.squareSize]
        self.players.add(Player(self, num, poss))
        self.realboard.set(pos[0], pos[1], num)

    def checkMove(self, id, direction):
        """
        Check the move is invalid or not
        """
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
            if self.realboard.get(current_pos[0], current_pos[1] - 1) in self.constValue["banned"]:
                return False
        elif direction == "down":
            if self.realboard.get(current_pos[0], current_pos[1] + 1) in self.constValue["banned"]:
                return False
        elif direction == "left":
            if self.realboard.get(current_pos[0] - 1, current_pos[1]) in self.constValue["banned"]:
                return False
        elif direction == "right":
            if self.realboard.get(current_pos[0] + 1, current_pos[1]) in self.constValue["banned"]:
                return False
        return True

    def change(self, id, pos):
        """
        mark the player with id: id through the last position and now is in the new position: pos
        """
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
        """
        Chuyển đổi từ tọa độ bàn chơi (cột, hàng)(số) sang tọa độ thực (tọa độ x, tọa độ y)(pixel).
        :param boardPos: tọa độ bàn chơi (cột, hàng)
        :return: [x, y] là tọa độ thực tính theo pixel
        """
        x = boardPos[0] * self.setting.squareSize + self.setting.boardDeltaX
        y = boardPos[1] * self.setting.squareSize + self.setting.boardDeltaY
        return [x, y]

    def setMode(self, mode):
        """
        Chỉnh lại chế độ game
        :param mode: 3 chế độ: AI-solo, Multiplayer, Pixel-art
        :return:
        """
        for i in self._game_mode:
            self._game_mode[i] = False
        self._game_mode[mode] = True

    def swapTurn(self):
        """
        Đổi lượt chơi của 2 người chơi.
        :return: Người đang có lượt sẽ nhường lượt kế tiếp cho người kia.
        """
        for player in self.players:
            player.swapTurn()

    def pause(self):
        """
        tạm dừng trò chơi
        :return:
        """
        if not self.states["pause"]:
            self.states["pause"] = True
        else:
            self.states["pause"] = False
