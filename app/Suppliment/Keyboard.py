import re

from adafruit_hid.keycode import Keycode as kc


class KeyData:
    @staticmethod
    def normalizeName(name: str) -> str:
        res = name
        res = res.upper()
        res = re.sub(r"_", r" ", res)
        return res

    @staticmethod
    def byName(name: str):
        testName = KeyData.normalizeName(name)
        if testName in KeyData._byName:
            return KeyData._byName[testName]
        return None

    _byName = {}

    def __init__(self, keycode, name: str) -> None:
        self.keycode = keycode
        self.name = KeyData.normalizeName(name)
        KeyData._byName[self.name] = self


def loadUSKeyCodes():

    KeyData(kc.A, "a")
    KeyData(kc.B, "b")
    KeyData(kc.C, "c")
    KeyData(kc.D, "d")
    KeyData(kc.E, "e")
    KeyData(kc.F, "f")
    KeyData(kc.G, "g")
    KeyData(kc.H, "h")
    KeyData(kc.I, "i")
    KeyData(kc.J, "j")
    KeyData(kc.K, "k")
    KeyData(kc.L, "l")
    KeyData(kc.M, "m")
    KeyData(kc.N, "n")
    KeyData(kc.O, "o")
    KeyData(kc.P, "p")
    KeyData(kc.Q, "q")
    KeyData(kc.R, "r")
    KeyData(kc.S, "s")
    KeyData(kc.T, "t")
    KeyData(kc.U, "u")
    KeyData(kc.V, "v")
    KeyData(kc.W, "w")
    KeyData(kc.X, "x")
    KeyData(kc.Y, "y")
    KeyData(kc.Z, "z")

    KeyData(kc.ONE, "1")
    KeyData(kc.TWO, "2")
    KeyData(kc.THREE, "3")
    KeyData(kc.FOUR, "4")
    KeyData(kc.FIVE, "5")
    KeyData(kc.SIX, "6")
    KeyData(kc.SEVEN, "7")
    KeyData(kc.EIGHT, "8")
    KeyData(kc.NINE, "9")
    KeyData(kc.ZERO, "0")

    KeyData(kc.ENTER, "Return")
    KeyData(kc.ESCAPE, "Escape")
    KeyData(kc.BACKSPACE, "Backspace")
    KeyData(kc.TAB, "Tab")
    KeyData(kc.SPACEBAR, "Spacebar")

    KeyData(kc.MINUS, "-")
    KeyData(kc.EQUALS, "=")
    KeyData(kc.LEFT_BRACKET, "[")
    KeyData(kc.RIGHT_BRACKET, "]")
    KeyData(kc.BACKSLASH, "\\")
    KeyData(kc.POUND, "#")
    KeyData(kc.SEMICOLON, ";")
    KeyData(kc.QUOTE, "'")
    KeyData(kc.GRAVE_ACCENT, "`")
    KeyData(kc.COMMA, ",")
    KeyData(kc.PERIOD, ".")
    KeyData(kc.FORWARD_SLASH, "/")

    KeyData(kc.CAPS_LOCK, "Caps Lock")

    KeyData(kc.F1, "F1")
    KeyData(kc.F2, "F2")
    KeyData(kc.F3, "F3")
    KeyData(kc.F4, "F4")
    KeyData(kc.F5, "F5")
    KeyData(kc.F6, "F6")
    KeyData(kc.F7, "F7")
    KeyData(kc.F8, "F8")
    KeyData(kc.F9, "F9")
    KeyData(kc.F10, "F10")
    KeyData(kc.F11, "F11")
    KeyData(kc.F12, "F12")

    KeyData(kc.PRINT_SCREEN, "Print Screen")
    KeyData(kc.SCROLL_LOCK, "Scroll Lock")

    KeyData(kc.PAUSE, "Pause")
    KeyData(kc.INSERT, "Insert")
    KeyData(kc.HOME, "Home")
    KeyData(kc.PAGE_UP, "Page up")
    KeyData(kc.DELETE, "Delete forward")
    KeyData(kc.END, "End")
    KeyData(kc.PAGE_DOWN, "Page down")
    KeyData(kc.RIGHT_ARROW, "right")
    KeyData(kc.LEFT_ARROW, "left")
    KeyData(kc.DOWN_ARROW, "down")
    KeyData(kc.UP_ARROW, "up")

    KeyData(kc.KEYPAD_NUMLOCK, "Clear")
    KeyData(kc.KEYPAD_FORWARD_SLASH, "Keypad /")
    KeyData(kc.KEYPAD_ASTERISK, "Keypad *")
    KeyData(kc.KEYPAD_MINUS, "Keyapd -")
    KeyData(kc.KEYPAD_PLUS, "Keypad +")
    KeyData(kc.KEYPAD_ENTER, "Keypad Enter")
    KeyData(kc.KEYPAD_ONE, "Keypad 1")
    KeyData(kc.KEYPAD_TWO, "Keypad 2")
    KeyData(kc.KEYPAD_THREE, "Keypad 3")
    KeyData(kc.KEYPAD_FOUR, "Keypad 4")
    KeyData(kc.KEYPAD_FIVE, "Keypad 5")
    KeyData(kc.KEYPAD_SIX, "Keypad 6")
    KeyData(kc.KEYPAD_SEVEN, "Keypad 7")
    KeyData(kc.KEYPAD_EIGHT, "Keypad 8")
    KeyData(kc.KEYPAD_NINE, "Keypad 9")
    KeyData(kc.KEYPAD_ZERO, "Keypad 0")
    KeyData(kc.KEYPAD_PERIOD, "Keypad .")
    KeyData(kc.KEYPAD_BACKSLASH, "Keypad \\")

    KeyData(kc.APPLICATION, "Application")

    KeyData(kc.POWER, "Power")

    KeyData(kc.KEYPAD_EQUALS, "Keypad =")
    KeyData(kc.F13, "F13")
    KeyData(kc.F14, "F14")
    KeyData(kc.F15, "F15")
    KeyData(kc.F16, "F16")
    KeyData(kc.F17, "F17")
    KeyData(kc.F18, "F18")
    KeyData(kc.F19, "F19")
    KeyData(kc.F20, "F20")
    KeyData(kc.F21, "F21")
    KeyData(kc.F22, "F22")
    KeyData(kc.F23, "F23")
    KeyData(kc.F24, "F24")

    KeyData(kc.LEFT_CONTROL, "CONTROL")
    KeyData(kc.LEFT_CONTROL, "ctrl")
    KeyData(kc.LEFT_CONTROL, "^")
    KeyData(kc.LEFT_SHIFT, "SHIFT")
    KeyData(kc.LEFT_ALT, "ALT")
    KeyData(kc.LEFT_ALT, "option")
    KeyData(kc.LEFT_GUI, "GUI")
    KeyData(kc.LEFT_GUI, "super")

    KeyData(kc.LEFT_CONTROL, "LEFT_CONTROL")
    KeyData(kc.LEFT_SHIFT, "LEFT_SHIFT")
    KeyData(kc.LEFT_ALT, "LEFT_ALT")
    KeyData(kc.LEFT_GUI, "LEFT_GUI")

    KeyData(kc.RIGHT_CONTROL, "RIGHT_CONTROL")
    KeyData(kc.RIGHT_SHIFT, "RIGHT_SHIFT")
    KeyData(kc.RIGHT_ALT, "RIGHT_ALT")
    KeyData(kc.RIGHT_GUI, "RIGHT_GUI")


loadUSKeyCodes()
