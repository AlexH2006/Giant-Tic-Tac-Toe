import tkinter as tk
import Welcome as wel

class instruction:
	def start_welcome(self):
		welcome=wel.welcome()

	def __init__(self):
		self.root = tk.Tk()
		self.root.geometry("800x1000")
		self.root.title("Tic-Tac-Toe Instruction")
		
		t = tk.Label(self.root, text = "Giant Tic-Tac-Toe Instructions")
		t.config(font =("Courier", 30))
		author = tk.Label(self.root, text = "Created by Terence Chalk and Alexander Huang")
		author.config(font =("Courier", 15))

		b = tk.Button(self.root, text = "Exit to Welcome", command = lambda: [self.root.destroy, self.start_welcome()])

		T = tk.Text(self.root, width = 200)

		Rule = "The game starts with player 1 clicking in the middle square. \nAfter player one has played the first move player 2 most play a move in the square that corresponds to the square played in the center. This action will repeat until either player wins or there is a draw. \nTo win a small box you must get 3 of your markers in a row. To win the game you must have 3 large boxes claimed in a row; either horizontal, vertical, or diagonal. \nTo draw a small box the box must be full of markers and no one player can have 3 in a row in that box. Once this occurs this box is no longer in play. To draw the game no player has or can get 3 large boxes in a row."

		t.pack()
		author.pack()
		b.pack()
		T.pack()

		T.insert(tk.END, Rule)
		
		self.root.mainloop()