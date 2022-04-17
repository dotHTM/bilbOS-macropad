from time import sleep

from Apps.Application import Application
from utils import debugMessage
from utils import rotate, transpose
from Views.DisplayGrid import Grid12


class Board:
    def __init__(self) -> None:
        self.reset()
        self.history = []
        self.future = []

    @property
    def lastPlay(self):
        if 0 < len(self.history):
            return self.history[-1]
        return None

    def reset(self):
        self.grid: list[list[str]] = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],
        ]
        self.players: list[str] = ["X", "O"]
        self.currentPlayer: int = 0
        self.turns: int = 0
        self.winner = None
        self.winningTriple = None
        self.action: str = ""
        self.history = []

    def resetFuture(self):
        self.future = []

    def undo(self):
        if 0 < len(self.history):
            self.future.append(self.history.pop())
            oldHist = self.history
            self.reset()
            for play in oldHist:
                self.play(*play, retainFuture=True)

    def redo(self):
        if 0 < len(self.future):
            self.play(*self.future.pop(), retainFuture=True)

    def incrementPlayer(self):
        self.currentPlayer += 1
        if len(self.players) <= self.currentPlayer:
            self.currentPlayer = self.currentPlayer % len(self.players)

    def play(self, x: int, y: int, retainFuture=False) -> bool:
        if self.winner == None:
            if self.grid[x][y] == "":
                self.history.append([x, y])
                self.grid[x][y] = self.players[self.currentPlayer]
                self.incrementPlayer()
                self.turns += 1
                self.hasWinner
                if not retainFuture:
                    self.resetFuture()
                return True
        return False

    @property
    def hasWinner(self):

        for t, g in enumerate([self.grid, transpose(self.grid)]):
            for r, row in enumerate(g):
                if row[0] in self.players:
                    if row[0] == row[1] and row[0] == row[2]:
                        self.winner = row[0]
                        if t == 0:
                            self.winningTriple = ((r, 0), (r, 1), (r, 2))
                        else:
                            self.winningTriple = ((0, r), (1, r), (2, r))

        for r, g in enumerate([self.grid, rotate(self.grid)]):
            if g[0][0] in self.players:
                if g[0][0] == g[1][1] and g[0][0] == g[2][2]:
                    self.winner = g[0][0]
                    if r == 0:
                        self.winningTriple = ((0, 0), (1, 1), (2, 2))
                    else:
                        self.winningTriple = ((0, 2), (1, 1), (2, 0))

        if 9 <= self.turns and self.winner == None:
            self.winner = "No One"

        return self.winner

    def declareWinner(self, winner, action):
        if self.winner == None:
            self.winner = winner
            self.action = action

    @property
    def currentPlayerName(self):
        return self.players[self.currentPlayer]


class TicTacToe(Application):
    def __init__(self) -> None:
        super(TicTacToe, self).__init__()
        self.name = "TicTacToe"

        self.game = Board()
        self.displayType = Grid12

        def updateScreen():
            print("\n" * 4)
            if self.game.winner:
                print(f"{self.game.winner} won\n{self.game.action}")
            else:
                print(self.game.currentPlayerName)

        self.onFocus(updateScreen)

        def playButton(i):
            x = int(i / 3)
            y = i % 3

            def inner():
                self.game.play(x, y)
                updateScreen()

            return inner

        def resignButton(i):
            winner = None
            action = None

            if i == 9:
                winner = "O"
                action = "X resigned"
            elif i == 10:
                winner = "Shared"
                action = "Draw"
            elif i == 11:
                winner = "X"
                action = "O resigned"

            def inner():
                if self.game.hasWinner:
                    self.game.reset()
                else:
                    self.game.declareWinner(winner=winner, action=action)
                updateScreen()

            return inner

        for i in range(9):
            self.onButtonPress(i, playButton(i))

        for i in range(9, 12):
            self.onButtonPress(i, resignButton(i))

        def undo():
            self.game.undo()
            updateScreen()

        def redo():
            self.game.redo()
            updateScreen()

        self.onEncoderCounterClockwise(undo)
        self.onEncoderClockwise(redo)

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

    def update(self):

        debugMessage(f"{self.game.history=}")
        debugMessage(f"{self.game.future=}")

        debugMessage(self.game.grid)

        # pixelBoard
        lc = 0
        for row in self.game.grid:
            for e in row:
                self.canvas[lc] = self.playerColors[e]["board"]
                lc += 1

        boardColor = {10: 0x222222}
        for s in [9, "X"], [11, "O"]:
            boardColor[s[0]] = self.playerColors[s[1]]["inactive"]
            if s[1] == self.game.currentPlayerName:

                boardColor[s[0]] = self.playerColors[s[1]]["active"]

        for k in boardColor:
            self.canvas[k] = boardColor[k]

        if self.game.lastPlay != None:
            (x, y) = self.game.lastPlay
            index = x * 3 + y
            self.canvas[index] = self.playerColors[self.game.grid[x][y]]["lastPlay"]

    def displayUpdate(self):

        labels = []

        noOneGrid = [
            ["No", "One", "Wins!"],
            ["", "", ""],
            ["", "SHAME!", ""],
        ]

        sharedGrid = [
            ["Shared", "Win", ": D"],
            ["", "", ""],
            ["1/2", "Point", "Each"],
        ]

        resignedGrid = [
            ["", "", ""],
            [self.game.winner, "has", "won"],
            ["", "", ""],
        ]

        for i, row in enumerate(self.game.grid):
            for j, e in enumerate(row):
                if self.game.winner == "No One":
                    labels.append(noOneGrid[i][j])
                elif self.game.winner == "Shared":
                    labels.append(sharedGrid[i][j])
                elif self.game.winner:
                    if self.game.winningTriple:
                        if (i, j) in self.game.winningTriple:
                            labels.append(e)
                        else:
                            labels.append("")
                    else:
                        labels.append(resignedGrid[i][j])
                else:
                    labels.append(e)

        labels.extend(["Rsgn X", "Draw", "Rsgn O"])

        return {
            "title": self.name,
            "labels": labels,
        }
