#用来实现3级ai的决策树算法，暂时不考虑剪枝和alpha-beta优化，先实现一个简单的两层决策树
import copy
import board
import AIfunction
#先定义决策树的class
class GameTreeNode:
    def __init__(self, board, player = 2, latestMove = None, parent=None):
        self.board = copy.deepcopy(board)
        self.player = player
        self.latestMove = latestMove
        self.parent = parent
        self.children = []
        self.score = 0

    def add_child(self, child):
        self.children.append(child)

    def evaluate(self):
        # 评估当前局面
        if self.player == 2:
            self.score = AIfunction.get_score(self.board.board, self.latestMove[0], self.latestMove[1]) if self.latestMove else 0
        else:
            self.score = -AIfunction.get_score(self.board.board, self.latestMove[0], self.latestMove[1]) if self.latestMove else 0
        node_score = self.score
        for child in self.children:
            #对每个路径进行评估然后
            child_score = child.evaluate()
            if child_score is not None:
                self.score += (child_score + node_score)
        return self.score

#定义函数：创建决策树，共2层
def create_game_tree(board, player, latestMove):
    root = GameTreeNode(board, player, latestMove)
    # 生成第一层子节点，为防止计算量爆炸，只考虑周围有棋子的位置
    valuable_positions = board.getValuablePlace(3)
    for pos in valuable_positions:
        child = GameTreeNode(board, 3 - player, pos, parent=root)
        root.add_child(child)
    return root