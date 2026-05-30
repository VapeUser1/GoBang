# AI相关的函数
# AI执白棋（2）
# 基础函数：检测横竖斜方向连线长度
import copy
from lst import lst1_in_lst2
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

# 提取：返回棋盘上所有长度>=5的直线（行/列/对角）字符串列表，便于评估函数复用
def get_all_lines(board):
    n = len(board)
    lines = []
    # rows
    for i in range(n):
        lines.append(board[i])
    # cols
    for j in range(n):
        lines.append([board[i][j] for i in range(n)])
    # diag (top-left to bottom-right)
    for k in range(-n + 5, n - 4):
        diag = []
        for i in range(n):
            j = i - k
            if 0 <= j < n:
                diag.append(board[i][j])
        if len(diag) >= 5:
            lines.append(diag)
    # anti-diag (top-right to bottom-left)
    for k in range(4, 2 * n - 4):
        adiag = []
        for i in range(n):
            j = k - i
            if 0 <= j < n:
                adiag.append(board[i][j])
        if len(adiag) >= 5:
            lines.append(adiag)
    return lines
#综合计算得分
def get_score(board, x, y):
    #优先级：胜利→阻止对方胜利→冲四活三→周围棋子数
    ailst = get_line_count(board, x, y)
    playerlst = is_blocking_opponent(board, x, y)
    distance = get_distance_to_edge(board, x, y)
    scorelst = [ailst[0], playerlst[0], ailst[1], playerlst[1], ailst[2], distance, len(get_nearby_pieces(board, x, y))]
    weights = [1000000, 10000, 1000, 500, 100, 10, 1]
    return sum(s * w for s, w in zip(scorelst, weights))

#评估局面对玩家的优势度，站在黑方先手的角度看
def evaluate_player(board, player):
    """
    使用列表匹配评估单个玩家的函数：
    - 扫描所有行（行/列/对角线），把每条线转换为整数列表
    - 使用滑动窗口统计重叠匹配；对于五连使用 lst1_in_lst2 做快速判断
    返回数值，越大表示该玩家越有利
    """
    # get_all_lines 已经直接返回了每条线的整数列表
    lines = get_all_lines(board)

    p = [player]
    zero = [0]
    patterns = {
        'five': p * 5,
        'open_four': zero + p * 4 + zero,
        'closed_four': p * 4 + zero,
        'open_three': zero + p * 3 + zero,
        'open_three_2': zero + p + zero + p * 2 + zero, #先手2步必胜
        'open_three_3': zero + p * 3 + zero * 2
    }

    def count_overlaps_list(line_list, pat):
        """滑动窗口计数，支持重叠匹配（基于列表相等）"""
        L = len(pat)
        if L == 0 or len(line_list) < L:
            return 0
        cnt = 0
        for i in range(len(line_list) - L + 1):
            if line_list[i:i+L] == pat:
                cnt += 1
        return cnt

    cnt = {k: 0 for k in patterns}
    # 遍历所有线并计数
    for line in lines:
        # 五连直接判胜（使用 lst 中的匹配判断，支持正反）
        if lst1_in_lst2(patterns['five'], line):
            return 10**9
        for name, pat in patterns.items():
            if name == 'five':
                continue
            cnt[name] += count_overlaps_list(line, pat)

    '''# 双活三或多个高威胁视为即胜的强威胁
    if cnt['open_three'] + cnt['open_three_2'] >= 2:
        return 3*10**5

    # 优先级赋值
    score = 0
    score += cnt['open_four'] * 10**6
    score += cnt['closed_four'] * 20000
    score += cnt['open_three'] * 10000
    score += cnt['open_three_2'] * 10**5'''
    score = 0
    #先考虑先手方：
    if player == 1:
        if cnt['open_four'] + cnt['closed_four'] > 0:
            return 10**9
        if cnt['open_three_2'] + cnt['open_three_3'] > 0:
            return 10**8
        score += cnt['open_three'] * 10000
    #然后是后手方：
    else:
        if cnt['open_four'] > 0:
            return 5 * 10**8
        if cnt['closed_four'] > 0 and cnt['open_three_2'] + cnt['open_three_3'] > 1:
            return 10**8
        if cnt['open_three_2'] + cnt['open_three_3'] > 1:
            return 5 * 10**7
        score += cnt['open_three'] * 10000
        score += (cnt['open_three_2'] + cnt['open_three_3']) * 100000
        
    return score

#评估局面总体对AI的得分
def evaluate_board(board): #需要考虑先后手影响，同样的局面先手方得分应该更高，系数暂定1.5
    vboard = board.board
    ai_score = evaluate_player(vboard, 2)
    player_score = evaluate_player(vboard, 1)
    # 先手优势系数稍微减少到1.2以避免过度放大先手
    k = 1
    return ai_score - k * player_score


