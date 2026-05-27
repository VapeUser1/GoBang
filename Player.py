#定义真人和ai玩家的类，包含获取用户输入的方法
import visualize
import random
#定义玩家类型，有两个子类：真人和ai
class Player:
    def __init__(self, name, piece):
        self.name = name
        self.piece = piece
class HumanPlayer(Player):
    def getMove_cmd(self):
        x, y = map(int, input("Enter your move (row and column): ").split())
        return x, y
    def getMove(self, gui):
        # 在这里实现图形用户界面的获取用户输入的方法
        pass
class AIPlayer(Player):
    def getMove(self, board):
        # 在这里实现AI获取用户输入的方法
        empty_cells = [(i, j) for i in range(board.size) for j in range(board.size) if board.board[i][j] == 0]
        return random.choice(empty_cells)
