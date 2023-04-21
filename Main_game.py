import tkinter as tk
import tkinter.messagebox
import Welcome as wel

class TicTacToeBoard(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        
        # Create the 9x9 buttons for the board
        self.buttons = []
        for i in range(9):
            row = []
            for j in range(9):
                button = tk.Button(self, text="", font=("Helvetica", 32), width=2, height=1, fg = "black",
                                   command=lambda i=i, j=j: self.button_click(i, j))
                button.grid(row=i, column=j, padx=5, pady=5)
                row.append(button)
            self.buttons.append(row)

        # Initialize the game state
        self.current_player = "X"
        self.current_block_pos = (1,1)
        self.block_state = [["" for _ in range(3)] for _ in range(3)]
        self.board_state = [["" for _ in range(9)] for _ in range(9)]
        self.game_over = False
        self.winner = ""
        #these are used to keep track of current states
        # a block is a 3x3 group of squares

    def button_click(self, i, j):
        # Check if the button has already been clicked or if the game is over
        if self.block_state[self.current_block_pos[0]][self.current_block_pos[1]]!="" :
            if self.board_state[i][j]!="" or self.game_over or (int((i)/3),int((j)/3))==self.current_block_pos:
                return

            # Update the button text and the game state
        
            # self.buttons[i][j].config(text=self.current_player)
            self.buttons[i][j]['text']=self.current_player
            self.board_state[i][j] = self.current_player

            for I in range(3):
                for J in range(3):
                    self.check_block(I,J)
        
            self.current_block_pos=(i%3,j%3)

            # Check if the game is over
            if self.check_win() or self.check_tie():
                self.game_over = True

            # Switch to the other player
            self.current_player = "O" if self.current_player == "X" else "X"

            print (self.buttons[i][j]["text"], "**", i, j, "##", self.current_block_pos,"**", 2)
        
        else:
            if self.board_state[i][j]!="" or self.game_over or (int((i)/3),int((j)/3))!=self.current_block_pos:
                return

            # Update the button text and the game state
        
            # self.buttons[i][j].config(text=self.current_player)
            self.buttons[i][j]['text']=self.current_player
            self.board_state[i][j] = self.current_player

            for I in range(3):
                for J in range(3):
                    self.check_block(I,J)
        
            self.current_block_pos=(i%3,j%3)

            # Check if the game is over
            if self.check_win() or self.check_tie():
                self.game_over = True


            # Switch to the other player
            self.current_player = "O" if self.current_player == "X" else "X"

            print (self.buttons[i][j]["text"], "**", i, j, "##", self.current_block_pos,"**", 1)
        
    
    def check_block(self, I, J):
        # Check rows
        for i in range(3):
            if self.board_state[i+I*3][3*J] == self.board_state[i+I*3][3*J+1] == self.board_state[i+I*3][3*J+2] != "":
                self.highlight_win(i+I*3, 3*J)
                self.highlight_win(i+I*3, 3*J+1)
                self.highlight_win(i+I*3, 3*J+2)
                self.block_state[I][J]=self.current_player

        # Check columns
        for j in range(3):
            if self.board_state[I*3][j+3*J] == self.board_state[I*3+1][j+3*J] == self.board_state[I*3+2][j+3*J] != "":
                self.highlight_win(I*3, j+3*J)
                self.highlight_win(I*3+1, j+3*J)
                self.highlight_win(I*3+2, j+3*J)
                self.block_state[I][J]=self.current_player

        # Check diagonals
        if self.board_state[I*3][3*J] == self.board_state[3*I+1][3*J+1] == self.board_state[3*I+2][3*J+2] != "":
            self.highlight_win(I*3, 3*J)
            self.highlight_win(3*I+1, 3*J+1)
            self.highlight_win(3*I+2, 3*J+2)
            self.block_state[I][J]=self.current_player

        if self.board_state[I*3][3*J+2] == self.board_state[3*I+1][3*J+1] == self.board_state[3*I+2][3*J] != "":
            self.highlight_win(I*3+2, 3*J) 
            self.highlight_win(3*I+1, 3*J+1) 
            self.highlight_win(3*I, 3*J+2)
            self.block_state[I][J]=self.current_player

    def check_win(self):
        # Check rows
        for i in range(3):
            if self.block_state[i][0] == self.block_state[i][1] == self.block_state[i][2] != "":
                self.winner=self.current_player
                self.messagebox(self.winner)
                return True

        # Check columns
        for j in range(3):
            if self.block_state[0][j] == self.block_state[1][j] == self.block_state[2][j] != "":
                self.winner=self.current_player
                self.messagebox(self.winner)
                return True

        # Check diagonals
        if self.block_state[0][0] == self.block_state[1][1] == self.block_state[2][2] != "":
            self.winner=self.current_player
            self.messagebox(self.winner)
            return True

        if self.block_state[0][2] == self.block_state[1][1] == self.block_state[2][0] != "":
            self.winner=self.current_player
            self.messagebox(self.winner)
            return True

        return False
    
    #remember to change the highlight color

    def check_tie(self):
        for row in self.board_state:
            for cell in row:
                if cell == "":
                    return False
        self.winner="tie"
        self.messagebox(self.winner)
        return True

    def highlight_win(self, i, j):
        if self.block_state=="X":
            self.buttons[i][j]['fg'] = "green"
        else:
            self.buttons[i][j]['fg'] = "blue"
    
    def messagebox(text=""):
        tkinter.messagebox.showinfo( "Game Ended", text)
            
class game:
    def start_welcome(self):
        welcome=wel.welcome()

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Giant Tic-Tac-Toe Main Game")
        t = tk.Label(self.root, text = "Giant Tic-Tac-Toe Instructions")
        t.config(font =("Courier", 30))
        author = tk.Label(self.root, text = "Created by Terence Chalk and Alexander Huang")
        author.config(font =("Courier", 15))
        b = tk.Button(self.root, text = "Exit to Welcome", command = lambda: [self.start_welcome()])  

        t.pack()
        author.pack()
        b.pack()
        board = TicTacToeBoard(self.root)
        board.pack()

        self.root.mainloop()

