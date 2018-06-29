from pynguyen.nskeleton import *

option(WIDTH = 1000)
class test(classical_skeleton):
    def __init__(self):
        classical_skeleton.__init__(self)

    def draw(self):
        self.screen.fill(Color('black'))
        draw.aaline(self.screen, Color('white'), (0, 0), (50, 50), 3)

t = test()
t.new()
t.run()
