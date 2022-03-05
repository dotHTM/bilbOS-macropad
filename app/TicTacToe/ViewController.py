# import time
# from utils import debugMessage
# from .Board import Board
# class TTTController:
#     def __init__(self, myHardwareController) -> None:
#         self.macropad = myHardwareController
#         self.game = Board()
#     playerColors = {
#         "": {
#             "board": 0x000800,
#         },
#         "X": {
#             "board": 0xFF0000,
#             "active": 0x880000,
#             "inactive": 0x882222,
#             "winner": 0xFF2222,
#             "lastPlay": 0xFF2200,
#         },
#         "O": {
#             "board": 0x0000FF,
#             "active": 0x000088,
#             "inactive": 0x222288,
#             "winner": 0x2222FF,
#             "lastPlay": 0x0044FF,
#         },
#         "Shared": {
#             "winner": 0x444444,
#         },
#         "No One": {
#             "winner": 0x000000,
#         },
#     }
#     def play(self):
#         while True:
#             pressedNumber = self.waitForKeyPress()
#             if pressedNumber == 9:
#                 if "O" == self.game.players[self.game.currentPlayer]:
#                     self.game.declareWinner("X", "O resigned")
#                     return
#             elif pressedNumber == 10:
#                 if self.game.winner == None:
#                     self.game.declareWinner("Shared", "Draw")
#                 else:
#                     self.game.reset()
#                 return
#             elif pressedNumber == 11:
#                 if "X" == self.game.players[self.game.currentPlayer]:
#                     self.game.declareWinner("O", "X resigned")
#                     return
#             elif pressedNumber == 12:
#                 pass
#             elif pressedNumber == 13:
#                 self.game.redo()
#                 return
#             elif pressedNumber == 14:
#                 self.game.undo()
#                 return
#             else:
#                 x = int(pressedNumber / 3)
#                 y = pressedNumber % 3
#                 if self.game.play(x, y):
#                     return
#     def waitForKeyPress(self, acceptable=None):
#         playedKey = None
#         while playedKey == None:
#             # waiting for a keypress to register as a play
#             time.sleep(0.001)
#             self.macropad.update()
#             if self.macropad.encoder:
#                 playedKey = 12
#             if self.macropad.encoder_direction == 1:
#                 playedKey = 13
#             if self.macropad.encoder_direction == -1:
#                 playedKey = 14
#             while self.macropad.pressedKeys:
#                 time.sleep(0.001)
#                 self.macropad.update()
#                 if len(self.macropad.pressedKeys) == 1:
#                     playedKey = self.macropad.pressedKeys[0]
#                     # print(playedKey)
#             if not (acceptable == None or playedKey in acceptable):
#                 playedKey = None
#         # waiting for all keys to be released, they are not allowed as plays
#         while self.macropad.pressedKeys:
#             time.sleep(0.001)
#             self.macropad.update()
#         return playedKey
#     def draw(self):
#         print("\n" * 4)
#         debugMessage(f"{self.game.history=}")
#         debugMessage(f"{self.game.future=}")
#         debugMessage(self.game.grid)
#         # pixelBoard
#         lc = 0
#         for row in self.game.grid:
#             for e in row:
#                 self.macropad.pixelColor(lc, self.playerColors[e]["board"])
#                 lc += 1
#         if self.game.winner != None:
#             print(
#                 f"""The winner is\n    {self.game.checkForWinner()}.\n{ self.game.action }"""
#             )
#             for i in (9, 11):
#                 self.macropad.pixelColor(
#                     i, self.playerColors[self.game.winner]["winner"]
#                 )
#         else:
#             boardColor = {10: 0x222222}
#             for s in [9, "X"], [11, "O"]:
#                 boardColor[s[0]] = self.playerColors[s[1]]["inactive"]
#                 if s[1] == self.game.players[self.game.currentPlayer]:
#                     print(s[1])
#                     boardColor[s[0]] = self.playerColors[s[1]]["active"]
#             for k in boardColor:
#                 self.macropad.pixelColor(k, boardColor[k])
#         if self.game.lastPlay != None:
#             (x, y) = self.game.lastPlay
#             index = x * 3 + y
#             self.macropad.pixelColor(
#                 index, self.playerColors[self.game.grid[x][y]]["lastPlay"]
#             )
#     def loop(self):
#         while True:
#             time.sleep(0.001)
#             self.update()
#     def update(self):
#         self.draw()
#         self.play()
