#定义真人和ai玩家的类，包含获取用户输入的方法
import AIfunction
import random
import copy
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
#第一级AI：在密集位置随机选取位置
class AIPlayer1(Player):
    def getMove(self, board):
        # 在这里实现AI获取用户输入的方法
        empty_cells = board.getValuablePlace(2)
        return random.choice(empty_cells)
#第二级AI：在密集位置中根据分数判断选取最有利的位置
class AIPlayer2(Player):
    def getMove(self, board):
        empty_cells = board.getValuablePlace(3)
        # 根据分数选择最有利的位置
        best_move = max(empty_cells, key=lambda cell: self.getScore(cell, board))
        print(best_move)
        return best_move
    def getScore(self, cell, board):
        # 在这里实现评分函数
        # 先把当前的棋盘深度复制一份
        vboard = copy.deepcopy(board.board)
        x, y = cell
        # 假设AI下在这个位置
        vboard[x][y] = self.piece
        line_counts = AIfunction.get_line_count(vboard, x, y) #检测横竖斜四个方向上的连线长度
        print(f'Line counts for {cell}: {line_counts}')
        #下面开始检测这个点的分数，主要是检测这个点在横竖斜四个方向上形成的棋型
        return sum(line_counts)  # 示例：随机返回一个分数
#第三级AI：考虑多步决策树
class AIPlayer3(Player):
    def getMove(self, board):
        pass