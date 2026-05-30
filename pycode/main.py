# 主程序
import tkinter
import tkinter.messagebox
from tkinter import simpledialog
import board
import Player
import visualize

def ask_game_mode(parent):
    dialog = tkinter.Toplevel(parent)
    dialog.title("五子棋")
    dialog.resizable(False, False)

    result = {'mode':False}

    tkinter.Label(
        dialog,
        text="请选择对战模式："
    ).pack(padx=20,pady=10)

    def choose_ai():
        result['mode']=True
        dialog.destroy()

    def choose_pvp():
        result['mode']=False
        dialog.destroy()

    dialog.protocol(
        "WM_DELETE_WINDOW",
        choose_pvp
    )

    frame=tkinter.Frame(dialog)
    frame.pack(pady=10)

    tkinter.Button(
        frame,
        text='人机',
        width=10,
        command=choose_ai
    ).pack(side='left',padx=8)

    tkinter.Button(
        frame,
        text='双人',
        width=10,
        command=choose_pvp
    ).pack(side='right',padx=8)

    dialog.grab_set()
    dialog.focus_force()

    parent.wait_window(dialog)

    return result['mode']

# 下面是主程序
if __name__ == '__main__':
    # 创建主窗口，先隐藏以便所有对话使用它作为父窗口
    root = tkinter.Tk()
    root.withdraw()

    # 先弹出对话框，询问用户是否开始新游戏
    if tkinter.messagebox.askyesno("五子棋", "是否开始新游戏？", parent=root):
        # 先询问用户需要多大的棋盘
        size = simpledialog.askinteger("五子棋", "请输入棋盘大小（默认为15）", initialvalue=15, parent=root)
        init_board = board.Board(size)

        # 然后问人机对战还是双人（使用自定义按钮：人机 / 双人）
        mode = ask_game_mode(root)
        if mode:
            player1 = Player.HumanPlayer("玩家", 1)
            AItier = simpledialog.askinteger("五子棋", "请输入AI难度（1-4），默认为1\n警告：4级难度可能导致游戏卡顿或不稳定", minvalue=1, maxvalue=4, initialvalue=1, parent=root)
            if AItier not in [1, 2, 3, 4]:
                AItier = 1
            if AItier == 1:
                player2 = Player.AIPlayer1("AI", 2)
            elif AItier == 2:
                player2 = Player.AIPlayer2("AI", 2)
            elif AItier == 3:
                player2 = Player.AIPlayer3("AI", 2)
            else:
                player2 = Player.AIPlayer4("AI", 2)
        else:
            player1 = Player.HumanPlayer("黑方", 1)
            player2 = Player.HumanPlayer("白方", 2)

        # 显示主窗口并创建可视化界面
        root.deiconify()
        ui = visualize.GobangGUI(root, init_board, player1, player2)
        ui.run()
    else:
        # 用户选择不开始新游戏，退出
        root.destroy()