import tkinter as tk

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.configure(bg='#1c1c1c')
        self.root.title("Tic-Tac-Toe")
        self.buttons = []
        self.player = "X"
        self.x_score = 0
        self.o_score = 0

        for i in range(3):
            button_row = []
            for j in range(3):
                button = tk.Button(self.root, text=" ", width=5, height=2, bg = '#1c1c1c',fg='#00ffff', activebackground = '#1c1c1c', activeforeground = '#00ffff', relief = 'solid', bd = '5', highlightbackground = '#ff0000', command=lambda row=i, col=j: self.play(row, col))
                button.grid(row=i, column=j)
                button_row.append(button)
            self.buttons.append(button_row)

        self.x_label = tk.Label(self.root, text="X: 0", bg = '#1c1c1c', fg = '#00ffff')
        self.x_label.grid(row=3, column=0)
        self.o_label = tk.Label(self.root, text="O: 0", bg = '#1c1c1c', fg = '#00ffff')
        self.o_label.grid(row=3, column=1)
        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset, bg = '#1c1c1c', fg = 'Whitesmoke')
        self.reset_button.grid(row=3, column=2)

    def play(self, row, col):
        button = self.buttons[row][col]
        if button["text"] == " ":
            button["text"] = self.player
            if self.check_win():
                self.root.title("{} wins!".format(self.player))
                self.update_score()
                return
            if self.check_draw():
                self.root.title("Draw!")
                return
            if self.player == "X":
                self.player = "O"
            else:
                self.player = "X"

    def check_win(self):
        for i in range(3):
            if self.buttons[i][0]["text"] == self.player and self.buttons[i][1]["text"] == self.player and self.buttons[i][2]["text"] == self.player:
                self.create_line(i,0,i,2)
                self.root.title("{} wins!".format(self.player))
                self.update_score()
                return True
            if self.buttons[0][i]["text"] == self.player and self.buttons[1][i]["text"] == self.player and self.buttons[2][i]["text"] == self.player:
                self.create_line(0,i,2,i)
                self.root.title("{} wins!".format(self.player))
                self.update_score()
                return True
        if self.buttons[0][0]["text"] == self.player and self.buttons[1][1]["text"] == self.player and self.buttons[2][2]["text"] == self.player:
            self.create_line(0,0,2,2)
            self.root.title("{} wins!".format(self.player))
            self.update_score()
            return True
        if self.buttons[0][2]["text"] == self.player and self.buttons[1][1]["text"] == self.player and self.buttons[2][0]["text"] == self.player:
            self.create_line(0,2,2,0)
            self.root.title("{} wins!".format(self.player))
            self.update_score()
            return True
        return False


    def check_draw(self):
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j]["text"] == " ":
                    return False
        return True

    def create_line(self, r1, c1, r2, c2):
        x1, y1 = self.buttons[r1][c1].winfo_x(), self.buttons[r1][c1].winfo_y()
        x2, y2 = self.buttons[r2][c2].winfo_x(), self.buttons[r2][c2].winfo_y()
        x1, y1, x2, y2 = x1+5, y1+5, x2+5, y2+5
        self.canvas = tk.Canvas(self.root, width=250, height=250, bg = '#1c1c1c')
        self.canvas.create_line(x1, y1, x2, y2, width=5, fill="#ff0000")
        self.canvas.grid(row = 0,column = 0,rowspan = 3,columnspan = 3)

    def update_score(self):
        if self.player == "X":
            self.x_score += 1
            self.x_label.config(text="X: {}".format(self.x_score))
        else:
            self.o_score += 1
            self.o_label.config(text="O: {}".format(self.o_score))

    def reset(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ")
        self.player = "X"
        self.x_score = 0
        self.o_score = 0
        self.x_label.config(text="X: 0")
        self.o_label.config(text="O: 0")
        self.root.title("Tic-Tac-Toe")
        self.canvas.destroy()

game = TicTacToe()
game.root.mainloop()



