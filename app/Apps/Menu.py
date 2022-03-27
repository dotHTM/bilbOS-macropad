from time import sleep

from Apps.Application import Application
from Apps.PushPaint import PushPaint
from Suppliment.Keyboard import KeyData
from views.DisplayGrid import DisplayAbstraction
from views.ExtendedMacropad import ExtendedMacropad


class Menu:
    """Base Level Menu View Controller"""

    def __init__(
        self,
        hardware: ExtendedMacropad,
        brightness=0.1,
        appList: list[Application] = [
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
        if callable(self.currentApp._FocusFunc):
            self.currentApp._FocusFunc()

        self.menuEnabled = False

        self.display = None
        self.displayType = None
        self.updateDisplay()

    def updateDisplay(self):
        if self.currentApp.displayType != self.displayType:
            print("changing view")
            if isinstance(self.currentApp.displayType, type):
                print("its advanced")
                self.display = None
                self.displayType = self.currentApp.displayType
                self.display = self.currentApp.displayType(self.hardware.display)
            else:
                print("its plain")
                self.display = None
                self.displayType = None

        if self.display != None:
            self.display.update(self.currentApp.displayUpdate())

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
                print("menu")
            else:
                print("app")

        if self.menuEnabled:
            oldApp = self.currentApp
            self.appIndex += self.hardware.encoder_direction
            self.appIndex %= len(self.appList)
            if self.hardware.encoder_direction != 0:
                print(f"{type(self.currentApp).__name__} {self.appIndex}")

                actionQueue.append(oldApp._FocusLostFunc)
                actionQueue.append(self.currentApp._FocusFunc)
        else:

            # if self.hardware.encoder_pressed:
            #     actionQueue.append(self.currentApp._EncoderPress)
            # if self.hardware.encoder_released:
            #     actionQueue.append(self.currentApp._EncoderRelease)

            if self.hardware.encoder_direction != 0:
                actionQueue.append(
                    self.currentApp.encoderRotateActions[
                        self.hardware.encoder_direction
                    ]
                )
            for b in self.hardware.newPressedKeys:
                # print(f"v{b}")
                action = self.currentApp.pressedActions[b]
                actionQueue.append(action)
            for b in self.hardware.newReleasedKeys:
                # print(f"^{b}")
                action = self.currentApp.releasedActions[b]
                actionQueue.append(action)

        for a in actionQueue:
            if callable(a):
                a()

        self.updateDisplay()

        self.currentApp.update()
        for i in range(12):
            self.hardware.pixels[i] = self.currentApp.canvas[i]

    def loop(self):
        while True:
            self.update()
