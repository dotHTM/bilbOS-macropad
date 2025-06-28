# import time

from Apps.Blinky import Blinky
from Apps.Menu import Menu

# from Apps.PagedApp import Button
# from Apps.PagedApp import PagedApp
# from Apps.PagedApp import KeyBoardApp

from Apps.KeyBoardApp import KeyBoardApp, WASD, Numpad, AnimeBoxesController, Phonepad
from Apps.PushPaint import PushPaint
from Apps.Rainbow import Rainbow
from Apps.TicTacToe import TicTacToe
from rainbowio import colorwheel
from Views.ExtendedMacropad import ExtendedMacropad

from adafruit_hid.keycode import Keycode as KC


# def kb(keyboard, k, i, r):
#     return KeyBoardApp(
#         keyboard=keyboard,
#         kcListList=k,
#         fillDirection=i,
#         reverse=r,
#         scrollPage=True,
#     )


# def testPress(i, b):
#     def inner():
#         print(f"    # v {i:>4} {b:>4}")

#     return inner


# def testRelease(i, b):
#     def inner():
#         print(f"    # ^ {i:>4} {b:>4}")

#     return inner


def applist(hardware):
    # kl = setupKeyList()

    ekc = [e for e in "qwerasdfzxcv"]

    return [
        WASD(),
        Numpad(),
        TicTacToe(),
        Blinky(),
        PushPaint(),
        Rainbow(),
        AnimeBoxesController(),
        Phonepad(),
    ]


def main():

    hardware = ExtendedMacropad()

    menu = Menu(
        hardware=hardware,
        appList=applist(hardware),
    )
    while True:
        menu.update()


if __name__ == "__main__":
    main()
