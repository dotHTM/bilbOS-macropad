import time

from views.ExtendedMacropad import ExtendedMacropad

myHardwareController = ExtendedMacropad()


def transpose(lol: list[list[T]]) -> list[list[T]]:
    return [list(r) for r in zip(*lol)]


def rotate(lol: list[list[T]]) -> list[list[T]]:
    return list(reversed(transpose(lol)))


class BaseModel:
    counter = 0

    def updateCounter(self, value):
        self.counter += value


class TTTBoard:
    history = []

    @property
    def lastPlay(self):
        if 0 < len(self.history):
            return self.history[-1]
        return None

    def reset(self, undo=False):
        self.grid: list[list[str]] = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.players: list[str] = ["X", "O"]
        self.currentPlayer: int = 0
        self.turns: int = 0
        self.winner = None
        self.action: str = ""
        if not undo:
            self.history = []
        else:
            if 0 < len(self.history):
                self.history.pop()
                oldHist = self.history
                self.history = []
                for play in oldHist:
                    self.play(*play)

    def incrementPlayer(self):
        self.currentPlayer += 1
        if len(self.players) <= self.currentPlayer:
            self.currentPlayer = self.currentPlayer % len(self.players)

    def play(self, x: int, y: int) -> bool:
        if self.grid[x][y] == "":
            self.history.append([x, y])
            self.grid[x][y] = self.players[self.currentPlayer]
            self.incrementPlayer()
            self.turns += 1
            self.checkForWinner()
            print(self.history)
            return True
        else:
            return False

    def checkForWinner(self):
        for g in (self.grid, rotate(self.grid)):
            for row in g:
                if row[0] in self.players:
                    if row[0] == row[1] and row[0] == row[2]:
                        self.winner = row[0]
            if g[0][0] in self.players:
                if g[0][0] == g[1][1] and g[0][0] == g[2][2]:
                    self.winner = g[0][0]
        if 9 <= self.turns and self.winner == None:
            self.winner = "No One"
        return self.winner


class TTTController:

    macropad = myHardwareController
    game = TTTBoard()
    playerColors = {
        "": {
            "board": 0x000800,
        },
        "X": {
            "board": 0xFF0000,
            "active": 0x880000,
            "inactive": 0x882222,
            "winner": 0xFF2222,
            "lastPlay": 0xFF2200,
        },
        "O": {
            "board": 0x0000FF,
            "active": 0x000088,
            "inactive": 0x222288,
            "winner": 0x2222FF,
            "lastPlay": 0x0044FF,
        },
        "Shared": {
            "winner": 0x444444,
        },
        "No One": {
            "winner": 0x000000,
        },
    }

    def play(self):
        while True:
            pressedNumber = self.waitForKeyPress()
            if pressedNumber == 9:
                if "O" == self.game.players[self.game.currentPlayer]:
                    self.game.winner = "X"
                    self.game.action = "O resigned"
                    return
            elif pressedNumber == 10:
                self.game.winner = "Shared"
                self.game.action = "Draw"
                return
            elif pressedNumber == 11:
                if "X" == self.game.players[self.game.currentPlayer]:
                    self.game.winner = "O"
                    self.game.action = "X resigned"
                    return
            elif pressedNumber == 12:
                pass
            elif pressedNumber == 13:
                pass
            elif pressedNumber == 14:
                self.game.reset(undo=True)
                self.displayBoard()
                return
            else:
                x = int(pressedNumber / 3)
                y = pressedNumber % 3
                if self.game.play(x, y):
                    return

    def waitForKeyPress(self, acceptable=None):
        playedKey = None
        while playedKey == None:
            # waiting for a keypress to register as a play
            time.sleep(0.001)
            self.macropad.update()

            if self.macropad.encoder:
                playedKey = 12
            if self.macropad.encoder_direction == 1:
                playedKey = 13
            if self.macropad.encoder_direction == -1:
                playedKey = 14

            while self.macropad.pressedKeys:
                time.sleep(0.001)
                self.macropad.update()
                if len(self.macropad.pressedKeys) == 1:
                    playedKey = self.macropad.pressedKeys[0]
                    # print(playedKey)
            if not (acceptable == None or playedKey in acceptable):
                playedKey = None
        # waiting for all keys to be released, they are not allowed as plays
        while self.macropad.pressedKeys:
            time.sleep(0.001)
            self.macropad.update()
        return playedKey

    def displayBoard(self):
        print("\n" * 4)
        # print(self.game.grid)

        # pixelBoard
        lc = 0
        for row in self.game.grid:
            for e in row:
                self.macropad.pixelColor(lc, self.playerColors[e]["board"])
                lc += 1

        if self.game.winner != None:
            for i in (9, 10, 11):
                self.macropad.pixelColor(
                    i, self.playerColors[self.game.winner]["winner"]
                )
        else:
            boardColor = {10: 0x222222}

            for s in [9, "X"], [11, "O"]:
                boardColor[s[0]] = self.playerColors[s[1]]["inactive"]
                if s[1] == self.game.players[self.game.currentPlayer]:
                    print(s[1])
                    boardColor[s[0]] = self.playerColors[s[1]]["active"]

            for k in boardColor:
                self.macropad.pixelColor(k, boardColor[k])

        if self.game.lastPlay != None:
            (x, y) = self.game.lastPlay
            index = x * 3 + y
            self.macropad.pixelColor(
                index, self.playerColors[self.game.grid[x][y]]["lastPlay"]
            )

    def loop(self):
        while True:
            self.game.reset()
            self.displayBoard()
            while not self.game.checkForWinner():
                self.play()
                self.displayBoard()
            print(
                f"\n\n\n\nThe winner is\n    {self.game.checkForWinner()}.\n{ self.game.action }"
            )
            self.waitForKeyPress([9, 10, 11])


class BaseController:

    model = BaseModel()
    macropad = myHardwareController

    def loop(self):
        while True:
            time.sleep(0.001)

            self.macropad.update()
            if self.macropad.encoder_pressed:
                print("pressed")
            if self.macropad.encoder_released:
                print("released")

            if self.macropad.encoder_direction != 0:
                self.model.updateCounter(self.macropad.encoder_delta)
                print(
                    f"c{self.model.counter} d{self.macropad.encoder_delta} r{self.macropad.encoder} f{ self.macropad.encoder - self.model.counter}"
                )

            while self.macropad.keys.events:
                key_event = self.macropad.keys.events.get()
                if key_event != None:
                    print(key_event.key_number)


def main():
    entry = TTTController()
    entry.loop()


if __name__ == "__main__":
    main()
