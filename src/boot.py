"""CircuitPython Essentials Storage logging boot.py file"""

from time import sleep

import usb_cdc
import storage

import adafruit_macropad

macropad = adafruit_macropad.MacroPad()


def get_pressed_keys():
    held = []
    while macropad.keys.events:
        key_event = macropad.keys.events.get()
        kpn = key_event.key_number
        if key_event.pressed:
            print(">> ", kpn)
            held.append(kpn)
    return held


def held_keys_actions(held):
    ret = {}
    try:
        if 3 in held:
            print("DiskMode")
            # storage.remount("/", readonly=False)
        else:
            print("ReadOnly")
            usb_cdc.enable(console=True, data=False)
            storage.disable_usb_drive()

        sleep(2)
    except Exception as e:
        print(e)
        sleep(2)


print("Booting in")
held = set()
for i in reversed(range(3)):
    print(" ", i, end="")
    held.update(get_pressed_keys())
    sleep(1)
print()
held_keys_actions(list(held))
