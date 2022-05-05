import tkinter
from tkinter import *
from mode import Mode
import pygame
from create import Create
import random




class Menu(Tk):
	def __init__(self):
		super().__init__()
		self.geometry("1280x750+150+0")
		self.title("Menu")
		self.bg = PhotoImage(file="assets/bg2.jpg")
		self.label = Label(self, image=self.bg)
		self.label.place(x=0, y=0, relheight=1, relwidth=1)



		self.Newgame_button= Button(self,text="                           New Game                           ",  font=("arial", 20, 'bold' ), bg="Cadet Blue", fg="#FBEEDF",  command= self.show_win, relief=RIDGE)
		self.Newgame_button.place(x=350, y =100)
		self.Highscore_button= Button(self,text="                           High Score                          ",  font=("arial", 20, 'bold' ), bg="Cadet Blue", fg="#FBEEDF",  command= self.show_win, relief=RIDGE)
		self.Highscore_button.place(x=350, y =250)
		self.sound_button= Button(self, text="                           Sound: OFF                          ",  font=("arial", 20, 'bold' ), bg="Cadet Blue", fg="#FBEEDF",  command= self.play, relief=RIDGE)
		self.sound_button.place(x=350, y =400)
		self.quit_button= Button(self,text="                                Create                                ",  font=("arial", 20, 'bold' ), bg="Cadet Blue", fg="#FBEEDF",  command= self.show_create, relief=RIDGE)
		self.quit_button.place(x=350, y =550)
		pygame.mixer.init()

	def play(self):
		pygame.mixer.music.load("music/neonon-109616.mp3")
		if self.sound_button["text"] != "                           Sound: ON                           ":
			self.sound_button["text"] = "                           Sound: ON                           "
			self.sound_button["bg"] = "Cadet Blue"
			pygame.mixer.music.play(loops=-1)
		else:
			self.sound_button["text"] = "                           Sound: OFF                          "
			self.sound_button["bg"] = "Cadet Blue"
			pygame.mixer.music.pause()

	def show_win(self):
		self.destroy()
		mode = Mode(self)
		mode.mainloop()

	def show_create(self):
		self.withdraw()
		create = Create(self)




if __name__ == "__main__":
	menu = Menu()
	menu.mainloop()

