import random
from math import cos
from math import pi
from time import monotonic

from Apps.Application import Application
from rainbowio import colorwheel


class Blinky(Application):
    """docstring for BlinkyVC"""

    def __init__(self):
        super(Blinky, self).__init__()
        self.blinkenRates = []
        self.blinkenOffsets = []
        self.blinkenColorAngles = []

        for _ in range(12):
            self.blinkenRates.append(random.randrange(1, 32) / 64)
            self.blinkenOffsets.append(random.randrange(1, 32) / 64)
            self.blinkenColorAngles.append(random.randrange(1, 255))

    def mutateBlinken(self):
        pass

        h = 100

        for b in range(12):
            self.blinkenRates[b] += (random.randrange(0, 2 * h) - h) / (1000000 * h)
            if self.canvas[b] == 0:
                self.blinkenColorAngles[b] += (random.randrange(0, 2 * h) - h) / h
                self.blinkenColorAngles[b] %= 255
            else:
                self.blinkenOffsets[b] += (random.randrange(0, 2 * h) - h) / (10000 * h)

    def update(self):
        now = monotonic()
        for b in range(12):
            color = 0x0
            if 0 < cos(self.blinkenRates[b] * (now + self.blinkenOffsets[b]) * 2 * pi):
                color = colorwheel(self.blinkenColorAngles[b])
            self.canvas[b] = color
        self.mutateBlinken()
        return super().update()
