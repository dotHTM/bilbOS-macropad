# Application and (eventually) Keyboard Firmware for the AdaFruit 3x4 MacroPad

Circuit Python firmware for the [Adafruit RP2040 3x4 Macropad](https://www.adafruit.com/product/5128).

This is an in-progress project, and is not fully functional at present.

What's Currently Implemented:

Games:

- Tic-Tac-Toe
    - designed around the MVC paradigm
    - players can play, resign, agree to draw, stalemate, undo and redo (given that no play has overwritten the redo stack)
    - key layout:
        
        | screen: current player / state | click encoder: exit (not implemented) | encoder rotation: undo / redo |
        |-|
        | play | play | play |
        | play | play | play |
        | play | play | play |
        | resign to X / red | agree to draw | resign to O / blue |

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
