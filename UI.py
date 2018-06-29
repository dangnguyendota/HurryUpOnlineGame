from Setting import *


class CreateHost(sprite.Sprite):
    def __init__(self, parent, pos, **kwargs):
        sprite.Sprite.__init__(self)
        self.parent = parent
        self.image = create_host_button
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.flag = {"mouseinside": False}

    def update(self):
        self.getKey()
        self.animation()

    def animation(self):
        """
        Xử lý chuyển dộng cho hình ảnh
        """
        self.parent.screen.blit(FontIomanoid_Large.render("create host",
                                                          True, Color("white"), None),
                                (self.rect.x + 10, self.rect.y + 5))

    def getKey(self):
        """
        Get key, xử lý sự kiện chuột, phím,...
        """
        keystate = key.get_pressed()
        mousepos = mouse.get_pos()
        if self.rect.x <= mousepos[0] <= self.rect.x + 120 and self.rect.y <= mousepos[1] <= self.rect.y + 40:
            self.image.fill(Color("grey"))
            self.flag["mouseinside"] = True
        else:
            self.image.fill(Color("black"))
            self.flag["mouseinside"] = False

    def action(self):
        """
        Sự kiện xảy ra khi nhấn nút,
         Sự kiện tạo máy chủ sẽ xảy ra
         Người chơi sẽ tạo một máy chủ trong game.
        """
        pass

    def readyToAction(self):
        """
        * Nhận biết chuột có đang chạm vào nút không.
        :return: True nếu chuột đang bên trong, False nếu chuột không bên trong
        """
        return self.flag["mouseinside"]


class Exit(sprite.Sprite):
    def __init__(self, parent, pos, **kwargs):
        sprite.Sprite.__init__(self)
        self.parent = parent
        self.image = exit_button
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.flag = {"mouseinside": False}

    def update(self):
        self.getKey()
        self.animation()

    def getKey(self):
        keystate = key.get_pressed()
        mousepos = mouse.get_pos()
        if self.rect.x <= mousepos[0] <= self.rect.x + 40 and self.rect.y <= mousepos[1] <= self.rect.y + 40:
            self.image.fill(Color("grey"))
            self.flag["mouseinside"] = True
        else:
            self.image.fill(Color("black"))
            self.flag["mouseinside"] = False

    def animation(self):
        self.parent.screen.blit(FontIomanoid_Large.render("Exit",
                                                          True, Color("blue"), None),
                                (self.rect.x + 7, self.rect.y + 7))

    def action(self):
        pass

    def readyToAction(self):
        """
        * Nhận biết chuột có đang chạm vào nút không.
        :return: True nếu chuột đang bên trong, False nếu chuột không bên trong
        """
        return self.flag["mouseinside"]
