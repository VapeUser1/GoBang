#评估整个局面
import AIfunction
import board
'''def evaluate_board(board, player):#player表示当前可以落子的玩家，评分始终表示白棋（AI）的优势度，board为二阶列表
    #思路：先获得整个局面所有的白棋点位，然后对每个点位获取其所在的横竖撇捺
    whitepoints = [(x, y) for x in range(len(board)) for y in range(len(board)) if board[x][y] == 2]
    blackpoints = [(x, y) for x in range(len(board)) for y in range(len(board)) if board[x][y] == 1]
    score = (0,0,0) #分别表示一步获胜，
    if player == 2:#先把轮到白棋下的情况写好
        conditions = ['22222', '02222', '022200', '02220', '002200']
        conditions2 = ['011110','011100','01111','01110','001100']
        #开始遍历所有白色点位
        for p in whitepoints:
            info = AIfunction.get_position_info(board, p[0], p[1])
            p_score = [0,0,0,0,0] #表示上述五种情况在这个点出现的次数
            for i in range(5):
                for line in info:
                    if conditions[i] in line:
                        p_score[i] += 1
            #如果有两个以上的活三或者冲四，算作一个胜利
            if p_score[0] >= 1 or p_score[1] >= 1:
                return float('inf')
            if p_score[2] >= 2:
                score += 10000
            else:
                score += p_score[3]*10 + p_score[4]*2
        #再遍历所有黑色点位，看看有没有必须要阻止的
        return score
    else: # 轮到黑棋下的情况，评分还是正数，因为还是读取白棋的情况，但是胜利条件要改变，比如02222不能直接胜利了
        conditions = ['22222','022220','022200','02222','02220','002200']
        for p in whitepoints:
            info = AIfunction.get_position_info(board, p[0], p[1])
            p_score = [0,0,0,0,0,0] #表示上述六种情况在这个点出现的次数
            for i in range(6):
                for line in info:
                    if conditions[i] in line:
                        p_score[i] += 1
            #如果有两个以上的活三或者冲四，算作一个胜利
            if p_score[0] >= 1 or p_score[1] >= 1 or p_score[2] >= 2 or p_score[3] >= 2:
                return float('inf')
            else:
                score += p_score[3]*1000 + p_score[4]*300 + p_score[5]*100'''
#先写一下评估单个玩家的函数，评估当前玩家的优势度，返回一个数值，数值越大表示当前玩家越有优势
def evaluate_player(board, player):
    pass
#把两个玩家的分数相减得到局面对AI方的评分用于minimax
