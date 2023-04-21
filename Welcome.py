import tkinter as tk
import Main_game as mg
import Instruction as Inst

class welcome:
	def start_game(self):
		self.root.destroy
		game= mg.game()

	def start_instruction(self):
		self.root.destroy
		instruction = Inst.instruction()

	def __init__(self):
		self.root = tk.Tk()
		self.root.geometry("800x400")
		self.root.title("Tic-Tac-Toe Welcome")
		
		t = tk.Label(self.root, text = "Welcome to Giant Tic-Tac-Toe")
		t.config(font =("Courier", 45))
		author = tk.Label(self.root, text = "Created by Terence Chalk and Alexander Huang")
		author.config(font =("Courier", 20))

		b1 = tk.Button(self.root, text = "Proceed to the Game", command = lambda: [self.start_game()])
		b2 = tk.Button(self.root, text = "Exit", command = self.root.destroy)
		b3 = tk.Button(self.root, text = "Instruction", command = lambda: [self.start_instruction()])

		t.pack()
		author.pack()
		b1.pack()
		b2.pack()
		b3.pack()
		
		self.root.mainloop()

	

