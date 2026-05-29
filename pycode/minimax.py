#不做树结构，直接写minimax
import board
import AIfunction
import copy
#先写minimax函数，思路：输入board类，深度，和当前玩家，返回最高得分
def minimax(board, depth, player):
    if depth == 0 or board.check_win() != 0 or len(board.get_empty_positions()) == 0:
        return AIfunction.evaluate_board(board.board) #返回棋局得分
    if player == 2: #AI白棋
        best_score = -float('inf') #开始搜索最佳得分，初始化为负无穷
        for x,y in board.getValuablePlace(2): #只搜索周围3个位置
            board.board[x][y] = player #模拟落子
            score = minimax(board, depth-1, 3-player) #递归搜索下一层
            best_score = max(score, best_score) #更新最佳得分
            board.board[x][y] = 0 #撤销落子
        return best_score
    else: #人类黑棋
        best_score = float('inf') #开始搜索最佳得分，初始化为正无穷
        for x,y in board.getValuablePlace(2): #只搜索周围3个位置
            board.board[x][y] = player #模拟落子
            score = minimax(board, depth-1, 3-player) #递归搜索下一层
            best_score = min(score, best_score) #更新最佳得分
            board.board[x][y] = 0 #撤销落子
        return best_score

def getBestMove(board, depth):
    places = board.getValuablePlace(2)
    best_score = -float('inf')
    best_move = None
    for x, y in places:
        board.board[x][y] = 2  # AI白棋落子
        score = minimax(board, depth-1, 1)  # 递归搜索
        board.board[x][y] = 0  # 撤销落子
        if score > best_score:
            best_score = score
            best_move = (x, y)
    return best_move