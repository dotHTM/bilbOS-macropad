# Keyboard and Applications for the AdaFruit 3x4 MacroPad

Applications for the [Adafruit RP2040 3x4 Macropad](https://www.adafruit.com/product/5128).

- [store page](https://www.adafruit.com/product/5128)
- [hardware guide](https://learn.adafruit.com/adafruit-macropad-rp2040)
- [the macropad on Circuit Python](https://circuitpython.org/board/adafruit_macropad_rp2040/)
- [firmware 9.2.8](https://github.com/adafruit/circuitpython/releases/tag/9.2.8)

## How to install:

1. Install `virtualenv` via `pipx` or your `pip` of choice.
2. Load Circuit Python Firmware 9.2.8 onto your device.
3. Connect your device in disk mode.
4. Open this directory in a terminal window (MacOS) and run `make install load` to setup and load onto your device.
5. ??? (optionally test/debug on a screen session).
6. Run `make eject` to eject the disk to safely close the filesystem. If you just disconnect, you may corrupt your data

# What's Currently Implemented:

Games:

- Tic-Tac-Toe
    - designed around the MVC paradigm
    - players can play, resign, agree to draw, stalemate, undo and redo (given that no play has overwritten the redo stack)
    - key layout:
        ```
        +------------------------------------------------------+
        | screen: current | click encoder:  | rotation:        |
        |  player / state |     nothing yet |      undo / redo |
        +------------------------------------------------------+
        |       play      |       play      |       play       |
        +------------------------------------------------------+
        |       play      |       play      |       play       |
        +------------------------------------------------------+
        |       play      |       play      |       play       |
        +------------------------------------------------------+
        | resign to X/red | draw / new game | resign to O/blue |
        +------------------------------------------------------+
        ```
To Do:

- Menu system
    - json settings for quick config
    - enable disk mode for code update/editing
- Keyboard pages
    - it's a macropad for goodness sake...
- Mouse Page
    - drive the mouse with buttons, could a modern FPS (ut99) be played with this instead of a mouse?
    - mono etch-a-sketch mode
- music Page
    - speaker can beep and buzz
    - recoder & playback
    - midi mode
