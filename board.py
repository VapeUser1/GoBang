#负责定义和棋盘相关的类
#可参考start.pyw
#先定义棋盘的类
class Board:
    def __init__(self, size = 15):
        self.size = size
        self.board = [[0 for _ in range(size)] for _ in range(size)]
        self.current_player = 1
    # 重置棋盘
    def reset(self):
        self.current_player = 1
        self.board = [[0 for _ in range(self.size)] for _ in range(self.size)]
    # 落子操作
    def add_piece(self, x: int, y: int) -> bool:
        #用1代表黑子，2代表白子
        if x < 0 or x >= self.size or y < 0 or y >= self.size:
            return False
        if self.board[x][y] == 0:
            self.board[x][y] = self.current_player
            self.current_player = 3 - self.current_player
            return True
        return False
    # 获取所有空位
    def get_empty_positions(self):
        empty_positions = []
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    empty_positions.append((i, j))
        return empty_positions
    # 检查是否黑子或白子获胜，返回获胜方（1 or 2）
    def check_win(self):
        # 检查行
        for row in self.board:
            if self.check_line(row) != 0:
                return self.check_line(row)
        # 检查列
        for col in range(self.size):
            if self.check_line([self.board[row][col] for row in range(self.size)]) != 0:
                return self.check_line([self.board[row][col] for row in range(self.size)])
        # 检查对角线
        if self.check_line([self.board[i][i] for i in range(self.size)]) != 0 or \
           self.check_line([self.board[i][self.size - 1 - i] for i in range(self.size)]) != 0:
            return self.check_line([self.board[i][i] for i in range(self.size)])
        return 0
    def check_line(self, line):
        count = 0
        for cell in line:
            if cell == 1:
                count += 1
                if count == 5:
                    return 1
            else:
                count = 0
        count = 0
        for cell in line:
            if cell == 2:
                count += 1
                if count == 5:
                    return 2
            else:
                count = 0
        return 0
    def display(self):
        for row in self.board:
            print(' '.join(str(cell) for cell in row))
    #获取所有临近空位（周围n格有棋子）
    def getValuablePlace(self, n):
        valuable_positions = set()
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] != 0:
                    # 检查周围n格
                    for dx in range(-n, n + 1):
                        for dy in range(-n, n + 1):
                            if abs(dx) + abs(dy) <= n:
                                x, y = i + dx, j + dy
                                if 0 <= x < self.size and 0 <= y < self.size:
                                    if self.board[x][y] == 0 and (x, y) not in valuable_positions:
                                        valuable_positions.add((x, y))
        return list(valuable_positions)
    