#定义真人和ai玩家的类，包含获取用户输入的方法
import AIfunction
import random
import time
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
        scores = [AIfunction.get_score(board.board, x, y) for x, y in empty_cells]
        max_score = max(scores) if scores else 0
        best_moves = [cell for cell, score in zip(empty_cells, scores) if score == max_score]
        return random.choice(best_moves) if best_moves else random.choice(empty_cells)
#第三级AI：考虑多步决策树
class AIPlayer3(Player):
    def getMove(self, board):
        pass