"""
* Gồm các thông số kỹ cmn thuật trong game
"""
from pygame import image, transform
import os
import sys

__PATH__ = os.path.dirname(__file__)
try:
    ndisplay = {"FPS" : 60, "WIDTH" : 500, "HEIGHT" : 500,
               "icon": image.load(os.path.join(__PATH__, "texture/pynguyen_logo.png")),
                "blue_line":{"vertical": image.load(os.path.join(__PATH__, "texture/line_blue.png")),
                             "horizontal": transform.rotate(image.load(os.path.join(__PATH__, "texture/line_blue.png")), 90)},
                "red_line": {"vertical": image.load(os.path.join(__PATH__, "texture/line_red.png")),
                              "horizontal": transform.rotate(
                                  image.load(os.path.join(__PATH__, "texture/line_red.png")), 90)},
                "green_line": {"vertical": image.load(os.path.join(__PATH__, "texture/line_green.png")),
                              "horizontal": transform.rotate(
                                  image.load(os.path.join(__PATH__, "texture/line_green.png")), 90)}
                }
except:
    print("Lỗi load dữ liệu")
    sys.exit()


def option(**kwargs):
    try:
        for setting_value in kwargs:
            ndisplay[setting_value] = kwargs[setting_value]
    except Exception:
        print("Lỗi cài đặt thông số cho game.")