from Apps.Application import Application
from rainbowio import colorwheel

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode as KC

from Views.DisplayGrid import Grid12


def noop(*a, **kwa):
    return


class KeyBoardApp(Application):
    def __init__(self, name="Keyboard", keyOrder=[]) -> None:
        super(KeyBoardApp, self).__init__()
        self.name = name

        self.displayType = Grid12

        self.keyOrder = keyOrder

        self.canvas = [kcPixel[el[0]] for el in self.keyOrder if el[0] in kcPixel]

        self._Buttons = []
        for kcList in keyOrder:
            self._Buttons.append(
                [
                    self.kcPress(kcList),
                    self.kcRelease(kcList),
                ],
            )

        while len(self._Buttons) < 12:
            self._Buttons.append([noop(), noop()])

    # def kcPress(self, kcList):
    #     def inner():
    #         for k in kcList:
    #             self.kcPressBuffer.append(k)

    #     return inner

    # def kcRelease(self, kcList):
    #     def inner():
    #         for k in reversed(kcList):
    #             self.kcReleaseBuffer.append(k)

    #     return inner

    def displayUpdate(self):
        return {
            "title": self.name,
            "labels": [
                " ".join([kcLabel[i] for i in el if i in kcLabel])
                for el in self.keyOrder
            ],
        }


class WASD(KeyBoardApp):
    def __init__(self) -> None:
        super().__init__(
            name="WASD",
            keyOrder=[
                [KC.SHIFT],
                [KC.A],
                [KC.Q],
                [KC.X],
                [KC.S],
                [KC.W],
                [KC.C],
                [KC.D],
                [KC.E],
                [KC.SPACE],
                [KC.F],
                [KC.R],
            ],
        )


class AnimeBoxesController(KeyBoardApp):
    def __init__(self) -> None:
        super().__init__(
            name="Anime Boxes",
            keyOrder=[
                [KC.SHIFT],
                [KC.LEFT_ARROW],
                [KC.I],
                [KC.COMMAND, KC.S],
                [KC.DOWN_ARROW],
                [KC.UP_ARROW],
                [KC.O],
                [KC.RIGHT_ARROW],
                [KC.U],
                [KC.SPACE],
                [KC.F],
                [KC.R],
            ],
        )


class Numpad(KeyBoardApp):
    def __init__(self) -> None:
        super().__init__(
            name="Number Pad",
            keyOrder=[
                [KC.KEYPAD_SEVEN],
                [KC.KEYPAD_EIGHT],
                [KC.KEYPAD_NINE],
                [KC.KEYPAD_FOUR],
                [KC.KEYPAD_FIVE],
                [KC.KEYPAD_SIX],
                [KC.KEYPAD_ONE],
                [KC.KEYPAD_TWO],
                [KC.KEYPAD_THREE],
                [KC.KEYPAD_ZERO],
                [KC.KEYPAD_PERIOD],
                [KC.KEYPAD_ENTER],
            ],
        )


class Phonepad(KeyBoardApp):
    def __init__(self) -> None:
        super().__init__(
            name="Phone Pad",
            keyOrder=[
                [KC.ONE],
                [KC.TWO],
                [KC.THREE],
                [KC.FOUR],
                [KC.FIVE],
                [KC.SIX],
                [KC.SEVEN],
                [KC.EIGHT],
                [KC.NINE],
                [KC.KEYPAD_ASTERISK],
                [KC.ZERO],
                [KC.POUND],
            ],
        )


wasd = KeyBoardApp


