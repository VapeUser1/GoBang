#用于实现棋盘和棋子的图形化
import tkinter as tk
import board

class GobangGUI:
    def __init__(self, master, board):
        self.master = master
        self.master.title("五子棋")
        self.board = board
        self.size = self.board.size
        self.canvas = tk.Canvas(self.master, width=40*self.size+80, height=40*self.size+80+40, bg='lightgreen')
        self.canvas.pack()
        self.draw_board()

    def draw_board(self):
        self.canvas.create_rectangle(40, 20, 80 + (self.size-1) * 40, 60 + (self.size-1) * 40, outline="black", fill='lightyellow')
        for i in range(self.size):
            self.canvas.create_line(60 + i * 40, 40, 60 + i * 40, 40 + (self.size-1) * 40)
            self.canvas.create_line(60, 40 + i * 40, 60 + (self.size-1) * 40, 40 + i * 40)

    def draw_piece(self, x, y, player):
        r = 15
        x1 = x - r
        y1 = y - r
        x2 = x + r
        y2 = y + r
        color = 'black' if player == 1 else 'white'
        self.canvas.create_oval(x1, y1, x2, y2, fill=color)

if __name__ == "__main__":
    root = tk.Tk()
    gobang_gui = GobangGUI(root, board.Board())
    root.mainloop()
