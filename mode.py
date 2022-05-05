from tkinter import *
from easymode import EasyMode
from advancedmode import AdvancedMode




class Mode(Tk):
	def __init__(self, menu ):
		super().__init__()
		self.menu = menu
		self.geometry("1280x750+150+0")
		self.title("Mode")
		self.bg = PhotoImage(file="assets/bg2.jpg")
		self.label = Label(self, image=self.bg)
		self.label.place(x=0, y=0, relheight=1, relwidth=1)



		self.Easymode_button= Button(self, text="                           Easy Mode                           ", font=("arial", 20, 'bold'), bg="Cadet Blue", fg="#FBEEDF", command= self.easymode, relief=RIDGE)
		self.Easymode_button.place(x=350, y =100)
		self.Advancedmode_button= Button(self, text="                           Advanced Mode                          ", font=("arial", 20, 'bold'), bg="Cadet Blue", fg="#FBEEDF", command= self.advancedmode, relief=RIDGE)
		self.Advancedmode_button.place(x=350, y =400)

	def easymode(self):
		self.destroy()
		easy = EasyMode(self.menu)
		easy.mainloop()

	def advancedmode(self):
		self.destroy()
		advanced = AdvancedMode()
		advanced.mainloop()





