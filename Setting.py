from pynguyen.ninit import *
from win32api import GetSystemMetrics
init()

__PATH__ = os.path.dirname(__file__)
SCREEN_WIDTH = GetSystemMetrics(0)
SCREEN_HEIGHT = GetSystemMetrics(1)
HOST = 'localhost'
PORT = 8000

# Setting lưu các thông số game.

class Setting:
    def __init__(self):
        option(WIDTH=SCREEN_WIDTH, HEIGHT=SCREEN_HEIGHT, FPS=60)
        self.gameRow = 9  # y
        self.gameColumn = 12  # x
        self.boardDeltaX = 10
        self.boardDeltaY = 50
        self.squareSize = 40
        self.buttonAreaPos = [SCREEN_WIDTH - 150,
                              30]

def addPos(pos1, pos2):
    return [pos1[0] + pos2[0], pos1[1] + pos2[1]]


setting = Setting()

# Font

FontIomanoid_Small = font.Font(os.path.join(__PATH__, "data/font/iomanoid.ttf"), 10)
FontIomanoid_Normal = font.Font(os.path.join(__PATH__, "data/font/iomanoid.ttf"), 15)
FontIomanoid_Large = font.Font(os.path.join(__PATH__, "data/font/iomanoid.ttf"), 20)
FontZorque_Small = font.Font(os.path.join(__PATH__, "data/font/zorque.ttf"), 10)
FontZorque_Normal = font.Font(os.path.join(__PATH__, "data/font/zorque.ttf"), 15)
FontZorque_Large = font.Font(os.path.join(__PATH__, "data/font/zorque.ttf"), 20)

# Nút tạo host
create_host_button = image.load(os.path.join(__PATH__, "data/texture/UI/Button1.png"))
create_host_button_pressing = image.load(os.path.join(__PATH__, "data/texture/UI/Button1-pressing.png"))

# Nút quit
exit_button = image.load(os.path.join(__PATH__, "data/texture/UI/Button2.png"))
exit_button_pressing = image.load(os.path.join(__PATH__, "data/texture/UI/Button2-pressing.png"))

# Scroll bar
scrollbar = image.load(os.path.join(__PATH__, "data/texture/UI/Scrollbar.png"))
scrollbar_background = image.load(os.path.join(__PATH__, "data/texture/UI/Scrollbar-background.png"))
small_dialog = image.load(os.path.join(__PATH__, "data/texture/UI/small-dialog.png"))
