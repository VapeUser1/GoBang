#定义真人和ai玩家的类，包含获取用户输入的方法
import AIfunction
import AIGameTree
import random
import minimax
#定义玩家类型，有两个子类：真人和ai
class Player:
    def __init__(self, name, piece):
        self.name = name
        self.piece = piece
    #2级ai使用算法
    def getMoveByScore(self, board):
        empty_cells = board.getValuablePlace(3)
        # 根据分数选择最有利的位置
        scores = [AIfunction.get_score(board.board, x, y) for x, y in empty_cells]
        max_score = max(scores) if scores else 0
        best_moves = [cell for cell, score in zip(empty_cells, scores) if score == max_score]
        return random.choice(best_moves) if best_moves else random.choice(empty_cells)
    #3级ai使用算法
    def getMoveByTree(self, board):
        empty_cells = board.getValuablePlace(3)
        for c in empty_cells:
            if AIfunction.get_score(board.board, c[0], c[1]) >= 1000000:
                return c
        # 如果没有找到直接获胜的棋步，使用决策树
        pos = []
        for c in empty_cells:
            pos.append(AIGameTree.create_game_tree(board, self.piece, c))
        # 在这里可以对决策树进行评估，选择最优解
        best_move = max(pos, key=lambda tree: tree.evaluate(), default=None)
        print(best_move.evaluate() if best_move else "No moves evaluated")
        if best_move and max(best_move.evaluate() for best_move in pos) >= 30000:
            return best_move.latestMove
        # 如果没有更好的选择就按照2级ai的算法
        return self.getMoveByScore(board)
    #4级ai使用算法
    def getMoveByMiniMax(self, board):
        return minimax.getBestMove(board, 3)

class HumanPlayer:
    def __init__(self, name, piece):
        self.name = name
        self.piece = piece
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
        return self.getMoveByScore(board)
#第三级AI：考虑多步决策树
class AIPlayer3(Player):
    def getMove(self, board):
        return self.getMoveByTree(board)
class AIPlayer4(Player):
    def getMove(self, board):
        return self.getMoveByMiniMax(board)