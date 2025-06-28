# from typing import Callable, Optional, Union
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
# from adafruit_hid.consumer_control import ConsumerControl
# from adafruit_hid.consumer_control_code import ConsumerControlCode


def makeKeyboardPress(keyboard: Keyboard, kcList: list[Keycode]) -> Callable[[], None]:
    def inner():
        for kc in kcList:
            keyboard.press(kc)

    return inner


def makeKeyboardRelease(
    keyboard: Keyboard, kcList: list[Keycode]
) -> Callable[[], None]:
    def inner():
        for kc in reversed(kcList):
            keyboard.release(kc)

    return inner


class Button:
    """Button Object, stores onPress, onRelease, and color for both states"""

    count = 0

    def __init__(
        self,
        name: str = "unk",
        keyboard: Optional[Keyboard] = None,
        keycode: Union[Keycode, list[Keycode], None] = None,
        pressFunc: Optional[Callable[[], None]] = None,
        releaseFunc: Optional[Callable[[], None]] = None,
        colorReleased=0x0,
        colorPressed=0xFFFFFF,
    ):
        super(Button, self).__init__()

        self.name = name
        self.colorPressed = colorPressed
        self.colorReleased = colorReleased
        self.pressFunc = pressFunc
        self.releaseFunc = releaseFunc
        self.countID = Button.count
        Button.count += 1

        if keycode and keyboard:
            if isinstance(keycode, Keycode):
                keycode = [keycode]

            if isinstance(keycode, list):
                self.pressFunc = makeKeyboardPress(keyboard, keycode)
                self.releaseFunc = makeKeyboardRelease(keyboard, keycode)

    def __repr__(self) -> str:
        return f"<Button({self.countID}, {self.name} ...)>"

    def __str__(self) -> str:
        return self.name
