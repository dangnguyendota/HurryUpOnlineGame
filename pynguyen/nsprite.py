from pygame import *


class Button2Image(sprite.Sprite):
    def __init__(self, parent, pos, image1, image2):
        sprite.Sprite.__init__(self)
        self.parent = parent
        self.pos = pos
        self.image = image1
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.image1 = image1
        self.image2 = image2
        self.default_flag = {"mouse_clicking": False, "mouseinside": False, "mouse_time_delay": time.get_ticks()}
        self._mouse_delay_maxTime = 200

    def update(self):
        self.animation()
        self.checkmouse()

    def animation(self):
        if not self.default_flag["mouse_clicking"]:
            self.image = self.image1
        else:
            self.image = self.image2

    def checkmouse(self):
        mouseaction = mouse.get_pressed()
        if self.mouseInsideButton():
            self.default_flag["mouseinside"] = True
        else:
            self.default_flag["mouseinside"] = False
        if self.mouseInsideButton():
            if mouseaction[0]:
                self.default_flag["mouse_clicking"] = True
            elif not mouseaction[0] and self.default_flag["mouse_clicking"] and self.mouseAlready():
                self.action()
        if not mouseaction[0]:
            self.default_flag["mouse_clicking"] = False

    def mouseInsideButton(self):
        """
        :return: Chuột đang trong nút hay không?
        """
        mousepos = mouse.get_pos()
        return self.rect.x <= mousepos[0] <= self.rect.x + self.image.get_width() and self.rect.y <= mousepos[
            1] <= self.rect.y + self.image.get_height()

    def mouseAlready(self):
        return (time.get_ticks() - self.default_flag["mouse_time_delay"]) > self._mouse_delay_maxTime

    def setTimeDelay(self, time):
        self._mouse_delay_maxTime = time

    def action(self):
        pass
