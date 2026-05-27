#用于实现棋盘和棋子的图形化
#把生成tkinter界面的内容也写在这里面
#每下一步棋就刷新一下棋盘
import tkinter as tk
import board
import winsound
import Player

class GobangGUI:
    def __init__(self, master, board, player1, player2):
        self.master = master
        self.master.title("五子棋")
        self.board = board
        self.size = self.board.size
        self.player1 = player1
        self.player2 = player2
        self.canvas = tk.Canvas(self.master, width=40*self.size+80, height=40*self.size+80+40, bg='lightgreen')
        self.canvas.pack()
        if isinstance(self.player2, Player.AIPlayer):
            self.canvas.bind("<Button-1>", self.on_click_ai)
        else:
            self.canvas.bind("<Button-1>", self.on_click) #鼠标左键绑定下棋

    def draw_board(self):
        self.canvas.create_rectangle(40, 20, 80 + (self.size-1) * 40, 60 + (self.size-1) * 40, outline="black", fill='lightyellow')
        for i in range(self.size):
            self.canvas.create_line(60 + i * 40, 40, 60 + i * 40, 40 + (self.size-1) * 40)
            self.canvas.create_line(60, 40 + i * 40, 60 + (self.size-1) * 40, 40 + i * 40)
        self.master.update()

    def refresh(self):
        self.canvas.delete("all")
        self.draw_board()
        s = self.size
        for i in range(s):
            for j in range(s):
                if self.board.board[i][j] == 1:
                    self.canvas.create_oval(60 + j * 40 - 15, 40 + i * 40 - 15, 60 + j * 40 + 15, 40 + i * 40 + 15, fill='black')
                elif self.board.board[i][j] == 2:
                    self.canvas.create_oval(60 + j * 40 - 15, 40 + i * 40 - 15, 60 + j * 40 + 15, 40 + i * 40 + 15, fill='white')
    #单独把询问是否重新开始做成模块
    def ask_restart(self):
        tk.messagebox.showinfo("游戏结束", f"{'黑子' if self.board.check_win() == 1 else '白子'}获胜！")
        if tk.messagebox.askyesno("五子棋", "是否开始新游戏？"):
            self.board.reset()
            self.refresh()
        else:
            self.master.quit()

    def on_click(self, event):
        x = event.x
        y = event.y
        col = (x - 40) // 40
        row = (y - 20) // 40
        self.board.add_piece(row, col)
        self.refresh()
        winsound.PlaySound('step.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
        #每下完一步都检测一下有没有赢
        if self.board.check_win() != 0:
            self.ask_restart()

    def on_click_ai(self, event):
        x = event.x
        y = event.y
        col = (x - 40) // 40
        row = (y - 20) // 40
        if self.board.current_player == 1:
            self.board.add_piece(row, col)
            self.refresh()
            winsound.PlaySound('step.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
            if self.board.check_win() != 0:
                self.ask_restart()
                return
        c2,r2 = self.player2.getMove(self.board)
        self.board.add_piece(c2, r2)
        self.refresh()
        winsound.PlaySound('step.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
        if self.board.check_win() != 0:
            self.ask_restart()
            return

    def run(self):
        self.draw_board()
        self.master.mainloop()
        self.master.update()

'''if __name__ == "__main__":
    root = tk.Tk()
    gobang_gui = GobangGUI(root, board.Board())
    gobang_gui.canvas.bind("<Button-1>", gobang_gui.on_click)
    root.mainloop()'''
