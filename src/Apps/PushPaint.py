from Apps.Application import Application


class PushPaint(Application):
    @property
    def currentColor(self):
        return self.pallete[self.palleteIndex]

    def paint(self, i):
        if self.canvas[i] == self.currentColor:
            self.canvas[i] = 0
        else:
            self.canvas[i] = self.currentColor

    def painter(self, i):
        def inner():
            self.paint(i)

        return inner

    def inspector(self, i):
        def inner():
            print(self.canvas[i])

        return inner

    def changeColor(self, reverse=False):
        if reverse:
            self.palleteIndex += -1
        else:
            self.palleteIndex += 1
        self.palleteIndex %= len(self.pallete)
        print(self.currentColor)

    def __init__(self):
        super(PushPaint, self).__init__()
        self.palleteIndex = 0
        self.pallete = [
            0xFF0000,
            0xFFFF00,
            0x00FF00,
            0x00FFFF,
            0x0000FF,
            0xFF00FF,
            0xFFFFFF,
            0x000000,
        ]
        for i in range(12):
            self.onButtonPress(i, self.inspector(i))
            self.onButtonRelease(i, self.painter(i))
        self.onEncoderClockwise(lambda: self.changeColor())
        self.onEncoderCounterClockwise(lambda: self.changeColor(reverse=True))
