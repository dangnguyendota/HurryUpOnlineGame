from Setting import *
from Server import Server
from Client import Client
from pynguyen.nsprite import *


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
        if not self.parent.states["pause"]:
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
        mouseaction = mouse.get_pressed()
        if self.mouseInsideButton():
            # self.image.fill(Color("grey"))
            self.flag["mouseinside"] = True
        else:
            # self.image.fill(Color("black"))
            self.flag["mouseinside"] = False
            self.flag["mouse_clicking"] = False

        if self.mouseInsideButton():
            if mouseaction[0]:
                self.flag["mouse_clicking"] = True
            elif not mouseaction[0] and self.flag["mouse_clicking"] and self.mouseAlready():
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
        self.flag = {"mouseinside": False, "mouse_clicking": False, "mouse_time_delay": time.get_ticks()}

    def update(self):
        self.getKey()
        self.animation()

    def getKey(self):
        mouseaction = mouse.get_pressed()
        if self.mouseInsideButton():
            # self.image.fill(Color("grey"))
            self.flag["mouseinside"] = True
        else:
            # self.image.fill(Color("black"))
            self.flag["mouseinside"] = False
            self.flag["mouse_clicking"] = False
        if self.mouseInsideButton():
            if mouseaction[0]:
                self.flag["mouse_clicking"] = True
            elif not mouseaction[0] and self.flag["mouse_clicking"] and self.mouseAlready():
                self.action()
        if not mouseaction[0]:
            self.flag["mouse_clicking"] = False

    def animation(self):
        mousepos = mouse.get_pos()
        if self.mouseInsideButton():
            # self.image = exit_button
            self.flag["mouseinside"] = True
        else:
            # self.image.fill(Color("black"))
            self.flag["mouseinside"] = False
        if not self.flag["mouse_clicking"]:
            self.image = exit_button
        else:
            self.image = exit_button_pressing
            # self.parent.screen.blit(FontIomanoid_Large.render("Exit",
            #                                                   True, Color("blue"), None),
            #                         (self.rect.x + 7, self.rect.y + 7))

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

    def mouseAlready(self):
        return (time.get_ticks() - self.flag["mouse_time_delay"]) > 200


class NewGame(sprite.Sprite):
    def __init__(self, parent, pos, **kwargs):
        sprite.Sprite.__init__(self)
        self.parent = parent
        self.image = create_host_button
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.flag = {"mouseinside": False, "mouse_time_delay": time.get_ticks(),
                     "mouse_clicking": False}
        self.server = Server()

    def update(self):
        if not self.parent.states["pause"]:
            self.getKey()
        self.animation()

    def animation(self):
        """
        Xử lý chuyển dộng cho hình ảnh
        """
        if not self.flag["mouse_clicking"]:
            self.image = create_host_button
            self.parent.screen.blit(FontIomanoid_Normal.render("NEW GAME",
                                                               True, Color("white"), None),
                                    (self.rect.x + 25, self.rect.y + 5))
        else:
            self.image = create_host_button_pressing
            self.parent.screen.blit(FontIomanoid_Normal.render("NEW GAME",
                                                               True, Color("white"), None),
                                    (self.rect.x + 25, self.rect.y + 10))

    def getKey(self):
        """
        Get key, xử lý sự kiện chuột, phím,...
        """
        mouseaction = mouse.get_pressed()
        if self.mouseInsideButton():
            # self.image.fill(Color("grey"))
            self.flag["mouseinside"] = True
        else:
            # self.image.fill(Color("black"))
            self.flag["mouseinside"] = False
            self.flag["mouse_clicking"] = False

        if self.mouseInsideButton():
            if mouseaction[0]:
                self.flag["mouse_clicking"] = True
            elif not mouseaction[0] and self.flag["mouse_clicking"] and self.mouseAlready():
                self.action()
        if not mouseaction[0]:
            self.flag["mouse_clicking"] = False

    def action(self):
        """
        Sự kiện xảy ra khi nhấn nút,
        """
        self.flag["mouse_time_delay"] = time.get_ticks()
        self.parent.setting.gameColumn = self.parent.sizeX.getCurrentSize()
        self.parent.setting.gameRow = self.parent.sizeY.getCurrentSize()
        self.parent.new()

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


