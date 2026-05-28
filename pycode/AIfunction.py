# AI相关的函数
# AI执白棋（2）
# 基础函数：检测横竖斜方向连线长度
import copy
def get_line_count(board, x, y, dx=1, dy=1, AIPlayer=2):
    vboard = copy.deepcopy(board)
    vboard[x][y] = AIPlayer  # 假设AI下在这个位置
    size = len(vboard)
    count = []  # 存储横 竖 主对角 副对角方向上的连线长度
    for i in range(4):
        count.append([0])
    for i in range(-4, 5):
        nx, ny = x + i * dx, y + i * dy
        if 0 <= nx < size and 0 <= ny < size and vboard[nx][ny] == AIPlayer:
            count[2][0] += 1
        else:
            count[2].append(count[2][0])
            count[2][0] = 0
    for i in range(-4, 5):
        nx, ny = x + i * dx, y - i * dy
        if 0 <= nx < size and 0 <= ny < size and vboard[nx][ny] == AIPlayer:
            count[3][0] += 1
        else:
            count[3].append(count[3][0])
            count[3][0] = 0
    for i in range(-4, 5):
        nx, ny = x + i * dx, y
        if 0 <= nx < size and 0 <= ny < size and vboard[nx][ny] == AIPlayer:
            count[0][0] += 1
        else:
            count[0].append(count[0][0])
            count[0][0] = 0
    for i in range(-4, 5):
        nx, ny = x, y + i * dy
        if 0 <= nx < size and 0 <= ny < size and vboard[nx][ny] == AIPlayer:
            count[1][0] += 1
        else:
            count[1].append(count[1][0])
            count[1][0] = 0
    res = [max(c) for c in count]
    return res
#获取周围棋子
def get_nearby_pieces(board, x, y):
    nearby = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(board) and 0 <= ny < len(board) and board[nx][ny] != 0:
                nearby.append((nx, ny, board[nx][ny]))
    return nearby
#阻拦黑棋判定
def is_blocking_opponent(board, x, y):
    vboard = copy.deepcopy(board)
    vboard[x][y] = 1  # 假设黑棋下这里
    lst = get_line_count(vboard, x, y, AIPlayer=1)
    return [lst.count(5), lst.count(4), lst.count(3)]
#综合计算得分
def get_score(board, x, y):
    #优先级：胜利→阻止对方胜利→冲四活三→周围棋子数
    ailst = get_line_count(board, x, y)
    playerlst = is_blocking_opponent(board, x, y)
    scorelst = [ailst.count(5), playerlst[0], ailst.count(4), playerlst[1], playerlst[2], ailst.count(3), len(get_nearby_pieces(board, x, y))]
    weights = [100000, 10000, 1000, 500, 100, 10, 1]
    return sum(s * w for s, w in zip(scorelst, weights))