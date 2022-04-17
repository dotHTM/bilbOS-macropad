import time

from Apps.Blinky import Blinky
from Apps.Menu import Menu
from Apps.PagedApp import Button
from Apps.PagedApp import PagedApp
from Apps.PushPaint import PushPaint
from Apps.Rainbow import Rainbow
from Apps.TicTacToe import TicTacToe
from rainbowio import colorwheel
from views.ExtendedMacropad import ExtendedMacropad


def kb(k, i, r):
    return PagedApp(
        keyList=k,
        fillDirection=i,
        reverse=r,
        scrollPage=True,
    )


def testPress(i, b):
    def inner():
        print(f"    # v {i:>4} {b:>4}")

    return inner


def testRelease(i, b):
    def inner():
        print(f"    # ^ {i:>4} {b:>4}")

    return inner


def setupKeyList():
    ret = []
    exampleButtons = [
        e.upper() for e in "1234567890qwertyuiopasdfghjklzxcvbnm-=[];',./`"
    ]
    examplePageSize = len(exampleButtons)
    for i, b in enumerate(exampleButtons):

        btn = Button(
            name=b,
            colorPressed=0xFFFFFF,
            colorReleased=colorwheel(255 / examplePageSize * i),
            pressFunc=testPress(i, b),
            releaseFunc=testRelease(i, b),
        )

        btn.pressFunc()

        ret.append(btn)
    return ret


def main():

    kl = setupKeyList()

    hardware = ExtendedMacropad()

    menu = Menu(
        hardware=hardware,
        appList=[
            kb(kl, 0, False),
            TicTacToe(),
            Blinky(),
            PushPaint(),
            Rainbow(),
        ],
    )
    while True:
        menu.update()


if __name__ == "__main__":
    main()
