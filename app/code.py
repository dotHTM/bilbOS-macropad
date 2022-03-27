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

kl = []

# print(f"{type(Menu).__name__=}")
# print(f"{Menu=}")
# print(f"{isinstance(Menu, type)=}")
# print("-" * 16)

# x = Menu(hardware=ExtendedMacropad())
# print(f"{type(x).__name__=}")
# print(f"{x=}")
# print(f"{isinstance(x, Menu)=}")


exampleButtons = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
    "Q",
    "W",
    "E",
    "R",
    "T",
    "Y",
    "U",
    "I",
    "O",
    "P",
    "A",
    "S",
    "D",
    "F",
    "G",
    "H",
    "J",
    "K",
    "L",
    "Z",
    "X",
    "C",
    "V",
    "B",
    "N",
    "M",
]

examplePageSize = len(exampleButtons)
for i in range(examplePageSize):

    kl.append(
        Button(
            name=exampleButtons[i],
            colorPressed=0xFFFFFF,
            # colorPressed=colorwheel(255 / examplePageSize * i + 128),
            colorReleased=colorwheel(255 / examplePageSize * i),
            pressFunc=lambda: print("# v i"),
            releaseFunc=lambda: print("# ^ i"),
        ),
    )
    pass


def kb(k, i, r):
    return PagedApp(
        keyList=kl,
        fillDirection=i,
        reverse=r,
        scrollPage=True,
    )


def main():

    hardware = ExtendedMacropad()

    menu = Menu(
        hardware=hardware,
        appList=[
            kb(hardware.keyboard, 0, False),
            kb(hardware.keyboard, 1, False),
            kb(hardware.keyboard, 2, False),
            kb(hardware.keyboard, 3, False),
            # TicTacToe(),
            # Blinky(),
            # PushPaint(),
            # Rainbow(),
        ],
    )
    while True:
        menu.update()


if __name__ == "__main__":
    main()
