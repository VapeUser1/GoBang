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
def get_position_info(board, x, y, size=11):
    n = len(board)
    def get_line(dx, dy):
        line = []
        for i in range(-n, n):
            nx, ny = x + i * dx, y + i * dy
            if 0 <= nx < n and 0 <= ny < n:
                line.append(board[nx][ny])
            '''else:
                line.append(0)  # 边界补0'''
        return ''.join(map(str, line))
    horizontal = get_line(0, 1)
    vertical   = get_line(1, 0)
    diag1      = get_line(1, 1)
    diag2      = get_line(1, -1)
    return [horizontal, vertical, diag1, diag2]
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

#评估局面对玩家的优势度
def evaluate_player(board, player):
    score = 0

    n = len(board)
    m = len(board[0])

    piece_list = [(i, j)
                  for i in range(n)
                  for j in range(m)
                  if board[i][j] == player]

    conditions = ['11111', '011110', '11110', '01110'] if player == 1 else \
                 ['22222', '022220', '22220', '02220']

    seen = set()  # 防止重复计分（关键优化）

    for x, y in piece_list:
        info = list(get_position_info(board, x, y))

        for d in range(4):
            key = (x, y, d)
            if key in seen:
                continue
            seen.add(key)

            pattern = info[d]

            if pattern == conditions[0]:
                return 10**8  # 五连直接胜

            elif pattern == conditions[1]:
                score += 20000  # 活四（高威胁）

            elif pattern == conditions[2]:
                score += 5000   # 冲四

            elif pattern == conditions[3]:
                score += 1000   # 活三

    return score

#评估局面总体对AI的得分
def evaluate_board(board):
    ai_score = evaluate_player(board, 2)
    player_score = evaluate_player(board, 1)
    return ai_score - player_score