class PauseGame(sprite.Sprite):
    def __init__(self, parent, pos, **kwargs):
        sprite.Sprite.__init__(self)
        self.parent = parent
        self.image = create_host_button
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.flag = {"mouseinside": False, "mouse_time_delay": time.get_ticks(),
                     "mouse_clicking": False, "game_pause": False}
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
            if not self.flag["game_pause"]:
                self.parent.screen.blit(FontIomanoid_Normal.render("PAUSE",
                                                                   True, Color("white"), None),
                                        (self.rect.x + 40, self.rect.y + 5))
            else:
                self.parent.screen.blit(FontIomanoid_Normal.render("RESUME",
                                                                   True, Color("white"), None),
                                        (self.rect.x + 35, self.rect.y + 5))
        else:
            self.image = create_host_button_pressing
            if not self.flag["game_pause"]:
                self.parent.screen.blit(FontIomanoid_Normal.render("PAUSE",
                                                                   True, Color("white"), None),
                                        (self.rect.x + 40, self.rect.y + 10))
            else:
                self.parent.screen.blit(FontIomanoid_Normal.render("RESUME",
                                                                   True, Color("white"), None),
                                        (self.rect.x + 35, self.rect.y + 10))

    def getKey(self):
        """
        Get key, xử lý sự kiện chuột, phím,...
        """
        mouseaction = mouse.get_pressed()
        if self.mouseInsideButton():
            # self.image.fill(Color("grey"))
            self.flag["mouseinside"] = True
        else:
            # self.image.fill(Color("black"))
            self.flag["mouseinside"] = False
            self.flag["mouse_clicking"] = False

        if self.mouseInsideButton():
            if mouseaction[0]:
                self.flag["mouse_clicking"] = True
            elif not mouseaction[0] and self.flag["mouse_clicking"] and self.mouseAlready():
                self.action()
        if not mouseaction[0]:
            self.flag["mouse_clicking"] = False

    def action(self):
        """
        Sự kiện xảy ra khi nhấn nút,
        """
        self.flag["mouse_time_delay"] = time.get_ticks()
        if self.flag["game_pause"] == True:
            self.flag["game_pause"] = False
        else:
            self.flag["game_pause"] = True
        self.parent.pause()

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


class ScrollBar(sprite.Sprite):
    def __init__(self, parent, pos, start_size, max_size, name=None):
        sprite.Sprite.__init__(self)
        self.parent = parent
        self.pos = pos
        self.name = name
        self.unit = 123 // max_size
        self.image = scrollbar
        self.rect = self.image.get_rect()
        self.rect.x = pos[0] + start_size * self.unit
        self.rect.y = pos[1]
        self.default_setting = {"current-value": start_size, "max-size": max_size, "mouse-clicking": False}

    def update(self):
        self.animation()
        if not self.parent.states["pause"]:
            self.getKey()

    def getKey(self):
        mouseaction = mouse.get_pressed()
        mouse_pos = mouse.get_pos()
        if self.mouseInsideButton():
            self.showSizeToScreen([mouse_pos[0] - 10, mouse_pos[1] - 35])

        if self.mouseInsideButton(False):
            if mouseaction[0]:
                self.default_setting["mouse-clicking"] = True
            else:
                self.default_setting["mouse-clicking"] = False
        else:
            self.default_setting["mouse-clicking"] = False
        if self.default_setting["mouse-clicking"]:
            if self.pos[0] + 16 < mouse_pos[0] < self.pos[0] + 134:
                self.rect.x = mouse_pos[0] - 16

    def animation(self):
        self.parent.screen.blit(scrollbar_background, self.pos)
        if self.name:
            text = FontIomanoid_Large.render(self.name, True, (4, 51, 0))
            self.parent.screen.blit(text, (self.pos[0], self.pos[1] - 20))
            draw.line(self.parent.screen, Color('black'), self.pos, (self.pos[0] + 150, self.pos[1]))

    def mouseInsideButton(self, really=True):
        """
        :return: Chuột đang trong nút hay không?
        """
        mousepos = mouse.get_pos()
        if really:
            return self.rect.x + 5 <= mousepos[0] <= self.rect.x + 26 and self.rect.y + 8 <= mousepos[
                1] <= self.rect.y + 22
        else:
            return self.pos[0] + 16 < mousepos[0] < self.pos[0] + 134 and self.rect.y + 8 <= mousepos[
                1] <= self.rect.y + 22

    def getCurrentSize(self):
        """
        Lấy kích thước của scroll hiện tại
        :return:
        """
        size = (self.rect.x - self.pos[0]) // self.unit
        if size <= 0:
            return 1
        return size

    def showSizeToScreen(self, pos):
        self.parent.screen.blit(small_dialog, pos)
        text = FontZorque_Normal.render(str(self.getCurrentSize()), True, Color("black"))
        if self.getCurrentSize() >= 10:
            self.parent.screen.blit(text, (pos[0] + 3, pos[1] + 5))
        else:
            self.parent.screen.blit(text, (pos[0] + 8, pos[1] + 5))


