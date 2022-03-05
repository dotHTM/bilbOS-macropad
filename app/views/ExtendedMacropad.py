import adafruit_macropad


class ExtendedMacropad(adafruit_macropad.MacroPad):

    encoder_delta = 0
    encoder_direction = 0

    _old_encoder = 0

    pressedKeys = []
    newPressedKeys = []
    newReleasedKeys = []

    def __init__(
        self,
        rotation=0,
        midi_in_channel=1,
        midi_out_channel=1,
    ):
        super().__init__(rotation, midi_in_channel, midi_out_channel)

    def pixelColor(self, index, newColor):
        if self.pixels != None and 0 <= index and index < len(self.pixels):
            self.pixels[index] = newColor

    def update(self):
        self.encoder_switch_debounced.update()
        self.encoder_pressed = self.encoder_switch_debounced.pressed
        self.encoder_released = self.encoder_switch_debounced.released

        self.encoder_delta = self.encoder - self._old_encoder
        if self.encoder_delta == 0:
            self.encoder_direction = 0
        else:
            self.encoder_direction = 1 if 0 < self.encoder_delta else -1
        self._old_encoder = self.encoder

        self.newPressedKeys = []
        self.newReleasedKeys = []

        while self.keys.events:
            key_event = self.keys.events.get()
            if key_event.pressed:
                self.newPressedKeys.append(key_event.key_number)
                self.pressedKeys.append(key_event.key_number)
            elif key_event.released:
                self.newReleasedKeys.append(key_event.key_number)
                while key_event.key_number in self.pressedKeys:
                    self.pressedKeys.remove(key_event.key_number)
