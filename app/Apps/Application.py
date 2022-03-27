class Application:
    def __init__(self) -> None:
        # super(Application, self).__init__()

        self.name = "Application"

        self.displayType = None

        self._FocusFunc = None
        self._FocusLostFunc = None

        self._EncoderClockwise = None
        self._EncoderCounterClockwise = None
        self._EncoderPress = None
        self._EncoderRelease = None

        self.canvas = [0 for _ in range(12)]

        self._Buttons = [
            [None, None],
            [None, None],
            [None, None],
            [None, None],
            [None, None],
            [None, None],
            [None, None],
            [None, None],
            [None, None],
            [None, None],
            [None, None],
            [None, None],
        ]

    def onFocus(self, func):
        if callable(func):
            self._FocusFunc = func
        else:
            self._FocusFunc = None

    def onFocusLost(self, func):
        if callable(func):
            self._FocusLostFunc = func
        else:
            self._FocusLostFunc = None

    def onEncoderPress(self, func):
        if callable(func):
            self._EncoderPress = func
        else:
            self._EncoderPress = None

    def onEncoderRelease(self, func):
        if callable(func):
            self._EncoderRelease = func
        else:
            self._EncoderRelease = None

    def onEncoderClockwise(self, func):
        if callable(func):
            self._EncoderClockwise = func
        else:
            self._EncoderClockwise = None

    def onEncoderCounterClockwise(self, func):
        if callable(func):
            self._EncoderCounterClockwise = func
        else:
            self._EncoderCounterClockwise = None

    @property
    def encoderSwitchActions(self):
        return [self._EncoderPress, self._EncoderRelease]

    @property
    def encoderRotateActions(self):
        return {
            -1: self._EncoderCounterClockwise,
            1: self._EncoderClockwise,
        }

    @property
    def pressedActions(self):
        return [b[0] for b in self._Buttons]

    @property
    def releasedActions(self):
        return [b[1] for b in self._Buttons]

    def onButtonPress(self, i, func):
        if 0 <= i < len(self._Buttons):
            if callable(func):
                self._Buttons[i][0] = func
            else:
                self._Buttons[i][0] = None

    def onButtonRelease(self, i, func):
        if 0 <= i < len(self._Buttons):
            if callable(func):
                self._Buttons[i][1] = func
            else:
                self._Buttons[i][1] = None

    def update(self):
        pass

    def displayUpdate(self):
        return
