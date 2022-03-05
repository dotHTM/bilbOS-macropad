from time import sleep

from Apps.PushPaint import PushPaint
from views.ExtendedMacropad import ExtendedMacropad


class Menu:
    """Base Level Menu View Controller"""

    def __init__(
        self,
        hardware=ExtendedMacropad(),
        brightness=0.1,
        appList=[
            PushPaint(),
        ],
        loopDelay=0.001,
    ):
        super(Menu, self).__init__()

        self.loopDelay = loopDelay

        self.appList = appList

        self.hardware = hardware
        self.hardware.pixels.brightness = brightness
        self.appIndex = 0

        self.menuEnabled = False

    @property
    def currentApp(self):
        return self.appList[self.appIndex]

    def update(self):
        sleep(self.loopDelay)
        self.hardware.update()

        actionQueue = []
        if self.hardware.encoder_pressed:
            self.menuEnabled = not self.menuEnabled
            if self.menuEnabled:
                actionQueue.append(self.currentApp._FocusLostFunc)
                print("menu")
            else:
                print("app")
                actionQueue.append(self.currentApp._FocusFunc)

        if self.menuEnabled:
            self.appIndex += self.hardware.encoder_direction
            self.appIndex %= len(self.appList)
            currentApp = self.appList[self.appIndex]
            if self.hardware.encoder_direction != 0:
                print(f"{type(currentApp).__name__} {self.appIndex}")
        else:

            if self.hardware.encoder_pressed:
                actionQueue.append(self.currentApp._EncoderPress)
            if self.hardware.encoder_released:
                actionQueue.append(self.currentApp._EncoderRelease)

            if self.hardware.encoder_direction != 0:
                actionQueue.append(
                    self.currentApp.encoderRotateActions[
                        self.hardware.encoder_direction
                    ]
                )
            for b in self.hardware.newPressedKeys:
                actionQueue.append(self.currentApp.pressedActions[b])
            for b in self.hardware.newReleasedKeys:
                actionQueue.append(self.currentApp.releasedActions[b])

        for a in actionQueue:
            if callable(a):
                a()

        self.currentApp.update()
        for i in range(12):
            self.hardware.pixels[i] = self.currentApp.canvas[i]

    def loop(self):
        while True:
            self.update()
