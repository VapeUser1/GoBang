# AI相关的函数
# AI执白棋（2）
# 基础函数：检测横竖斜方向连线长度
import copy
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
#获取棋盘上一点所在的横竖斜信息
def get_position_info(board, x, y):
    line1 = board[x]  # 横
    line2 = [board[i][y] for i in range(len(board))]  # 竖
    line3 = [board[x + i][y + i] for i in range(-4, 5) if 0 <= x + i < len(board) and 0 <= y + i < len(board)]  # 主对角
    line4 = [board[x + i][y - i] for i in range(-4, 5) if 0 <= x + i < len(board) and 0 <= y - i < len(board)]  # 副对角
    info = (line1, line2, line3, line4)
    return (''.join(map(str, line)) for line in info)
#重新写一下检测横竖斜方向连线长度的函数
def get_line_count(board, x, y):
    vboard = copy.deepcopy(board)
    vboard[x][y] = 2  # 假设AI下在这个位置
    info = get_position_info(vboard, x, y)
    win_conditions = '22222'
    win_conditions2 = '022220'
    valuable_conditions = '02220'
    normal_conditions = '0222'
    scorelst = [0,0,0]
    for line in info:
        if win_conditions in line or win_conditions2 in line:
            scorelst[0] += 2
        elif valuable_conditions in line:
            scorelst[1] += 1
        elif normal_conditions in line:
            scorelst[2] += 1
    if scorelst[1] >= 2:
        scorelst[0] += 1
    return scorelst
#计算一点距离边界距离
def get_distance_to_edge(board, x, y):
    size = len(board)
    return min(x, y, size - 1 - x, size - 1 - y)
#阻拦黑棋判定
def is_blocking_opponent(board, x, y):
    vboard = copy.deepcopy(board)
    vboard[x][y] = 1  # 假设黑棋下这里
    win_conditions = '11111'
    win_conditions2 = '011110'
    dangerous_conditions = '01110'
    info = get_position_info(vboard, x, y)
    scorelst = [0,0]#表示必须拦截，潜在威胁
    for line in info:
        if win_conditions in line or win_conditions2 in line:
            scorelst[0] += 2
        if dangerous_conditions in line:
            scorelst[1] += 1
    #有两个活3也必须拦截：
    if scorelst[1] >= 2:
        scorelst[0] += 1
    return scorelst
#综合计算得分
def get_score(board, x, y):
    #优先级：胜利→阻止对方胜利→冲四活三→周围棋子数
    ailst = get_line_count(board, x, y)
    playerlst = is_blocking_opponent(board, x, y)
    distance = get_distance_to_edge(board, x, y)
    scorelst = [ailst[0], playerlst[0], ailst[1], playerlst[1], ailst[2], distance, len(get_nearby_pieces(board, x, y))]
    weights = [1000000, 10000, 1000, 500, 100, 10, 1]
    return sum(s * w for s, w in zip(scorelst, weights))