kcLabel = {
    KC.A: """A""",
    KC.B: """B""",
    KC.C: """C""",
    KC.D: """D""",
    KC.E: """E""",
    KC.F: """F""",
    KC.G: """G""",
    KC.H: """H""",
    KC.I: """I""",
    KC.J: """J""",
    KC.K: """K""",
    KC.L: """L""",
    KC.M: """M""",
    KC.N: """N""",
    KC.O: """O""",
    KC.P: """P""",
    KC.Q: """Q""",
    KC.R: """R""",
    KC.S: """S""",
    KC.T: """T""",
    KC.U: """U""",
    KC.V: """V""",
    KC.W: """W""",
    KC.X: """X""",
    KC.Y: """Y""",
    KC.Z: """Z""",
    #
    KC.ONE: """1""",
    KC.TWO: """2""",
    KC.THREE: """3""",
    KC.FOUR: """4""",
    KC.FIVE: """5""",
    KC.SIX: """6""",
    KC.SEVEN: """7""",
    KC.EIGHT: """8""",
    KC.NINE: """9""",
    KC.ZERO: """0""",
    KC.ENTER: """Return""",
    KC.RETURN: """Return""",
    KC.ESCAPE: """Esc""",
    KC.BACKSPACE: """Backspace""",
    KC.TAB: """Tab""",
    KC.SPACEBAR: """Space""",
    KC.SPACE: """Space""",
    KC.MINUS: """-`""",
    KC.EQUALS: """=`""",
    KC.LEFT_BRACKET: """[""",
    KC.RIGHT_BRACKET: """]""",
    KC.BACKSLASH: r"""""",
    KC.POUND: """#""",
    KC.SEMICOLON: """;""",
    KC.QUOTE: """'""",
    KC.GRAVE_ACCENT: r"""`""",
    KC.COMMA: """,""",
    KC.PERIOD: """.""",
    KC.FORWARD_SLASH: """/""",
    #
    KC.CAPS_LOCK: """Caps Lock""",
    #
    KC.F1: """F1""",
    KC.F2: """F2""",
    KC.F3: """F3""",
    KC.F4: """F4""",
    KC.F5: """F5""",
    KC.F6: """F6""",
    KC.F7: """F7""",
    KC.F8: """F8""",
    KC.F9: """F9""",
    KC.F10: """F10""",
    KC.F11: """F11""",
    KC.F12: """F12""",
    #
    KC.PRINT_SCREEN: """Print Screen""",
    KC.SCROLL_LOCK: """Scroll Lock""",
    KC.PAUSE: """Pause""",
    #
    KC.INSERT: """Insert""",
    KC.HOME: """Home""",
    KC.PAGE_UP: """Page Up""",
    KC.DELETE: """Delete""",
    KC.END: """End""",
    KC.PAGE_DOWN: """Page Down""",
    #
    KC.RIGHT_ARROW: """Right""",
    KC.LEFT_ARROW: """Left""",
    KC.DOWN_ARROW: """Down""",
    KC.UP_ARROW: """Up""",
    #
    KC.KEYPAD_NUMLOCK: """Clear""",
    KC.KEYPAD_FORWARD_SLASH: """/""",
    KC.KEYPAD_ASTERISK: """*""",
    KC.KEYPAD_MINUS: """-""",
    KC.KEYPAD_PLUS: """+""",
    KC.KEYPAD_ENTER: """Enter""",
    KC.KEYPAD_ONE: """1""",
    KC.KEYPAD_TWO: """2""",
    KC.KEYPAD_THREE: """3""",
    KC.KEYPAD_FOUR: """4""",
    KC.KEYPAD_FIVE: """5""",
    KC.KEYPAD_SIX: """6""",
    KC.KEYPAD_SEVEN: """7""",
    KC.KEYPAD_EIGHT: """8""",
    KC.KEYPAD_NINE: """9""",
    KC.KEYPAD_ZERO: """0""",
    KC.KEYPAD_PERIOD: """.""",
    KC.KEYPAD_BACKSLASH: """\\""",
    KC.KEYPAD_EQUALS: """=""",
    #
    KC.APPLICATION: """Menu""",
    KC.POWER: """Power""",
    KC.F13: """F13""",
    KC.F14: """F14""",
    KC.F15: """F15""",
    KC.F16: """F16""",
    KC.F17: """F17""",
    KC.F18: """F18""",
    KC.F19: """F19""",
    #
    KC.F20: """F20""",
    KC.F21: """F21""",
    KC.F22: """F22""",
    KC.F23: """F23""",
    KC.F24: """F24""",
    #
    KC.LEFT_CONTROL: """CTRL""",
    KC.CONTROL: """CTRL""",
    KC.LEFT_SHIFT: """SHIFT""",
    KC.SHIFT: """SHIFT""",
    KC.LEFT_ALT: """ALT""",
    KC.ALT: """ALT""",
    KC.OPTION: """OPTION""",
    KC.LEFT_GUI: """GUI""",
    KC.GUI: """GUI""",
    KC.WINDOWS: """WINDOWS""",
    KC.COMMAND: """CMD""",
    KC.RIGHT_CONTROL: """R CTRL""",
    KC.RIGHT_SHIFT: """R SHIFT""",
    KC.RIGHT_ALT: """R ALT""",
    KC.RIGHT_GUI: """R GUI""",
}


class pix:
    control = 0x00FF88
    delete = 0xFF0000
    fn = 0x88FF88
    knumber = 0x8888FF
    letter = 0xFFFFFF
    wasd = 0xFF4400
    math = 0x8800FF
    meta = 0x0000FF
    move = 0x00FF00
    number = 0xFFFF00
    punct = 0x00FFFF
    space = 0xFF00FF


