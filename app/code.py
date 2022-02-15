import time

from views.ExtendedMacropad import ExtendedMacropad

myHardwareController = ExtendedMacropad()


def transpose(lol):
    return list(zip(*lol))
    
def rotate(lol):
    tmp = transpose(lol)
    return list(reversed(tmp))

class BaseModel:

    counter = 0

    def updateCounter(self, value):
        self.counter += value


class TTTBoard:

    def reset(self):
        self.grid = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.players = ["X", "O"]
        self.currentPlayer = 0
        self.turns = 0
        self.winner = None

    def incrementPlayer(self):
        self.currentPlayer += 1
        if len(self.players) <= self.currentPlayer:
            self.currentPlayer = self.currentPlayer % len(self.players)

    def play(self, x, y):
        if self.grid[x][y] == "":
            self.grid[x][y] = self.players[self.currentPlayer]
            self.incrementPlayer()
            self.turns += 1
            self.declareWinner()
            return True
        else:
            return False

    def declareWinner(self):
        for g in (self.grid, rotate(self.grid)):
            for row in g:
                if row[0] in self.players:
                    if row[0] == row[1] and row[0] == row[2]:
                        self.winner = row[0]
                        
            if g[0][0] in self.players:
                if g[0][0] == g[1][1] and g[0][0] == g[2][2]:
                    self.winner = g[0][0]
        
        if 9 <= self.turns:
            self.winner = 'No One'
            
        return self.winner


class TTTController:

    macropad = myHardwareController
    game = TTTBoard()

    def play(self):
        waitingForLegalMove = True
        while waitingForLegalMove:
            pressedNumber = self.waitForKeyPress()
            x = int(pressedNumber / 3)
            y = pressedNumber % 3
            if self.game.play(x, y):
                waitingForLegalMove = False

    def waitForKeyPress(self):
        playedKey = None
        self.macropad.update()
        # waiting for a keypress to register as a play
        while not self.macropad.pressedKeys:
            time.sleep(0.001)
            self.macropad.update()
        playedKey = self.macropad.pressedKeys[0]
        # waiting for all keys to be released, they are not allowed as plays
        while self.macropad.pressedKeys:
            time.sleep(0.001)
            self.macropad.update()
        return playedKey

    def displayBoard(self):
        print("\n" * 4)
        print(self.game.grid)
        
        # pixelBoard
        lc = 0
        for row in self.game.grid:
            for e in row:
                color = 0x002200
                if e == 'X':
                    color = 0xff0000
                if e == 'O':
                    color = 0x0000ff
                self.macropad.pixels[lc] = color
                lc += 1
        
        color = 0x040404
        if self.game.winner == 'X':
            color = 0xff0000
        if self.game.winner == 'O':
            color = 0x0000ff
        for i in (9, 10, 11):
            self.macropad.pixels[i] = color
        

    def loop(self):
        while True:
            self.game.reset()
            self.displayBoard()
            while not self.game.declareWinner():
                self.play()
                self.displayBoard()
            print(f"'{self.game.declareWinner()}' is the winner!\nGame Over!")
            self.waitForKeyPress()


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


if __name__ == '__main__':
    main()
