# AI相关的函数
# AI执白棋（2）
# 基础函数：检测横竖斜方向连线长度
AIplayer = 2
def get_line_count(board, x, y, dx=1, dy=1):
    global AIplayer
    size = len(board)
    count = [] #存储横 竖 主对角 副对角方向上的连线长度
    for i in range(4):
        count.append([0])
    for i in range(-4, 5):
        nx, ny = x + i * dx, y + i * dy
        if 0 <= nx < size and 0 <= ny < size and board[nx][ny] == AIplayer:
            count[2][0] += 1
        else:
            count[2].append(count[2][0])
            count[2][0] = 0
    for i in range(-4, 5):
        nx, ny = x + i * dx, y - i * dy
        if 0 <= nx < size and 0 <= ny < size and board[nx][ny] == AIplayer:
            count[3][0] += 1
        else:
            count[3].append(count[3][0])
            count[3][0] = 0
    for i in range(-4, 5):
        nx, ny = x + i * dx, y
        if 0 <= nx < size and 0 <= ny < size and board[nx][ny] == AIplayer:
            count[0][0] += 1
        else:
            count[0].append(count[0][0])
            count[0][0] = 0
    for i in range(-4, 5):
        nx, ny = x, y + i * dy
        if 0 <= nx < size and 0 <= ny < size and board[nx][ny] == AIplayer:
            count[1][0] += 1
        else:
            count[1].append(count[1][0])
            count[1][0] = 0
    res = [max(c) for c in count]
    return res