kcPixel = {
    KC.A: pix.wasd,
    KC.B: pix.letter,
    KC.C: pix.letter,
    KC.D: pix.wasd,
    KC.E: pix.letter,
    KC.F: pix.letter,
    KC.G: pix.letter,
    KC.H: pix.letter,
    KC.I: pix.letter,
    KC.J: pix.letter,
    KC.K: pix.letter,
    KC.L: pix.letter,
    KC.M: pix.letter,
    KC.N: pix.letter,
    KC.O: pix.letter,
    KC.P: pix.letter,
    KC.Q: pix.letter,
    KC.R: pix.letter,
    KC.S: pix.wasd,
    KC.T: pix.letter,
    KC.U: pix.letter,
    KC.V: pix.letter,
    KC.W: pix.wasd,
    KC.X: pix.letter,
    KC.Y: pix.letter,
    KC.Z: pix.letter,
    #
    KC.ONE: pix.number,
    KC.TWO: pix.number,
    KC.THREE: pix.number,
    KC.FOUR: pix.number,
    KC.FIVE: pix.number,
    KC.SIX: pix.number,
    KC.SEVEN: pix.number,
    KC.EIGHT: pix.number,
    KC.NINE: pix.number,
    KC.ZERO: pix.number,
    KC.ENTER: pix.control,
    KC.RETURN: pix.control,
    KC.ESCAPE: pix.delete,
    KC.BACKSPACE: pix.delete,
    KC.TAB: pix.space,
    KC.SPACEBAR: pix.space,
    KC.SPACE: pix.space,
    KC.MINUS: pix.punct,
    KC.EQUALS: pix.punct,
    KC.LEFT_BRACKET: pix.punct,
    KC.RIGHT_BRACKET: pix.punct,
    KC.BACKSLASH: pix.punct,
    KC.POUND: pix.punct,
    KC.SEMICOLON: pix.punct,
    KC.QUOTE: pix.punct,
    KC.GRAVE_ACCENT: pix.punct,
    KC.COMMA: pix.punct,
    KC.PERIOD: pix.punct,
    KC.FORWARD_SLASH: pix.punct,
    #
    KC.CAPS_LOCK: pix.control,
    #
    KC.F1: pix.fn,
    KC.F2: pix.fn,
    KC.F3: pix.fn,
    KC.F4: pix.fn,
    KC.F5: pix.fn,
    KC.F6: pix.fn,
    KC.F7: pix.fn,
    KC.F8: pix.fn,
    KC.F9: pix.fn,
    KC.F10: pix.fn,
    KC.F11: pix.fn,
    KC.F12: pix.fn,
    #
    KC.PRINT_SCREEN: pix.control,
    KC.SCROLL_LOCK: pix.control,
    KC.PAUSE: pix.control,
    #
    KC.INSERT: pix.control,
    KC.HOME: pix.move,
    KC.PAGE_UP: pix.move,
    KC.DELETE: pix.delete,
    KC.END: pix.move,
    KC.PAGE_DOWN: pix.move,
    #
    KC.RIGHT_ARROW: pix.move,
    KC.LEFT_ARROW: pix.move,
    KC.DOWN_ARROW: pix.move,
    KC.UP_ARROW: pix.move,
    #
    KC.KEYPAD_NUMLOCK: pix.math,
    KC.KEYPAD_FORWARD_SLASH: pix.math,
    KC.KEYPAD_ASTERISK: pix.math,
    KC.KEYPAD_MINUS: pix.math,
    KC.KEYPAD_PLUS: pix.math,
    KC.KEYPAD_ENTER: pix.control,
    KC.KEYPAD_ONE: pix.knumber,
    KC.KEYPAD_TWO: pix.knumber,
    KC.KEYPAD_THREE: pix.knumber,
    KC.KEYPAD_FOUR: pix.knumber,
    KC.KEYPAD_FIVE: pix.knumber,
    KC.KEYPAD_SIX: pix.knumber,
    KC.KEYPAD_SEVEN: pix.knumber,
    KC.KEYPAD_EIGHT: pix.knumber,
    KC.KEYPAD_NINE: pix.knumber,
    KC.KEYPAD_ZERO: pix.knumber,
    KC.KEYPAD_PERIOD: pix.math,
    KC.KEYPAD_BACKSLASH: pix.math,
    KC.KEYPAD_EQUALS: pix.math,
    #
    KC.APPLICATION: pix.meta,
    KC.POWER: pix.meta,
    KC.F13: pix.fn,
    KC.F14: pix.fn,
    KC.F15: pix.fn,
    KC.F16: pix.fn,
    KC.F17: pix.fn,
    KC.F18: pix.fn,
    KC.F19: pix.fn,
    #
    KC.F20: pix.fn,
    KC.F21: pix.fn,
    KC.F22: pix.fn,
    KC.F23: pix.fn,
    KC.F24: pix.fn,
    #
    KC.LEFT_CONTROL: pix.meta,
    KC.CONTROL: pix.meta,
    KC.LEFT_SHIFT: pix.meta,
    KC.SHIFT: pix.meta,
    KC.LEFT_ALT: pix.meta,
    KC.ALT: pix.meta,
    KC.OPTION: pix.meta,
    KC.LEFT_GUI: pix.meta,
    KC.GUI: pix.meta,
    KC.WINDOWS: pix.meta,
    KC.COMMAND: pix.meta,
    KC.RIGHT_CONTROL: pix.meta,
    KC.RIGHT_SHIFT: pix.meta,
    KC.RIGHT_ALT: pix.meta,
    KC.RIGHT_GUI: pix.meta,
}
