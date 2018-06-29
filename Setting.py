from pynguyen.ninit import *

init()

__PATH__ = os.path.dirname(__file__)


# Setting lưu các thông số game.

class Setting:
    def __init__(self):
        option(WIDTH=700, HEIGHT=500, FPS=60)
        self.gameRow = 9  # y
        self.gameColumn = 12  # x
        self.boardDeltaX = 10
        self.boardDeltaY = 50
        self.squareSize = 40
        self.buttonAreaPos = [self.gameColumn * self.squareSize + self.boardDeltaX + 30,
                              30]


def addPos(pos1, pos2):
    return [pos1[0] + pos2[0], pos1[1] + pos2[1]]


setting = Setting()

# Font

FontIomanoid_Small = font.Font(os.path.join(__PATH__, "data/font/iomanoid.ttf"), 10)
FontIomanoid_Normal = font.Font(os.path.join(__PATH__, "data/font/iomanoid.ttf"), 15)
FontIomanoid_Large = font.Font(os.path.join(__PATH__, "data/font/iomanoid.ttf"), 20)

# Nút tạo host
create_host_button = Surface((120, 40))
create_host_button.fill(Color('black'))

# Nút quit
exit_button = Surface((50, 40))
exit_button.fill(Color("black"))
