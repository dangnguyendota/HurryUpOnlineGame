from Setting import *

class CreateHost(sprite.Sprite):
    def __init__(self, parent):
        sprite.Sprite.__init__(self)
        self.parent = parent

    def update(self):
        self.animation()

    def animation(self):
        """Xử lý chuyển dộng cho hình ảnh"""
        pass

    def getKey(self):
        """Get key, xử lý sự kiện chuột, phím,..."""
        keystate = key.get_pressed()

    def action(self):
        """
        Sự kiện xảy ra khi nhấn nút,
         Sự kiện tạo máy chủ sẽ xảy ra
         Người chơi sẽ tạo một máy chủ trong game.
        """