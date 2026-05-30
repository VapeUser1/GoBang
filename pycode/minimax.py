# 不做树结构，直接写minimax，加入 alpha-beta 剪枝
import board
import AIfunction
import copy

# 先写minimax函数，思路：输入 board 类，深度，和当前玩家，返回最高得分
def minimax(board, depth, player, alpha=-float('inf'), beta=float('inf')):
    """
    带 alpha-beta 剪枝的 minimax。
    player: 当前落子方（1 或 2）。
    返回该节点的估值（越大表示对白方/AI越有利，保持与 AIfunction.evaluate_board 一致）。
    """
    # 终止条件：有人已胜或达到深度或无子可下
    w = board.check_win()
    if w != 0:
        return float('inf') if w == 2 else -float('inf')
    if depth == 0 or len(board.get_empty_positions()) == 0:
        return AIfunction.evaluate_board(board)

    # 最大化节点（AI 白棋，player==2）
    if player == 2:
        value = -float('inf')
        for x, y in board.getValuablePlace(1):
            board.board[x][y] = player
            board.current_player = 3 - board.current_player
            score = minimax(board, depth - 1, 3 - player, alpha, beta)
            board.board[x][y] = 0
            board.current_player = 3 - board.current_player

            if score > value:
                value = score
            if value > alpha:
                alpha = value
            # beta 剪枝
            if alpha >= beta:
                break
        return value

    # 最小化节点（人类 黑棋，player==1）
    else:
        value = float('inf')
        for x, y in board.getValuablePlace(1):
            board.board[x][y] = player
            board.current_player = 3 - board.current_player
            score = minimax(board, depth - 1, 3 - player, alpha, beta)
            board.board[x][y] = 0
            board.current_player = 3 - board.current_player

            if score < value:
                value = score
            if value < beta:
                beta = value
            # alpha 剪枝
            if alpha >= beta:
                break
        return value


def getBestMove(board, depth):
    places = board.getValuablePlace(1)
    best_score = -float('inf')
    best_move = None
    # 初始 alpha/beta
    alpha = -float('inf')
    beta = float('inf')
    for x, y in places:
        board.board[x][y] = 2  # AI 白棋落子
        board.current_player = 3 - board.current_player
        score = minimax(board, depth - 1, 1, alpha, beta)
        board.board[x][y] = 0  # 撤销落子
        board.current_player = 3 - board.current_player
        if score > best_score:
            best_score = score
            best_move = (x, y)
        if best_score > alpha:
            alpha = best_score
        # 如果某一步已经能达到 beta（极端情况），可以提前退出
        if alpha >= beta:
            break
    # 调试信息：最佳得分
    try:
        steps = getattr(board, 'steps', '?')
    except Exception:
        steps = '?'
    print('best score for move' + str(steps) + ': ' + str(best_score))
    return best_move, best_score