# from utils import debugAnounce
# from utils import rotate
# class Board:
#     history = []
#     future = []
#     def __init__(self) -> None:
#         self.reset()
#     @property
#     def lastPlay(self):
#         if 0 < len(self.history):
#             return self.history[-1]
#         return None
#     @debugAnounce
#     def reset(self):
#         self.grid: list[list[str]] = [["", "", ""], ["", "", ""], ["", "", ""]]
#         self.players: list[str] = ["X", "O"]
#         self.currentPlayer: int = 0
#         self.turns: int = 0
#         self.winner = None
#         self.action: str = ""
#         self.history = []
#     @debugAnounce
#     def resetFuture(self):
#         self.future = []
#     @debugAnounce
#     def undo(self):
#         if 0 < len(self.history):
#             self.future.append(self.history.pop())
#             oldHist = self.history
#             self.reset()
#             for play in oldHist:
#                 self.play(*play, retainFuture=True)
#     @debugAnounce
#     def redo(self):
#         if 0 < len(self.future):
#             self.play(*self.future.pop(), retainFuture=True)
#     @debugAnounce
#     def incrementPlayer(self):
#         self.currentPlayer += 1
#         if len(self.players) <= self.currentPlayer:
#             self.currentPlayer = self.currentPlayer % len(self.players)
#     @debugAnounce
#     def play(self, x: int, y: int, retainFuture=False) -> bool:
#         if self.winner == None:
#             if self.grid[x][y] == "":
#                 self.history.append([x, y])
#                 self.grid[x][y] = self.players[self.currentPlayer]
#                 self.incrementPlayer()
#                 self.turns += 1
#                 self.checkForWinner()
#                 if not retainFuture:
#                     self.resetFuture()
#                 return True
#         return False
#     def checkForWinner(self):
#         for g in (self.grid, rotate(self.grid)):
#             for row in g:
#                 if row[0] in self.players:
#                     if row[0] == row[1] and row[0] == row[2]:
#                         self.winner = row[0]
#             if g[0][0] in self.players:
#                 if g[0][0] == g[1][1] and g[0][0] == g[2][2]:
#                     self.winner = g[0][0]
#         if 9 <= self.turns and self.winner == None:
#             self.winner = "No One"
#         return self.winner
#     def declareWinner(self, winner, action):
#         if self.winner == None:
#             self.winner = winner
#             self.action = action
