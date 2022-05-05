from tkinter import *
from easymode import EasyMode
from advancedmode import AdvancedMode




class Create():
	def __init__(self, menu):
		self.menu = menu
		self.create = Toplevel(self.menu)
		self.create.geometry("1280x750+150+0")
		self.create.title("Mode")
		self.menu.bg = PhotoImage(file="assets/bg2.jpg")
		self.label = Label(self.create, image=menu.bg)
		self.label.place(x=0, y=0, relheight=1, relwidth=1)



		self.Nhomlbl= Label(self.create, text="                           Nhom 14:                           ", font=("arial", 25, 'bold'), bg="Cadet Blue", fg="#FBEEDF", relief=RIDGE)
		self.Nhomlbl.place(x=350, y =100)
		self.name1= Label(self.create, text="                           Tran Dinh Hieu                          ", font=("arial", 20, 'bold'), bg="Cadet Blue", fg="#FBEEDF", relief=RIDGE)
		self.name1.place(x=350, y =200)
		self.name2= Label(self.create, text="                           Tran Dinh Hieu                          ", font=("arial", 20, 'bold'), bg="Cadet Blue", fg="#FBEEDF", relief=RIDGE)
		self.name2.place(x=350, y =300)
		self.name3= Label(self.create, text="                           Tran Dinh Hieu                          ", font=("arial", 20, 'bold'), bg="Cadet Blue", fg="#FBEEDF", relief=RIDGE)
		self.name3.place(x=350, y =400)
		self.name4= Label(self.create, text="                           Tran Dinh Hieu                          ", font=("arial", 20, 'bold'), bg="Cadet Blue", fg="#FBEEDF", relief=RIDGE)
		self.name4.place(x=350, y =500)
		self.backbtn= Button(self.create, text="                           Back                          ", font=("arial", 20, 'bold'), bg="Cadet Blue", fg="#FBEEDF",command=self.back, relief=RIDGE)
		self.backbtn.place(x=350, y =600)

	def back(self):
		self.Nhomlbl.destroy()
		self.name4.destroy()
		self.name3.destroy()
		self.name2.destroy()
		self.name1.destroy()
		self.backbtn.destroy()

		self.Newgame_button = Button(self.create, text="                           New Game                           ",
		                             font=("arial", 20, 'bold'), bg="Cadet Blue", fg="#FBEEDF", command=self.menu.show_win,
		                             relief=RIDGE)
		self.Newgame_button.place(x=350, y=100)
		self.Highscore_button = Button(self.create, text="                           High Score                          ",
		                               font=("arial", 20, 'bold'), bg="Cadet Blue", fg="#FBEEDF", command=self.menu.show_win,
		                               relief=RIDGE)
		self.Highscore_button.place(x=350, y=250)
		self.sound_button = Button(self.create, text="                           Sound: OFF                          ",
		                           font=("arial", 20, 'bold'), bg="Cadet Blue", fg="#FBEEDF", command=self.menu.play,
		                           relief=RIDGE)
		self.sound_button.place(x=350, y=400)
		self.quit_button = Button(self.create, text="                                Create                                ",
		                          font=("arial", 20, 'bold'), bg="Cadet Blue", fg="#FBEEDF", command=self.menu.show_create,
		                          relief=RIDGE)
		self.quit_button.place(x=350, y=550)









