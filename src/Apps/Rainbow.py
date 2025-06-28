import time
from math import pi
from math import sin

from Apps.Application import Application


class Rainbow(Application):
    """docstring for Blinky"""

    def __init__(self):
        super(Rainbow, self).__init__()
        self._paintColor = (0, 0, 0)

    def update(self):
        now = time.monotonic()
        for lc in range(12):
            self.canvas[lc] = (
                127.5 * (sin((lc + 1) / 10 * ((now + 0.0) * 2 * pi)) + 1),
                127.5 * (sin((lc + 1) / 10 * ((now + 0.333) * 2 * pi)) + 1),
                127.5 * (sin((lc + 1) / 10 * ((now + 0.666) * 2 * pi)) + 1),
            )
        return super().update()
