import tkinter as tk
from tkinter import *
import random
import pygame

btnNumbers =[]
numberofClicks = 0


class EasyMode(tk.Tk):

    def __init__(self, menu):
        super().__init__()
        self.menu = menu
        # configure the root window
        self.title('Puzzle ')
        self.geometry('1200x750+150+0')
        self.configure(background="Cadet Blue")

        self.Tops = Frame(self, bg="Cadet Blue", pady=2, width=1350, height=150, relief=RIDGE)
        self.Tops.grid(row=0, column=0)
        self.lblTitle = Label(self.Tops, font=("arial", 80, 'bold'), text="   Easy Puzzle Game   ", bd=10, bg="Cadet Blue",
                         fg="Cornsilk", justify=CENTER)
        self.lblTitle.grid(row=0, column=0)

        self.MainFrame = Frame(self, bg="Powder Blue", bd=10, width=1350, height=600, relief=RIDGE)
        self.MainFrame.grid(row=1, column=0, padx=30)

        self.LeftFrame = Frame(self.MainFrame, bg="Cadet Blue", bd=10, width=500, height=500, pady=2, relief=RIDGE)
        self.LeftFrame.pack(side=LEFT)

        self.RightFrame = Frame(self.MainFrame, bg="Cadet Blue", bd=10, width=540, height=500, padx=1, pady=2, relief=RIDGE)
        self.RightFrame.pack(side=RIGHT)

        self.RightFrame1 = Frame(self.RightFrame, bg="Cadet Blue", bd=10, width=540, height=200, padx=10, pady=2, relief=RIDGE)
        self.RightFrame1.grid(row=0, column=0)

        self.RightFrame2a = Frame(self.RightFrame, bg="Cadet Blue", bd=10, width=540, height=140, padx=10, pady=2, relief=RIDGE)
        self.RightFrame2a.grid(row=1, column=0)

        self.RightFrame2b = Frame(self.RightFrame, bg="Cadet Blue", bd=10, width=540, height=140, padx=10, pady=2, relief=RIDGE)
        self.RightFrame2b.grid(row=2, column=0)


        self.highscore = 9999
        self.displayClicks = StringVar()
        self.displayClicks.set("Number of Clicks" + "\n" + "0")
        self.gameStateString = StringVar()
        self.gameStateString.set("High Score:" + str(self.highscore))
        self.slove()
        self.shuffle()

        lblDisplayClicks = Label(self.RightFrame1, textvariable=self.displayClicks, font=("arial", 40)).place(x=0, y=10, width=480, height=160)
        btnShuffle = Button(self.RightFrame2a, text="New Game", font=("arial", 37), bd=5, command=self.shuffle).pack(side=RIGHT)
        btnBack = Button(self.RightFrame2a, text="  Back  ", font=("arial", 37), bd=5, command=self.back).pack(side=LEFT)
        lblDisplayClick = Label(self.RightFrame2b, textvariable=self.gameStateString, font=("arial", 40)).place(x=0, y=10,
                                                                                                      width=480,
                                                                                                      height=100)


    def upDateCounter(self):
        global numberofClicks
        self.displayClicks.set("Number of Clicks" + "\n" + str(numberofClicks))

    def upDateHighScore(self):
        self.gameStateString.set("High Score:" + str(self.highscore))

    def gameStateUpdate(self):
        self.gameStateString.set("You are a Winner")

    def shuffle(self):
        global btnNumbers, numberofClicks
        nums = []
        for x in range(9):
            x += 1
            if x == 9:
                nums.append("")
            else:
                nums.append(str(x))

        for y in range(len(btnNumbers)):
            for x in range(len(btnNumbers[y])):
                num = random.choice(nums)
                btnNumbers[y][x].textTaken.set(num)
                nums.remove(num)
        numberofClicks = 0
        self.upDateCounter()
        self.upDateHighScore()

    def back(self):
        self.destroy()
        self.menu.mainloop()



    def slove(self):
        global btnNumbers, numberofClicks
        name = 0
        for y in range(3):
            btnNumbers_ = []
            for x in range(3):
                name += 1
                if name == 9:
                    name = ""
                btnNumbers_.append(Button_(str(name), x, y, self.LeftFrame, Function=Funtion(self)))
            btnNumbers.append(btnNumbers_)



    def winCheck(self):
        global btnNumbers, numberofClicks
        lost = False
        for y in range(len(btnNumbers)):
            for x in range(len(btnNumbers[y])):
                if btnNumbers[y][x].enterValue != btnNumbers[y][x].textTaken.get():
                    lost = True
                    break
        if not lost:
            if numberofClicks < self.highscore and numberofClicks != 0:
                self.highscore = numberofClicks
            self.upDateHighScore()
            self.gameStateUpdate()



class Button_():
    def __init__(self, text_, x, y, LeftFrame, Function):
        self.function = Function
        self.LeftFrame = LeftFrame
        self.enterValue = text_
        self.textTaken = StringVar()
        self.textTaken.set(text_)
        self.x = x
        self.y = y
        self.btnNumber = Button(self.LeftFrame, textvariable=self.textTaken, font=("arial", 80), bd=3,
                                command=lambda i=self.x, j=self.y: self.function.emptySpotChecker( i, j))
        self.btnNumber.place(x=self.x * 150, y=self.y * 150, width=170, height=170)


class Funtion():
    def __init__(self, App):
        self.app = App

    def emptySpotChecker(self, y, x):
        pygame.mixer.init()
        pygame.mixer.music.load("music/mixkit-fish-dropped-hit-2920.wav")
        pygame.mixer.music.play()

        global btnNumbers, numberofClicks
        if not btnNumbers[x][y].textTaken.get() == "":
            for i in range(-1, 2):
                newX = x + i

                if not (newX < 0 or len(btnNumbers) - 1 < newX or i == 0):
                    if btnNumbers[newX][y].textTaken.get() == "":
                        text = btnNumbers[x][y].textTaken.get()
                        btnNumbers[x][y].textTaken.set(btnNumbers[newX][y].textTaken.get())
                        btnNumbers[newX][y].textTaken.set(text)
                        self.app.winCheck()
                        break

            for j in range(-1, 2):
                newY = y + j
                if not (newY < 0 or len(btnNumbers[0]) - 1 < newY or j == 0):
                    if btnNumbers[x][newY].textTaken.get() == "":
                        text = btnNumbers[x][y].textTaken.get()
                        btnNumbers[x][y].textTaken.set(btnNumbers[x][newY].textTaken.get())
                        btnNumbers[x][newY].textTaken.set(text)
                        self.app.winCheck()
                        break
        numberofClicks += 1
        self.app.upDateCounter()