class ColorBar(sprite.Sprite):
    def __init__(self, parent, pos):
        sprite.Sprite.__init__(self)
        self.parent = parent
        self.pos = pos
        self.image = Surface((23, 261))
        self.image.fill(Color('black'))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0] - 1
        self.rect.y = pos[1] - 1
        self.pull_pos = [pos[0]-1, pos[1]]
        self.field_pos = [pos[0] + 30, pos[1] + 70]
        self.choose_color_button = [self.field_pos[0] + 130, self.field_pos[1]]

    def update(self):
        self.animation()
        self.getKey()

    def animation(self):
        drawSquare(self.parent.screen, (self.pos[0] + 30, self.pos[1]), self.getColorFieldResult(), Color('black'),
                   (40, 40))
        drawSquare(self.parent.screen, self.field_pos, Color('grey'), Color('grey'),
                   (132, 131))
        # Vẽ thanh quận chọn màu
        for x in range(43):
            draw.line(self.parent.screen, (255, 0, x * 6), (self.pos[0], self.pos[1] + x),
                      (self.pos[0] + 20, self.pos[1] + x), 1)
            draw.line(self.parent.screen, (255 - x * 6, 0, 255), (self.pos[0], self.pos[1] + x + 43),
                      (self.pos[0] + 20, self.pos[1] + x + 43), 1)
            draw.line(self.parent.screen, (0, x * 6, 255), (self.pos[0], self.pos[1] + x + 86),
                      (self.pos[0] + 20, self.pos[1] + x + 86), 1)
            draw.line(self.parent.screen, (0, 255, 255 - x * 6), (self.pos[0], self.pos[1] + x + 129),
                      (self.pos[0] + 20, self.pos[1] + x + 129), 1)
            draw.line(self.parent.screen, (x * 6, 255, 0), (self.pos[0], self.pos[1] + x + 172),
                      (self.pos[0] + 20, self.pos[1] + x + 172), 1)
            draw.line(self.parent.screen, (255, 255 - x * 6, 0), (self.pos[0], self.pos[1] + x + 215),
                      (self.pos[0] + 20, self.pos[1] + x + 215), 1)
        # Vẽ hộp chọn màu chi tiết
        (r, g, b) = self.getPullResult()
        rx, gx, bx = (255 - r) / 130, (255 - g) / 130, (255 - b) / 130
        print(rx, gx, bx)
        for x in range(130):
            for y in range(130):
                draw.line(self.parent.screen,
                          (int(r + rx * x - (r + rx * x) * y / 130), int(g + gx * x - (g + gx * x) * y / 130),
                           int(b + bx * x - (b + bx * x) * y / 130)),
                          [self.field_pos[0] + 130 - x, self.field_pos[1] + y],
                          [self.field_pos[0] + 130 - x, self.field_pos[1] + y], 1)

        # Linh tinh
        self.parent.screen.blit(pull_button, self.pull_pos)
        draw.circle(self.parent.screen, Color("white"), self.choose_color_button, 3, 2)
        self.showResult()
        # mouse_pos = mouse.get_pos()
        # if self.mouseInsideColorBar():
        #     self.showResultToScreen([mouse_pos[0] - 10, mouse_pos[1] - 35])
        # if self.mouseInsideColorField():
        #     self.showChooseColor([mouse_pos[0] - 100, mouse_pos[1] - 35])

    def getKey(self):
        mouseacion = mouse.get_pressed()
        mouse_pos = mouse.get_pos()
        if self.mouseInsideButton():
            if mouseacion[0] and -1 < (mouse_pos[1] - self.pos[1]) // 43 < 6:
                self.pull_pos[1] = mouse_pos[1]
        if self.mouseInsideColorField():
            if mouseacion[0]:
                self.choose_color_button = mouse.get_pos()

    def mouseInsideButton(self):
        """
        :return: Chuột đang trong nút hay không?
        """
        mousepos = mouse.get_pos()
        return self.rect.x + 1 <= mousepos[0] <= self.rect.x + 21 and self.rect.y + 1 <= mousepos[
            1] <= self.rect.y + 259

    def mouseInsideColorBar(self):
        """
        :return: Chuột đang trong nút hay không?
        """
        mouse_pos = mouse.get_pos()
        return 0 <= mouse_pos[0] - self.pull_pos[0] <= 20 and 0 <= mouse_pos[1] - self.pull_pos[1] <= 10

    def mouseInsideColorField(self):
        mouse_pos = mouse.get_pos()
        return 0 <= mouse_pos[0] - self.field_pos[0] <= 130 and 0 <= mouse_pos[1] - self.field_pos[1] <= 130

    def getPullResult(self):
        thuong = (self.pull_pos[1] - self.pos[1]) // 43
        du = (self.pull_pos[1] - self.pos[1]) % 43
        if thuong == 0:
            return (255, 0, du * 6)
        elif thuong == 1:
            return (255 - du * 6, 0, 255)
        elif thuong == 2:
            return (0, du * 6, 255)
        elif thuong == 3:
            return (0, 255, 255 - du * 6)
        elif thuong == 4:
            return (du * 6, 255, 0)
        elif thuong == 5:
            return (255, 255 - du * 6, 0)

    def getColorFieldResult(self):
        (r, g, b) = self.getPullResult()
        rx, gx, bx = (255 - r) / 130, (255 - g) / 130, (255 - b) / 130
        x, y = self.field_pos[0] + 130 - self.choose_color_button[0], self.choose_color_button[1] - self.field_pos[1]
        return (int(r + rx * x - (r + rx * x) * y / 130), int(g + gx * x - (g + gx * x) * y / 130),
                 int(b + bx * x - (b + bx * x) * y / 130))

    def showResultToScreen(self, pos):
        self.parent.screen.blit(normal_dialog, pos)
        text = FontZorque_Normal.render(str(self.getPullResult()), True, Color("black"))
        self.parent.screen.blit(text, (pos[0] + 10, pos[1] + 5))

    def showChooseColor(self, pos):
        self.parent.screen.blit(normal_dialog, pos)
        (r, g, b) = self.getPullResult()
        rx, gx, bx = (255 - r) / 130, (255 - g) / 130, (255 - b) / 130
        x, y = self.field_pos[0] + 130 - mouse.get_pos()[0], mouse.get_pos()[1] - self.field_pos[1]
        text = FontZorque_Normal.render(
            str((int(r + rx * x - (r + rx * x) * y / 130), int(g + gx * x - (g + gx * x) * y / 130),
                 int(b + bx * x - (b + bx * x) * y / 130))), True, Color("black"))
        self.parent.screen.blit(text, (pos[0] + 10, pos[1] + 5))

    def showResult(self):
        cl = self.getColorFieldResult()
        r = FontZorque_Normal.render("R:  "+str(cl[0]), True, Color("black"))
        g = FontZorque_Normal.render("G:  " + str(cl[1]), True, Color("black"))
        b = FontZorque_Normal.render("B:  " + str(cl[2]), True, Color("black"))
        self.parent.screen.blit(r, (self.pos[0] + 80, self.pos[1]))
        self.parent.screen.blit(g, (self.pos[0] + 80, self.pos[1]+15))
        self.parent.screen.blit(b, (self.pos[0] + 80, self.pos[1]+30))

