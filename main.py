#主程序
import tkinter
import tkinter.messagebox
from tkinter import simpledialog
import winsound
import board
import Player
import visualize

def updateUI(gui):
    for i in range(gui.board.size):
        for j in range(gui.board.size):
            if gui.board.board[i][j] == 1:
                gui.canvas.create_oval(60 + j * 40 - 15, 40 + i * 40 - 15, 60 + j * 40 + 15, 40 + i * 40 + 15, fill='black')
            elif gui.board.board[i][j] == 2:
                gui.canvas.create_oval(60 + j * 40 - 15, 40 + i * 40 - 15, 60 + j * 40 + 15, 40 + i * 40 + 15, fill='white')
#下面是主程序
#先弹出对话框，询问用户是否开始游戏
if tkinter.messagebox.askyesno("五子棋", "是否开始新游戏？"):
    #如果用户选择“是”，则开始新游戏
    #先询问用户需要多大的棋盘
    size = simpledialog.askinteger("五子棋", "请输入棋盘大小（默认为15）", initialvalue=15)
    init_board = board.Board(size)
    #然后问人机对战还是双人
    mode = tkinter.messagebox.askyesno("五子棋", "是否进行人机对战？")
    #创建可视化界面
    root = tkinter.Tk()
    if mode:
        player1 = Player.HumanPlayer("玩家", 1)
        player2 = Player.AIPlayer("AI", 2)
    else:
        player1 = Player.HumanPlayer("黑方", 1)
        player2 = Player.HumanPlayer("白方", 2)
    ui = visualize.GobangGUI(root, init_board, player1, player2)
    ui.run()

