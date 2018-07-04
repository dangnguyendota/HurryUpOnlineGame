"""
* Tạo khung xương cho game.
"""
from pygame import *
from pynguyen.nsetting import *


class classical_skeleton:
    def __init__(self):
        init()
        mixer.init()
        self.clock = time.Clock()
        self.running = True
        self.screen = display.set_mode((ndisplay["WIDTH"], ndisplay["HEIGHT"]))
        display.set_caption("pynguyen screen classical mode")
        display.set_icon(ndisplay['icon'])

    def new(self):
        pass

    def run(self):
        while self.running:
            for e in event.get():
                if e.type == QUIT:
                    sys.exit(1)
                self.event(e)
            self.draw()
            self.collision()
            self.update()
            display.update()
            self.clock.tick(ndisplay["FPS"])

    def event(self, e):
        """Xử lý sự kiện bàn phím, chuột"""
        pass

    def update(self):
        """Update lại các trạng thái của game"""
        pass

    def draw(self):
        """Vẽ các đối tượng lên"""
        self.screen.fill(Color('white'))

    def collision(self):
        """Xử lý va chạm"""
        pass

