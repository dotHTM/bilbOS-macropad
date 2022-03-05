import time

from Apps.Blinky import Blinky
from Apps.Menu import Menu
from Apps.PushPaint import PushPaint
from Apps.Rainbow import Rainbow
from Apps.TicTacToe import TicTacToe


def main():
    menu = Menu(
        appList=[
            TicTacToe(),
            Blinky(),
            PushPaint(),
            Rainbow(),
        ]
    )
    while True:
        menu.update()


if __name__ == "__main__":
    main()
