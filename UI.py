from Setting import *
from Server import Server
from Client import Client


class CreateHost(sprite.Sprite):
    def __init__(self, parent, pos, **kwargs):
        sprite.Sprite.__init__(self)
        self.parent = parent
        self.image = create_host_button
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.flag = {"mouseinside": False, "connecting": False, "mouse_time_delay": time.get_ticks(),
                     "mouse_clicking": False}
        self.server = Server()

    def update(self):
        self.getKey()
        self.animation()

    def animation(self):
        """
        Xử lý chuyển dộng cho hình ảnh
        """
        if not self.flag["mouse_clicking"]:
            self.image = create_host_button
            if not self.flag["connecting"]:
                self.parent.screen.blit(FontIomanoid_Normal.render("create host",
                                                                   True, Color("white"), None),
                                        (self.rect.x + 18, self.rect.y + 5))
            else:
                self.parent.screen.blit(FontIomanoid_Normal.render("connecting!",
                                                                   True, Color("white"), None),
                                        (self.rect.x + 18, self.rect.y + 5))
        else:
            self.image = create_host_button_pressing
            if not self.flag["connecting"]:
                self.parent.screen.blit(FontIomanoid_Normal.render("create host",
                                                                   True, Color("white"), None),
                                        (self.rect.x + 18, self.rect.y + 10))
            else:
                self.parent.screen.blit(FontIomanoid_Normal.render("connecting!",
                                                                   True, Color("white"), None),
                                        (self.rect.x + 18, self.rect.y + 10))

    def getKey(self):
        """
        Get key, xử lý sự kiện chuột, phím,...
        """
        keystate = key.get_pressed()
        mouseaction = mouse.get_pressed()
        if self.mouseInsideButton():
            # self.image.fill(Color("grey"))
            self.flag["mouseinside"] = True
        else:
            # self.image.fill(Color("black"))
            self.flag["mouseinside"] = False
        if self.mouseInsideButton():
            if mouseaction[0]:
                self.flag["mouse_clicking"] = True
            elif not mouseaction[0] and self.flag["mouse_clicking"]  and self.mouseAlready():
                self.action()
        if not mouseaction[0]:
            self.flag["mouse_clicking"] = False

    def action(self):
        """
        Sự kiện xảy ra khi nhấn nút,
         Sự kiện tạo máy chủ sẽ xảy ra
         Người chơi sẽ tạo một máy chủ trong game.
        """
        if self.flag["connecting"] == False:
            self.flag["connecting"] = True
            # self.server.connect(HOST, PORT)
        else:
            self.flag["connecting"] = False
            # self.server.disconnect()
        self.flag["mouse_time_delay"] = time.get_ticks()

    def readyToAction(self):
        """
        * Nhận biết chuột có đang chạm vào nút không.
        :return: True nếu chuột đang bên trong, False nếu chuột không bên trong
        """
        return self.flag["mouseinside"]

    def mouseInsideButton(self):
        """
        :return: Chuột đang trong nút hay không?
        """
        mousepos = mouse.get_pos()
        return self.rect.x <= mousepos[0] <= self.rect.x + self.image.get_width() and self.rect.y <= mousepos[
            1] <= self.rect.y + self.image.get_height()

    def mouseAlready(self):
        return (time.get_ticks() - self.flag["mouse_time_delay"]) > 200


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
        mouseaction = mouse.get_pressed()
        if mouseaction[0] and self.mouseInsideButton():
            self.action()

    def animation(self):
        mousepos = mouse.get_pos()
        if self.mouseInsideButton():
            self.image.fill(Color("grey"))
            self.flag["mouseinside"] = True
        else:
            self.image.fill(Color("black"))
            self.flag["mouseinside"] = False
        self.parent.screen.blit(FontIomanoid_Large.render("Exit",
                                                          True, Color("blue"), None),
                                (self.rect.x + 7, self.rect.y + 7))

    def action(self):
        sys.exit(0)

    def readyToAction(self):
        """
        * Nhận biết chuột có đang chạm vào nút không.
        :return: True nếu chuột đang bên trong, False nếu chuột không bên trong
        """
        return self.flag["mouseinside"]

    def mouseInsideButton(self):
        """
        Chuột nằm trong nút ấn
        :return:
        """
        mousepos = mouse.get_pos()
        return self.rect.x <= mousepos[0] <= self.rect.x + self.image.get_width() and self.rect.y <= mousepos[
            1] <= self.rect.y + self.image.get_height()
