# from typing import Union
from Suppliment.Keyboard import KeyData
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

import json
import re

from Apps.Application import Application
from displayio import Display
from utils import rotate
from utils import transpose
from Views.DisplayGrid import Grid12
from Apps.Button import Button


class PagedApp(Application):
    """docstring for pagedApp"""

    def __init__(
        self,
        keyList: list[Button] = [],
        fillDirection: int = 0,
        reverse=False,
        scrollPage=False,
    ) -> None:
        super(PagedApp, self).__init__()
        fillDirection %= 4

        self.direction = fillDirection
        self.displayType = Grid12

        fillWidth = 4
        fillHeight = 3
        if fillDirection % 2 == 0:
            fillWidth = 3
            fillHeight = 4

        self.scrollSize = 1
        if scrollPage:
            self.scrollSize = fillHeight

        blankID = 0

        self.keyGrid = []
        row = []
        for k in keyList:
            row.append(k)
            if len(row) == fillWidth:
                self.keyGrid.append(row)
                row = []
        while (
            0 < len(row)
            or len(self.keyGrid) < fillHeight
            or (len(self.keyGrid) - fillHeight) % self.scrollSize != 0
        ):

            while len(row) < fillWidth:
                row.append(Button(name=""))
                blankID += 1
            self.keyGrid.append(row)
            row = []

        if reverse:
            lc = 0
            while lc < len(self.keyGrid):
                self.keyGrid[lc] = list(reversed(self.keyGrid[lc]))
                lc += 1

        self.viewOffsetRange = len(self.keyGrid) - fillHeight
        self.viewOffset = 0
        if self.direction == 1 or self.direction == 2:
            self.viewOffset = self.viewOffsetRange

        for _ in range(fillDirection):
            self.keyGrid = rotate(self.keyGrid)

        self.onEncoderClockwise(self.incrementView)
        self.onEncoderCounterClockwise(self.decrementView)

        self.changedPage = True

        self.displayView = None

    @property
    def flattenedCurrentPage(self) -> list[Button]:
        res = []
        for row in self.currentPage:
            for e in row:
                res.append(e)
        return res

    def displayUpdate(self):
        fcp = self.flattenedCurrentPage
        for i in range(12):
            self.canvas[i] = fcp[i].colorReleased
        return {
            "title": self.name,
            "labels": [e.name for e in fcp],
        }

    def update(self) -> None:
        if self.changedPage:
            self.displayUpdate()
            self.changedPage = False

    def incrementView(self) -> None:
        if self.viewOffset < self.viewOffsetRange:
            self.viewOffset += self.scrollSize
            self.changedPage = True

    def decrementView(self) -> None:
        if 0 < self.viewOffset:
            self.viewOffset += -self.scrollSize
            self.changedPage = True

    def verticalPage(self, offset) -> list[list[Button]]:
        self.keyGrid
        res: list[list[Button]] = []
        for r in range(offset, offset + 4):
            res.append(self.keyGrid[r])
        return res

    def horizontalPage(self, offset) -> list[list[Button]]:
        workingGrid = self.keyGrid
        workingGrid = rotate(workingGrid)
        res: list[list[Button]] = []
        for r in range(offset, offset + 3):
            res.append(workingGrid[r])
        for _ in range(3):
            res = rotate(res)
        return res

    @property
    def currentPage(self) -> list[list[Button]]:
        if self.direction % 2 == 0:
            return self.verticalPage(self.viewOffset)
        else:
            return self.horizontalPage(self.viewOffset)

    @property
    def pressedActions(self):
        def buttonAction(i):
            e = self.flattenedCurrentPage[i]

            def inner():
                self.canvas[i] = e.colorPressed
                print(f"v {i} {e.colorPressed} v")
                if callable(e.pressFunc):
                    e.pressFunc()

            return inner

        return [buttonAction(i) for i in range(12)]

    @property
    def releasedActions(self):
        def buttonAction(i):
            e = self.flattenedCurrentPage[i]

            def inner():
                self.canvas[i] = e.colorReleased
                print(f"^ {i} {e.colorReleased} ^")

                if callable(e.releaseFunc):
                    e.releaseFunc()

            return inner

        return [buttonAction(i) for i in range(12)]


class KeyBoardApp(PagedApp):
    def __init__(
        self,
        keyboard: Keyboard,
        KeyButtonList=[],
        fillDirection: int = 0,
        reverse=False,
        scrollPage=False,
    ) -> None:
        self.keyboard = keyboard
        keyList = []
        for e in kcListList:
            btn = Button(
                name=e,
                keycode=KeyData.byName(e).keycode,
                colorPressed=0xFFFFFF,
                colorReleased=0xFFAAAA,
            )
            keyList.append(btn)

        super().__init__(keyList, fillDirection, reverse, scrollPage)
