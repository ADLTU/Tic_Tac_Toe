from tkinter import *
from tkinter import messagebox
from tkinter import font
from random import randint


class T(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.difficulty = 0
        self.configure(bg="black")
        self.grid()
        self.start_menue()
        self.click = True  # Start with X
        self.buttons = []
        # self.font = font.Font(family="Helvetica", size=9, weight="bold")
        self.plays = [0, 0, 0, 0]

    def start_game(self, diff):
        self.difficulty = diff
        # creating all the buttons
        for i in range(2, 5):
            for j in range(2, 5):
                self.buttons.append(self.create_buttons(i, j))

    def start_menue(self):
        message1 = Label(self, text=" ", fg="light grey", bg="black")
        message1.grid(row=0, column=1)
        start_message = Label(self, text="Welcome to Tic Tac Toe", fg="light grey", bg="black")
        start_message.grid(row=0, column=2)
        message = Label(self, text="select player difficulty", fg="light grey", bg="black")
        message.grid(row=1, column=4)
        button1 = Button(self, text="One Player (Easy Mode)", height=3, width=20, fg="black", bg="light grey", command=lambda: self.start_game(1))
        button1.grid(row=2, column=4)
        button2 = Button(self, text="One Player (Hard Mode)", height=3, width=20, fg="black", bg="light grey", command=lambda: self.start_game(2))
        button2.grid(row=3, column=4)
        button3 = Button(self, text="Two Players", height=3, width=20, fg="black", bg="light grey", command=lambda: self.start_game(3))
        button3.grid(row=4, column=4)

    def create_buttons(self, x, y):
        if self.difficulty == 1:
            button = Button(self, text=" ", height=3, width=20, fg="black", command=lambda: self.easy_play(button))
        if self.difficulty == 2:
            button = Button(self, text=" ", height=3, width=20, fg="black", command=lambda: self.hard_play(button))
        if self.difficulty == 3:
            button = Button(self, text=" ", height=3, width=20, fg="black", command=lambda: self.two_players(button))
        button.configure(bg="light grey")
        button.grid(row=x, column=y)
        return button

    def check(self):
        if self.buttons[0]["text"] == self.buttons[1]["text"] == self.buttons[2]["text"] != " " \
                or self.buttons[3]["text"] == self.buttons[4]["text"] == self.buttons[5]["text"] != " "\
                or self.buttons[6]["text"] == self.buttons[7]["text"] == self.buttons[8]["text"] != " "\
                or self.buttons[0]["text"] == self.buttons[3]["text"] == self.buttons[6]["text"] != " "\
                or self.buttons[1]["text"] == self.buttons[4]["text"] == self.buttons[7]["text"] != " "\
                or self.buttons[2]["text"] == self.buttons[5]["text"] == self.buttons[8]["text"] != " " \
                or self.buttons[2]["text"] == self.buttons[4]["text"] == self.buttons[6]["text"] != " " \
                or self.buttons[0]["text"] == self.buttons[4]["text"] == self.buttons[8]["text"] != " ":
            if self.click:
                messagebox.showinfo(title="Game Over", message="The winner is O !")
            else:
                messagebox.showinfo(title="Game Over", message="The winner is X !")
            sys.exit(0)
        elif self.buttons[0]["text"] != " " and self.buttons[1]["text"] != " " and self.buttons[2]["text"] != " " and\
                self.buttons[3]["text"] != " " and self.buttons[4]["text"] != " " and self.buttons[5]["text"] != " "and\
                self.buttons[6]["text"] != " " and self.buttons[7]["text"] != " " and self.buttons[8]["text"] != " ":
            messagebox.showinfo(title="Game Over", message="Draw !")
            sys.exit(0)

    def two_players(self, button1):
        if button1["text"] == " ":
            if self.click:
                button1["text"] = "X"
                self.click = False
                self.check()
            else:
                button1["text"] = "O"
                self.click = True
                self.check()

    def easy_play(self, button1):
        if button1["text"] == " ":
            if self.click:
                button1["text"] = "X"
                self.click = False
                self.check()
                x = randint(0, 8)
                while self.buttons[x]["text"] != " ":
                    x = randint(0, 8)
                self.buttons[x]["text"] = "O"
                self.click = True
                self.check()

    def hard_play(self, button1):
        if button1["text"] == " ":
            if self.click:
                button1["text"] = "X"
                self.click = False
                self.check()
                if self.plays[0] == 0:
                    if self.buttons[0]["text"] == "X" or self.buttons[2]["text"] == "X" \
                            or self.buttons[6]["text"] == "X" or self.buttons[8]["text"] == "X":
                        self.buttons[4]["text"] = "O"
                        self.plays[1] = 1
                    elif self.buttons[7]["text"] == "X":
                        self.buttons[1]["text"] = "O"
                        self.plays[1] = 2
                    elif self.buttons[5]["text"] == "X":
                        self.buttons[3]["text"] = "O"
                        self.plays[1] = 3
                    elif self.buttons[1]["text"] == "X":
                        self.buttons[7]["text"] = "O"
                        self.plays[1] = 4
                    elif self.buttons[3]["text"] == "X":
                        self.buttons[5]["text"] = "O"
                        self.plays[1] = 5
                    elif self.buttons[4]["text"] == "X":
                        self.buttons[6]["text"] = "O"
                        self.plays[1] = 6
                    self.plays[0] += 1
                    self.click = True
                elif self.plays[0] == 1:
                    if self.plays[1] == 1:
                        if self.buttons[0]["text"] == "X":
                            if self.buttons[1]["text"] == "X":
                                self.buttons[2]["text"] = "O"
                                self.plays[2] = 1
                            elif self.buttons[2]["text"] == "X":
                                self.buttons[1]["text"] = "O"
                                self.plays[2] = 2
                            elif self.buttons[3]["text"] == "X":
                                self.buttons[6]["text"] = "O"
                                self.plays[2] = 3
                            elif self.buttons[6]["text"] == "X":
                                self.buttons[3]["text"] = "O"
                                self.plays[2] = 4
                            elif self.buttons[5]["text"] == "X":
                                self.buttons[7]["text"] = "O"
                                self.plays[2] = 5
                            elif self.buttons[7]["text"] == "X":
                                self.buttons[5]["text"] = "O"
                                self.plays[2] = 6
                            elif self.buttons[8]["text"] == "X":
                                self.buttons[3]["text"] = "O"
                                self.plays[2] = 7
                        elif self.buttons[2]["text"] == "X":
                            if self.buttons[1]["text"] == "X":
                                self.buttons[0]["text"] = "O"
                                self.plays[2] = 8
                            elif self.buttons[0]["text"] == "X":
                                self.buttons[1]["text"] = "O"
                                self.plays[2] = 9
                            elif self.buttons[3]["text"] == "X":
                                self.buttons[7]["text"] = "O"
                                self.plays[2] = 10
                            elif self.buttons[7]["text"] == "X":
                                self.buttons[3]["text"] = "O"
                                self.plays[2] = 11
                            elif self.buttons[8]["text"] == "X":
                                self.buttons[5]["text"] = "O"
                                self.plays[2] = 12
                            elif self.buttons[5]["text"] == "X":
                                self.buttons[8]["text"] = "O"
                                self.plays[2] = 13
                            elif self.buttons[6]["text"] == "X":
                                self.buttons[3]["text"] = "O"
                                self.plays[2] = 14
                        elif self.buttons[6]["text"] == "X":
                            if self.buttons[3]["text"] == "X":
                                self.buttons[0]["text"] = "O"
                                self.plays[2] = 15
                            elif self.buttons[0]["text"] == "X":
                                self.buttons[3]["text"] = "O"
                                self.plays[2] = 16
                            elif self.buttons[8]["text"] == "X":
                                self.buttons[7]["text"] = "O"
                                self.plays[2] = 17
                            elif self.buttons[7]["text"] == "X":
                                self.buttons[8]["text"] = "O"
                                self.plays[2] = 18
                            elif self.buttons[1]["text"] == "X":
                                self.buttons[5]["text"] = "O"
                                self.plays[2] = 19
                            elif self.buttons[5]["text"] == "X":
                                self.buttons[1]["text"] = "O"
                                self.plays[2] = 20
                            elif self.buttons[2]["text"] == "X":
                                self.buttons[3]["text"] = "O"
                                self.plays[2] = 21
                        elif self.buttons[8]["text"] == "X":
                            if self.buttons[2]["text"] == "X":
                                self.buttons[5]["text"] = "O"
                                self.plays[2] = 22
                            elif self.buttons[5]["text"] == "X":
                                self.buttons[2]["text"] = "O"
                                self.plays[2] = 23
                            elif self.buttons[6]["text"] == "X":
                                self.buttons[7]["text"] = "O"
                                self.plays[2] = 24
                            elif self.buttons[7]["text"] == "X":
                                self.buttons[6]["text"] = "O"
                                self.plays[2] = 25
                            elif self.buttons[1]["text"] == "X":
                                self.buttons[3]["text"] = "O"
                                self.plays[2] = 26
                            elif self.buttons[3]["text"] == "X":
                                self.buttons[1]["text"] = "O"
                                self.plays[2] = 27
                            elif self.buttons[0]["text"] == "X":
                                self.buttons[5]["text"] = "O"
                                self.plays[2] = 28
                        # self.plays[0] += 1
                        # self.click = True
                    elif self.plays[1] == 2:
                        if self.buttons[2]["text"] == "X" or self.buttons[5]["text"] == "X" \
                                or self.buttons[6]["text"] == "X":
                            self.buttons[8]["text"] = "O"
                            self.plays[2] = 29
                        else:
                            self.buttons[6]["text"] = "O"
                            self.plays[2] = 30
                        # self.plays[0] += 1
                        # self.click = True
                    elif self.plays[1] == 3:
                        if self.buttons[6]["text"] == "X" or self.buttons[7]["text"] == "X" \
                                    or self.buttons[2]["text"] == "X":
                            self.buttons[8]["text"] = "O"
                            self.plays[2] = 31
                        else:
                            self.buttons[2]["text"] = "O"
                            self.plays[2] = 32
                        # self.plays[0] += 1
                        # self.click = True
                    elif self.plays[1] == 4:
                        if self.buttons[8]["text"] == "X" or self.buttons[5]["text"] == "X" \
                                    or self.buttons[0]["text"] == "X":
                            self.buttons[2]["text"] = "O"
                            self.plays[2] = 33
                        else:
                            self.buttons[0]["text"] = "O"
                            self.plays[2] = 34
                        # self.plays[0] += 1
                        # self.click = True
                    elif self.plays[1] == 5:
                        if self.buttons[8]["text"] == "X" or self.buttons[7]["text"] == "X" \
                                or self.buttons[0]["text"] == "X":
                            self.buttons[6]["text"] = "O"
                            self.plays[2] = 35
                        else:
                            self.buttons[0]["text"] = "O"
                            self.plays[2] = 36
                        # self.plays[0] += 1
                        # self.click = True
                    elif self.plays[1] == 6:
                        if self.buttons[0]["text"] == "X":
                            self.buttons[8]["text"] = "O"
                            self.plays[2] = 37
                        elif self.buttons[1]["text"] == "X":
                            self.buttons[7]["text"] = "O"
                            self.plays[2] = 38
                        elif self.buttons[3]["text"] == "X":
                            self.buttons[5]["text"] = "O"
                            self.plays[2] = 39
                        elif self.buttons[5]["text"] == "X":
                            self.buttons[3]["text"] = "O"
                            self.plays[2] = 40
                        elif self.buttons[7]["text"] == "X":
                            self.buttons[1]["text"] = "O"
                            self.plays[2] = 41
                        elif self.buttons[8]["text"] == "X":
                            self.buttons[0]["text"] = "O"
                            self.plays[2] = 42
                        elif self.buttons[2]["text"] == "X":
                            self.buttons[8]["text"] = "O"
                            self.plays[2] = 43
                        # self.plays[0] += 1
                        # self.click = True
                    self.plays[0] += 1
                    self.click = True
                elif self.plays[0] == 2:
                    if self.plays[2] == 1:
                        if self.buttons[6]["text"] != "X":
                            self.buttons[6]["text"] = "O"
                        else:
                            self.buttons[3]["text"] = "O"
                            self.plays[3] = 1
                    elif self.plays[2] == 2:
                        if self.buttons[7]["text"] != "X":
                            self.buttons[7]["text"] = "O"
                        else:
                            self.buttons[6]["text"] = "O"
                            self.plays[3] = 2
                    elif self.plays[2] == 3:
                        if self.buttons[2]["text"] != "X":
                            self.buttons[2]["text"] = "O"
                        else:
                            self.buttons[1]["text"] = "O"
                            self.plays[3] = 3
                    elif self.plays[2] == 4:
                        if self.buttons[5]["text"] != "X":
                            self.buttons[5]["text"] = "O"
                        else:
                            self.buttons[2]["text"] = "O"
                            self.plays[3] = 4
                    elif self.plays[2] == 5:
                        if self.buttons[1]["text"] != "X":
                            self.buttons[1]["text"] = "O"
                        else:
                            self.buttons[2]["text"] = "O"
                            self.plays[3] = 5
                    elif self.plays[2] == 6:
                        if self.buttons[3]["text"] != "X":
                            self.buttons[3]["text"] = "O"
                        else:
                            self.buttons[6]["text"] = "O"
                            self.plays[3] = 6
                    elif self.plays[2] == 7:
                        if self.buttons[5]["text"] != "X":
                            self.buttons[5]["text"] = "O"
                        else:
                            self.buttons[2]["text"] = "O"
                            self.plays[3] = 7
                    elif self.plays[2] == 8:
                        if self.buttons[8]["text"] != "X":
                            self.buttons[8]["text"] = "O"
                        else:
                            self.buttons[5]["text"] = "O"
                            self.plays[3] = 8
                    elif self.plays[2] == 9:
                        if self.buttons[7]["text"] != "X":
                            self.buttons[7]["text"] = "O"
                        else:
                            self.buttons[3]["text"] = "O"
                            self.plays[3] = 9
                    elif self.plays[2] == 10:
                        if self.buttons[1]["text"] != "X":
                            self.buttons[1]["text"] = "O"
                        else:
                            self.buttons[0]["text"] = "O"
                            self.plays[3] = 10
                    elif self.plays[2] == 11:
                        if self.buttons[5]["text"] != "X":
                            self.buttons[5]["text"] = "O"
                        else:
                            self.buttons[8]["text"] = "O"
                            self.plays[3] = 11
                    elif self.plays[2] == 12:
                        if self.buttons[3]["text"] != "X":
                            self.buttons[3]["text"] = "O"
                        else:
                            self.buttons[0]["text"] = "O"
                            self.plays[3] = 12
                    elif self.plays[2] == 13:
                        if self.buttons[0]["text"] != "X":
                            self.buttons[0]["text"] = "O"
                        else:
                            self.buttons[1]["text"] = "O"
                            self.plays[3] = 13
                    elif self.plays[2] == 14:
                        if self.buttons[5]["text"] != "X":
                            self.buttons[5]["text"] = "O"
                        else:
                            self.buttons[8]["text"] = "O"
                            self.plays[3] = 14
                    elif self.plays[2] == 15:
                        if self.buttons[8]["text"] != "X":
                            self.buttons[8]["text"] = "O"
                        else:
                            self.buttons[7]["text"] = "O"
                            self.plays[3] = 15
                    elif self.plays[2] == 16:
                        if self.buttons[5]["text"] != "X":
                            self.buttons[5]["text"] = "O"
                        else:
                            self.buttons[2]["text"] = "O"
                            self.plays[3] = 16
                    elif self.plays[2] == 17:
                        if self.buttons[1]["text"] != "X":
                            self.buttons[1]["text"] = "O"
                        else:
                            self.buttons[0]["text"] = "O"
                            self.plays[3] = 17
                    elif self.plays[2] == 18:
                        if self.buttons[0]["text"] != "X":
                            self.buttons[0]["text"] = "O"
                        else:
                            self.buttons[3]["text"] = "O"
                            self.plays[3] = 18
                    elif self.plays[2] == 19:
                        if self.buttons[3]["text"] != "X":
                            self.buttons[3]["text"] = "O"
                        else:
                            self.buttons[0]["text"] = "O"
                            self.plays[3] = 19
                    elif self.plays[2] == 20:
                        if self.buttons[7]["text"] != "X":
                            self.buttons[7]["text"] = "O"
                        else:
                            self.buttons[8]["text"] = "O"
                            self.plays[3] = 20
                    elif self.plays[2] == 21:
                        if self.buttons[5]["text"] != "X":
                            self.buttons[5]["text"] = "O"
                        else:
                            self.buttons[8]["text"] = "O"
                            self.plays[3] = 21
                    elif self.plays[2] == 22:
                        if self.buttons[3]["text"] != "X":
                            self.buttons[3]["text"] = "O"
                        else:
                            self.buttons[0]["text"] = "O"
                            self.plays[3] = 22
                    elif self.plays[2] == 23:
                        if self.buttons[6]["text"] != "X":
                            self.buttons[6]["text"] = "O"
                        else:
                            self.buttons[7]["text"] = "O"
                            self.plays[3] = 23
                    elif self.plays[2] == 24:
                        if self.buttons[1]["text"] != "X":
                            self.buttons[1]["text"] = "O"
                        else:
                            self.buttons[0]["text"] = "O"
                            self.plays[3] = 24
                    elif self.plays[2] == 25:
                        if self.buttons[2]["text"] != "X":
                            self.buttons[2]["text"] = "O"
                        else:
                            self.buttons[5]["text"] = "O"
                            self.plays[3] = 25
                    elif self.plays[2] == 26:
                        if self.buttons[5]["text"] != "X":
                            self.buttons[5]["text"] = "O"
                        else:
                            self.buttons[2]["text"] = "O"
                            self.plays[3] = 26
                    elif self.plays[2] == 27:
                        if self.buttons[7]["text"] != "X":
                            self.buttons[7]["text"] = "O"
                        else:
                            self.buttons[6]["text"] = "O"
                            self.plays[3] = 27
                    elif self.plays[2] == 28:
                        if self.buttons[3]["text"] != "X":
                            self.buttons[3]["text"] = "O"
                        else:
                            self.buttons[6]["text"] = "O"
                            self.plays[3] = 28
                    elif self.plays[2] == 29:
                        if self.buttons[2]["text"] == "X":
                            if self.buttons[4]["text"] != "X":
                                self.buttons[4]["text"] = "O"
                                self.plays[3] = 29
                            else:
                                self.buttons[6]["text"] = "O"
                                self.plays[3] = 30
                        elif self.buttons[5]["text"] == "X":
                            if self.buttons[4]["text"] != "X":
                                self.buttons[4]["text"] = "O"
                                self.plays[3] = 31
                            else:
                                self.buttons[3]["text"] = "O"
                                self.plays[3] = 32
                        elif self.buttons[6]["text"] == "X":
                                if self.buttons[4]["text"] == "X":
                                    self.buttons[2]["text"] = "O"
                                    self.plays[3] = 33
                                elif self.buttons[2]["text"] == "X":
                                    self.buttons[4]["text"] = "O"
                                    self.plays[3] = 34
                                elif self.buttons[3]["text"] == "X":
                                    self.buttons[0]["text"] = "O"
                                    self.plays[3] = 35
                                elif self.buttons[0]["text"] == "X":
                                    self.buttons[3]["text"] = "O"
                                    self.plays[3] = 36
                    elif self.plays[2] == 30:
                        if self.buttons[0]["text"] == "X":
                            if self.buttons[4]["text"] != "X":
                                self.buttons[4]["text"] = "O"
                                self.plays[3] = 37
                            else:
                                self.buttons[8]["text"] = "O"
                                self.plays[3] = 38
                        elif self.buttons[3]["text"] == "X":
                            if self.buttons[4]["text"] != "X":
                                self.buttons[4]["text"] = "O"
                                self.plays[3] = 39
                            else:
                                self.buttons[5]["text"] = "O"
                                self.plays[3] = 40
                        elif self.buttons[4]["text"] == "X":
                                if self.buttons[5]["text"] == "X":
                                    self.buttons[3]["text"] = "O"
                                    self.plays[3] = 41
                                elif self.buttons[3]["text"] == "X":
                                    self.buttons[5]["text"] = "O"
                                    self.plays[3] = 42
                                elif self.buttons[8]["text"] == "X":
                                    self.buttons[0]["text"] = "O"
                                    self.plays[3] = 43
                                elif self.buttons[0]["text"] == "X":
                                    self.buttons[8]["text"] = "O"
                                    self.plays[3] = 44
                                elif self.buttons[2]["text"] == "X":  # forgot it so i add it late
                                    self.buttons[0]["text"] = "O"
                                    self.plays[3] = 124
                        elif self.buttons[8]["text"] == "X":
                                if self.buttons[4]["text"] == "X":
                                    self.buttons[0]["text"] = "O"
                                    self.plays[3] = 45
                                elif self.buttons[0]["text"] == "X":
                                    self.buttons[4]["text"] = "O"
                                    self.plays[3] = 46
                                elif self.buttons[5]["text"] == "X":
                                    self.buttons[2]["text"] = "O"
                                    self.plays[3] = 47
                                elif self.buttons[2]["text"] == "X":
                                    self.buttons[5]["text"] = "O"
                                    self.plays[3] = 48
                    elif self.plays[2] == 31:
                        if self.buttons[6]["text"] == "X":
                            if self.buttons[4]["text"] != "X":
                                self.buttons[4]["text"] = "O"
                                self.plays[3] = 49
                            else:
                                self.buttons[2]["text"] = "O"
                                self.plays[3] = 50
                        elif self.buttons[7]["text"] == "X":
                            if self.buttons[4]["text"] != "X":
                                self.buttons[4]["text"] = "O"
                                self.plays[3] = 51
                            else:
                                self.buttons[1]["text"] = "O"
                                self.plays[3] = 52
                        elif self.buttons[2]["text"] == "X":
                                if self.buttons[4]["text"] == "X":
                                    self.buttons[6]["text"] = "O"
                                    self.plays[3] = 53
                                elif self.buttons[6]["text"] == "X":
                                    self.buttons[4]["text"] = "O"
                                    self.plays[3] = 54
                                elif self.buttons[1]["text"] == "X":
                                    self.buttons[0]["text"] = "O"
                                    self.plays[3] = 55
                                elif self.buttons[0]["text"] == "X":
                                    self.buttons[1]["text"] = "O"
                                    self.plays[3] = 56
                    elif self.plays[2] == 32:
                        if self.buttons[0]["text"] == "X":
                            if self.buttons[4]["text"] != "X":
                                self.buttons[4]["text"] = "O"
                                self.plays[3] = 57
                            else:
                                self.buttons[8]["text"] = "O"
                                self.plays[3] = 58
                        elif self.buttons[1]["text"] == "X":
                            if self.buttons[4]["text"] != "X":
                                self.buttons[4]["text"] = "O"
                                self.plays[3] = 59
                            else:
                                self.buttons[7]["text"] = "O"
                                self.plays[3] = 60
                        elif self.buttons[4]["text"] == "X":
                                if self.buttons[7]["text"] == "X":
                                    self.buttons[1]["text"] = "O"
                                    self.plays[3] = 61
                                elif self.buttons[1]["text"] == "X":
                                    self.buttons[7]["text"] = "O"
                                    self.plays[3] = 62
                                elif self.buttons[8]["text"] == "X":
                                    self.buttons[0]["text"] = "O"
                                    self.plays[3] = 63
                                elif self.buttons[0]["text"] == "X":
                                    self.buttons[8]["text"] = "O"
                                    self.plays[3] = 64
                                elif self.buttons[6]["text"] == "X":
                                    self.buttons[0]["text"] = "O"
                                    self.plays[3] = 125  # added late
                        elif self.buttons[8]["text"] == "X":
                                if self.buttons[4]["text"] == "X":
                                    self.buttons[0]["text"] = "O"
                                    self.plays[3] = 65
                                elif self.buttons[0]["text"] == "X":
                                    self.buttons[4]["text"] = "O"
                                    self.plays[3] = 66
                                elif self.buttons[6]["text"] == "X":
                                    self.buttons[7]["text"] = "O"
                                    self.plays[3] = 67
                                elif self.buttons[7]["text"] == "X":
                                    self.buttons[6]["text"] = "O"
                                    self.plays[3] = 68
                    elif self.plays[2] == 33:
                        if self.buttons[5]["text"] == "X":
                            if self.buttons[4]["text"] != "X":
                                self.buttons[4]["text"] = "O"
                                self.plays[3] = 69
                            else:
                                self.buttons[3]["text"] = "O"
                                self.plays[3] = 70
                        elif self.buttons[8]["text"] == "X":
                            if self.buttons[4]["text"] != "X":
                                self.buttons[4]["text"] = "O"
                                self.plays[3] = 71
                            else:
                                self.buttons[0]["text"] = "O"
                                self.plays[3] = 72
                        elif self.buttons[0]["text"] == "X":
                                if self.buttons[4]["text"] == "X":
                                    self.buttons[8]["text"] = "O"
                                    self.plays[3] = 73
                                elif self.buttons[8]["text"] == "X":
                                    self.buttons[4]["text"] = "O"
                                    self.plays[3] = 74
                                elif self.buttons[3]["text"] == "X":
                                    self.buttons[6]["text"] = "O"
                                    self.plays[3] = 75
                                elif self.buttons[6]["text"] == "X":
                                    self.buttons[3]["text"] = "O"
                                    self.plays[3] = 76
                    elif self.plays[2] == 34:
                        if self.buttons[3]["text"] == "X":
                            if self.buttons[4]["text"] != "X":
                                self.buttons[4]["text"] = "O"
                                self.plays[3] = 77
                            else:
                                self.buttons[5]["text"] = "O"
                                self.plays[3] = 78
                        elif self.buttons[6]["text"] == "X":
                            if self.buttons[4]["text"] != "X":
                                self.buttons[4]["text"] = "O"
                                self.plays[3] = 79
                            else:
                                self.buttons[2]["text"] = "O"
                                self.plays[3] = 80
                        elif self.buttons[2]["text"] == "X":
                                if self.buttons[4]["text"] == "X":
                                    self.buttons[6]["text"] = "O"
                                    self.plays[3] = 81
                                elif self.buttons[6]["text"] == "X":
                                    self.buttons[4]["text"] = "O"
                                    self.plays[3] = 82
                                elif self.buttons[8]["text"] == "X":
                                    self.buttons[5]["text"] = "O"
                                    self.plays[3] = 83
                                elif self.buttons[5]["text"] == "X":
                                    self.buttons[8]["text"] = "O"
                                    self.plays[3] = 84
                        elif self.buttons[4]["text"] == "X":
                                if self.buttons[2]["text"] == "X":
                                    self.buttons[6]["text"] = "O"
                                    self.plays[3] = 85
                                elif self.buttons[6]["text"] == "X":
                                    self.buttons[2]["text"] = "O"
                                    self.plays[3] = 86
                                elif self.buttons[5]["text"] == "X":
                                    self.buttons[3]["text"] = "O"
                                    self.plays[3] = 87
                                elif self.buttons[3]["text"] == "X":
                                    self.buttons[5]["text"] = "O"
                                    self.plays[3] = 88
                                elif self.buttons[8]["text"] == "X":
                                    self.buttons[6]["text"] = "O"
                                    self.plays[3] = 126  # added late
                    elif self.plays[2] == 35:
                        if self.buttons[7]["text"] == "X":
                            if self.buttons[4]["text"] != "X":
                                self.buttons[4]["text"] = "O"
                                self.plays[3] = 89
                            else:
                                self.buttons[1]["text"] = "O"
                                self.plays[3] = 90
                        elif self.buttons[8]["text"] == "X":
                            if self.buttons[4]["text"] != "X":
                                self.buttons[4]["text"] = "O"
                                self.plays[3] = 91
                            else:
                                self.buttons[0]["text"] = "O"
                                self.plays[3] = 92
                        elif self.buttons[0]["text"] == "X":
                                if self.buttons[4]["text"] == "X":
                                    self.buttons[8]["text"] = "O"
                                    self.plays[3] = 93
                                elif self.buttons[8]["text"] == "X":
                                    self.buttons[4]["text"] = "O"
                                    self.plays[3] = 94
                                elif self.buttons[1]["text"] == "X":
                                    self.buttons[2]["text"] = "O"
                                    self.plays[3] = 95
                                elif self.buttons[2]["text"] == "X":
                                    self.buttons[1]["text"] = "O"
                                    self.plays[3] = 96
                    elif self.plays[2] == 36:
                        if self.buttons[1]["text"] == "X":
                            if self.buttons[4]["text"] != "X":
                                self.buttons[4]["text"] = "O"
                                self.plays[3] = 97
                            else:
                                self.buttons[7]["text"] = "O"
                                self.plays[3] = 98
                        elif self.buttons[2]["text"] == "X":
                            if self.buttons[4]["text"] != "X":
                                self.buttons[4]["text"] = "O"
                                self.plays[3] = 99
                            else:
                                self.buttons[6]["text"] = "O"
                                self.plays[3] = 100
                        elif self.buttons[4]["text"] == "X":
                                if self.buttons[2]["text"] == "X":
                                    self.buttons[6]["text"] = "O"
                                    self.plays[3] = 101
                                elif self.buttons[6]["text"] == "X":
                                    self.buttons[2]["text"] = "O"
                                    self.plays[3] = 102
                                elif self.buttons[7]["text"] == "X":
                                    self.buttons[1]["text"] = "O"
                                    self.plays[3] = 103
                                elif self.buttons[1]["text"] == "X":
                                    self.buttons[7]["text"] = "O"
                                    self.plays[3] = 104
                                elif self.buttons[8]["text"] == "X":
                                    self.buttons[2]["text"] = "O"
                                    self.plays[3] = 127  # added late
                        elif self.buttons[6]["text"] == "X":
                                if self.buttons[4]["text"] == "X":
                                    self.buttons[2]["text"] = "O"
                                    self.plays[3] = 105
                                elif self.buttons[2]["text"] == "X":
                                    self.buttons[4]["text"] = "O"
                                    self.plays[3] = 106
                                elif self.buttons[7]["text"] == "X":
                                    self.buttons[8]["text"] = "O"
                                    self.plays[3] = 107
                                elif self.buttons[8]["text"] == "X":
                                    self.buttons[7]["text"] = "O"
                                    self.plays[3] = 108
                    elif self.plays[2] == 37:
                        if self.buttons[7]["text"] != "X":
                            self.buttons[7]["text"] = "O"
                        else:
                            self.buttons[1]["text"] = "O"
                            self.plays[3] = 109
                    elif self.plays[2] == 38:
                        if self.buttons[8]["text"] != "X":
                            self.buttons[8]["text"] = "O"
                        else:
                            self.buttons[0]["text"] = "O"
                            self.plays[3] = 110
                    elif self.plays[2] == 39:
                        if self.buttons[1]["text"] == "X":
                            self.buttons[7]["text"] = "O"
                            self.plays[3] = 111
                        elif self.buttons[2]["text"] == "X":
                            self.buttons[7]["text"] = "O"
                            self.plays[3] = 112
                        elif self.buttons[7]["text"] == "X":
                            self.buttons[1]["text"] = "O"
                            self.plays[3] = 113
                        elif self.buttons[0]["text"] == "X":
                            self.buttons[8]["text"] = "O"
                            self.plays[3] = 114
                        elif self.buttons[8]["text"] == "X":
                            self.buttons[0]["text"] = "O"
                            self.plays[3] = 115
                    elif self.plays[2] == 40:
                        if self.buttons[0]["text"] != "X":
                            self.buttons[0]["text"] = "O"
                        else:
                            self.buttons[8]["text"] = "O"
                            self.plays[3] = 116
                    elif self.plays[2] == 41:
                        if self.buttons[5]["text"] == "X":
                            self.buttons[3]["text"] = "O"
                            self.plays[3] = 117
                        elif self.buttons[2]["text"] == "X":
                            self.buttons[3]["text"] = "O"
                            self.plays[3] = 118
                        elif self.buttons[3]["text"] == "X":
                            self.buttons[5]["text"] = "O"
                            self.plays[3] = 119
                        elif self.buttons[0]["text"] == "X":
                            self.buttons[8]["text"] = "O"
                            self.plays[3] = 120
                        elif self.buttons[8]["text"] == "X":
                            self.buttons[0]["text"] = "O"
                            self.plays[3] = 121
                    elif self.plays[2] == 42:
                        if self.buttons[3]["text"] != "X":
                            self.buttons[3]["text"] = "O"
                        else:
                            self.buttons[5]["text"] = "O"
                            self.plays[3] = 122
                    elif self.plays[2] == 43:
                        if self.buttons[7]["text"] != "X":
                            self.buttons[7]["text"] = "O"
                        else:
                            self.buttons[1]["text"] = "O"
                            self.plays[3] = 123
                    self.plays[0] += 1
                    self.click = True
                    self.check()
                elif self.plays[0] == 3:
                    if self.plays[3] == 1:
                        if self.buttons[5]["text"] != "X":
                            self.buttons[5]["text"] = "O"
                        else:
                            self.buttons[8]["text"] = "O"
                    elif self.plays[3] == 2:
                        if self.buttons[5]["text"] != "X":
                            self.buttons[5]["text"] = "O"
                        else:
                            self.buttons[8]["text"] = "O"
                    elif self.plays[3] == 9:
                        if self.buttons[5]["text"] != "X":
                            self.buttons[5]["text"] = "O"
                        else:
                            self.buttons[8]["text"] = "O"
                    elif self.plays[3] == 3:
                        if self.buttons[7]["text"] != "X":
                            self.buttons[7]["text"] = "O"
                        else:
                            self.buttons[8]["text"] = "O"
                    elif self.plays[3] == 4:
                        if self.buttons[7]["text"] != "X":
                            self.buttons[7]["text"] = "O"
                        else:
                            self.buttons[8]["text"] = "O"
                    elif self.plays[3] == 16:
                        if self.buttons[7]["text"] != "X":
                            self.buttons[7]["text"] = "O"
                        else:
                            self.buttons[8]["text"] = "O"
                    elif self.plays[3] == 5:
                        if self.buttons[6]["text"] != "X":
                            self.buttons[6]["text"] = "O"
                        else:
                            self.buttons[3]["text"] = "O"
                    elif self.plays[3] == 6:
                        if self.buttons[2]["text"] != "X":
                            self.buttons[2]["text"] = "O"
                        else:
                            self.buttons[1]["text"] = "O"
                    elif self.plays[3] == 28:
                        if self.buttons[2]["text"] != "X":
                            self.buttons[2]["text"] = "O"
                        else:
                            self.buttons[1]["text"] = "O"
                    elif self.plays[3] == 7:
                        if self.buttons[6]["text"] != "X":
                            self.buttons[6]["text"] = "O"
                        else:
                            self.buttons[7]["text"] = "O"
                    elif self.plays[3] == 26:
                        if self.buttons[6]["text"] != "X":
                            self.buttons[6]["text"] = "O"
                        else:
                            self.buttons[7]["text"] = "O"
                    elif self.plays[3] == 8:
                        if self.buttons[3]["text"] != "X":
                            self.buttons[3]["text"] = "O"
                        else:
                            self.buttons[6]["text"] = "O"
                    elif self.plays[3] == 10:
                        if self.buttons[8]["text"] != "X":
                            self.buttons[8]["text"] = "O"
                        else:
                            self.buttons[5]["text"] = "O"
                    elif self.plays[3] == 11:
                        if self.buttons[0]["text"] != "X":
                            self.buttons[0]["text"] = "O"
                        else:
                            self.buttons[1]["text"] = "O"
                    elif self.plays[3] == 14:
                        if self.buttons[0]["text"] != "X":
                            self.buttons[0]["text"] = "O"
                        else:
                            self.buttons[1]["text"] = "O"
                    elif self.plays[3] == 21:
                        if self.buttons[0]["text"] != "X":
                            self.buttons[0]["text"] = "O"
                        else:
                            self.buttons[1]["text"] = "O"
                    elif self.plays[3] == 12:
                        if self.buttons[7]["text"] != "X":
                            self.buttons[7]["text"] = "O"
                        else:
                            self.buttons[6]["text"] = "O"
                    elif self.plays[3] == 13:
                        if self.buttons[7]["text"] != "X":
                            self.buttons[7]["text"] = "O"
                        else:
                            self.buttons[6]["text"] = "O"
                    elif self.plays[3] == 22:
                        if self.buttons[7]["text"] != "X":
                            self.buttons[7]["text"] = "O"
                        else:
                            self.buttons[6]["text"] = "O"
                    elif self.plays[3] == 15:
                        if self.buttons[1]["text"] != "X":
                            self.buttons[1]["text"] = "O"
                        else:
                            self.buttons[5]["text"] = "O"
                    elif self.plays[3] == 17:
                        if self.buttons[5]["text"] != "X":
                            self.buttons[5]["text"] = "O"
                        else:
                            self.buttons[2]["text"] = "O"
                    elif self.plays[3] == 18:
                        if self.buttons[5]["text"] != "X":
                            self.buttons[5]["text"] = "O"
                        else:
                            self.buttons[2]["text"] = "O"
                    elif self.plays[3] == 24:
                        if self.buttons[5]["text"] != "X":
                            self.buttons[5]["text"] = "O"
                        else:
                            self.buttons[2]["text"] = "O"
                    elif self.plays[3] == 19:
                        if self.buttons[8]["text"] != "X":
                            self.buttons[8]["text"] = "O"
                        else:
                            self.buttons[7]["text"] = "O"
                    elif self.plays[3] == 20:
                        if self.buttons[0]["text"] != "X":
                            self.buttons[0]["text"] = "O"
                        else:
                            self.buttons[3]["text"] = "O"
                    elif self.plays[3] == 23:
                        if self.buttons[1]["text"] != "X":
                            self.buttons[1]["text"] = "O"
                        else:
                            self.buttons[0]["text"] = "O"
                    elif self.plays[3] == 25:
                        if self.buttons[3]["text"] != "X":
                            self.buttons[3]["text"] = "O"
                        else:
                            self.buttons[1]["text"] = "O"
                    elif self.plays[3] == 27:
                        if self.buttons[2]["text"] != "X":
                            self.buttons[2]["text"] = "O"
                        else:
                            self.buttons[5]["text"] = "O"
                    elif self.plays[3] == 29:
                        if self.buttons[0]["text"] != "X":
                            self.buttons[0]["text"] = "O"
                        elif self.buttons[3]["text"] != "X":
                            self.buttons[3]["text"] = "O"
                        elif self.buttons[6]["text"] != "X":
                            self.buttons[6]["text"] = "O"
                    elif self.plays[3] == 30:
                        if self.buttons[5]["text"] != "X":
                            self.buttons[5]["text"] = "O"
                        else:
                            self.buttons[3]["text"] = "O"
                    elif self.plays[3] == 31:
                        if self.buttons[0]["text"] != "X":
                            self.buttons[0]["text"] = "O"
                        elif self.buttons[3]["text"] != "X":
                            self.buttons[3]["text"] = "O"
                        elif self.buttons[6]["text"] != "X":
                            self.buttons[6]["text"] = "O"
                    elif self.plays[3] == 32:
                        if self.buttons[2]["text"] != "X":
                            self.buttons[2]["text"] = "O"
                        else:
                            self.buttons[6]["text"] = "O"
                    elif self.plays[3] == 33:
                        if self.buttons[5]["text"] != "X":
                            self.buttons[5]["text"] = "O"
                        else:
                            self.buttons[3]["text"] = "O"
                    elif self.plays[3] == 34:
                        if self.buttons[0]["text"] != "X":
                            self.buttons[0]["text"] = "O"
                        else:
                            self.buttons[3]["text"] = "O"
                    elif self.plays[3] == 35:
                        if self.buttons[2]["text"] != "X":
                            self.buttons[2]["text"] = "O"
                        else:
                            self.buttons[4]["text"] = "O"
                    elif self.plays[3] == 36:
                        if self.buttons[4]["text"] != "X":
                            self.buttons[4]["text"] = "O"
                        else:
                            self.buttons[2]["text"] = "O"
                    elif self.plays[3] == 37:
                        if self.buttons[2]["text"] != "X":
                            self.buttons[2]["text"] = "O"
                        elif self.buttons[5]["text"] != "X":
                            self.buttons[5]["text"] = "O"
                        elif self.buttons[8]["text"] != "X":
                            self.buttons[8]["text"] = "O"
                    elif self.plays[3] == 38:
                        if self.buttons[5]["text"] != "X":
                            self.buttons[5]["text"] = "O"
                        else:
                            self.buttons[3]["text"] = "O"
                    elif self.plays[3] == 39:
                        if self.buttons[2]["text"] != "X":
                            self.buttons[2]["text"] = "O"
                        elif self.buttons[5]["text"] != "X":
                            self.buttons[5]["text"] = "O"
                        elif self.buttons[8]["text"] != "X":
                            self.buttons[8]["text"] = "O"
                    elif self.plays[3] == 40:
                        if self.buttons[8]["text"] != "X":
                            self.buttons[8]["text"] = "O"
                        else:
                            self.buttons[0]["text"] = "O"
                    elif self.plays[3] == 41:
                        if self.buttons[0]["text"] != "X":
                            self.buttons[0]["text"] = "O"
                        else:
                            self.buttons[8]["text"] = "O"
                    elif self.plays[3] == 42:
                        if self.buttons[0]["text"] != "X":
                            self.buttons[0]["text"] = "O"
                        else:
                            self.buttons[8]["text"] = "O"
                    elif self.plays[3] == 43:
                        if self.buttons[3]["text"] != "X":
                            self.buttons[3]["text"] = "O"
                        else:
                            self.buttons[2]["text"] = "O"
                    elif self.plays[3] == 44:
                        if self.buttons[5]["text"] != "X":
                            self.buttons[5]["text"] = "O"
                        else:
                            self.buttons[3]["text"] = "O"
                    elif self.plays[3] == 45:
                        if self.buttons[3]["text"] != "X":
                            self.buttons[3]["text"] = "O"
                        else:
                            self.buttons[2]["text"] = "O"
                    elif self.plays[3] == 46:
                        if self.buttons[5]["text"] != "X":
                            self.buttons[5]["text"] = "O"
                        else:
                            self.buttons[3]["text"] = "O"
                    elif self.plays[3] == 47:
                        if self.buttons[0]["text"] != "X":
                            self.buttons[0]["text"] = "O"
                        else:
                            self.buttons[4]["text"] = "O"
                    elif self.plays[3] == 48:
                        if self.buttons[4]["text"] != "X":
                            self.buttons[4]["text"] = "O"
                        else:
                            self.buttons[0]["text"] = "O"
                    elif self.plays[3] == 49:
                        if self.buttons[2]["text"] != "X":
                            self.buttons[2]["text"] = "O"
                        elif self.buttons[0]["text"] != "X":
                            self.buttons[0]["text"] = "O"
                        elif self.buttons[1]["text"] != "X":
                            self.buttons[1]["text"] = "O"
                    elif self.plays[3] == 50:
                        if self.buttons[1]["text"] != "X":
                            self.buttons[1]["text"] = "O"
                        else:
                            self.buttons[7]["text"] = "O"
                    elif self.plays[3] == 51:
                        if self.buttons[2]["text"] != "X":
                            self.buttons[2]["text"] = "O"
                        elif self.buttons[0]["text"] != "X":
                            self.buttons[0]["text"] = "O"
                        elif self.buttons[1]["text"] != "X":
                            self.buttons[1]["text"] = "O"
                    elif self.plays[3] == 52:
                        if self.buttons[2]["text"] != "X":
                            self.buttons[2]["text"] = "O"
                        else:
                            self.buttons[6]["text"] = "O"
                    elif self.plays[3] == 53:
                        if self.buttons[0]["text"] != "X":
                            self.buttons[0]["text"] = "O"
                        else:
                            self.buttons[1]["text"] = "O"
                    elif self.plays[3] == 54:
                        if self.buttons[0]["text"] != "X":
                            self.buttons[0]["text"] = "O"
                        else:
                            self.buttons[1]["text"] = "O"
                    elif self.plays[3] == 55:
                        if self.buttons[4]["text"] != "X":
                            self.buttons[4]["text"] = "O"
                        else:
                            self.buttons[7]["text"] = "O"
                    elif self.plays[3] == 57:
                        if self.buttons[6]["text"] != "X":
                            self.buttons[6]["text"] = "O"
                        elif self.buttons[7]["text"] != "X":
                            self.buttons[7]["text"] = "O"
                        elif self.buttons[8]["text"] != "X":
                            self.buttons[8]["text"] = "O"
                    elif self.plays[3] == 58:
                        if self.buttons[1]["text"] != "X":
                            self.buttons[1]["text"] = "O"
                        else:
                            self.buttons[7]["text"] = "O"
                    elif self.plays[3] == 59:
                        if self.buttons[6]["text"] != "X":
                            self.buttons[6]["text"] = "O"
                        elif self.buttons[7]["text"] != "X":
                            self.buttons[7]["text"] = "O"
                        elif self.buttons[8]["text"] != "X":
                            self.buttons[8]["text"] = "O"
                    elif self.plays[3] == 60:
                        if self.buttons[8]["text"] != "X":
                            self.buttons[8]["text"] = "O"
                        else:
                            self.buttons[0]["text"] = "O"
                    elif self.plays[3] == 61:
                        if self.buttons[0]["text"] != "X":
                            self.buttons[0]["text"] = "O"
                        else:
                            self.buttons[8]["text"] = "O"
                    elif self.plays[3] == 62:
                        if self.buttons[0]["text"] != "X":
                            self.buttons[0]["text"] = "O"
                        else:
                            self.buttons[8]["text"] = "O"
                    elif self.plays[3] == 63:
                        if self.buttons[1]["text"] != "X":
                            self.buttons[1]["text"] = "O"
                        else:
                            self.buttons[6]["text"] = "O"
                    elif self.plays[3] == 64:
                        if self.buttons[1]["text"] != "X":
                            self.buttons[1]["text"] = "O"
                        else:
                            self.buttons[7]["text"] = "O"
                    elif self.plays[3] == 65:
                        if self.buttons[1]["text"] != "X":
                            self.buttons[1]["text"] = "O"
                        else:
                            self.buttons[6]["text"] = "O"
                    elif self.plays[3] == 66:
                        if self.buttons[6]["text"] != "X":
                            self.buttons[6]["text"] = "O"
                        else:
                            self.buttons[7]["text"] = "O"
                    elif self.plays[3] == 67:
                        if self.buttons[0]["text"] != "X":
                            self.buttons[0]["text"] = "O"
                        else:
                            self.buttons[4]["text"] = "O"
                    elif self.plays[3] == 68:
                        if self.buttons[0]["text"] != "X":
                            self.buttons[0]["text"] = "O"
                        else:
                            self.buttons[4]["text"] = "O"
                    elif self.plays[3] == 69:
                        if self.buttons[6]["text"] != "X":
                            self.buttons[6]["text"] = "O"
                        elif self.buttons[3]["text"] != "X":
                            self.buttons[3]["text"] = "O"
                        elif self.buttons[0]["text"] != "X":
                            self.buttons[0]["text"] = "O"
                    elif self.plays[3] == 70:
                        if self.buttons[8]["text"] != "X":
                            self.buttons[8]["text"] = "O"
                        else:
                            self.buttons[0]["text"] = "O"
                    elif self.plays[3] == 71:
                        if self.buttons[6]["text"] != "X":
                            self.buttons[6]["text"] = "O"
                        elif self.buttons[3]["text"] != "X":
                            self.buttons[3]["text"] = "O"
                        elif self.buttons[0]["text"] != "X":
                            self.buttons[0]["text"] = "O"
                    elif self.plays[3] == 72:
                        if self.buttons[5]["text"] != "X":
                            self.buttons[5]["text"] = "O"
                        else:
                            self.buttons[3]["text"] = "O"
                    elif self.plays[3] == 73:
                        if self.buttons[5]["text"] != "X":
                            self.buttons[5]["text"] = "O"
                        else:
                            self.buttons[6]["text"] = "O"
                    elif self.plays[3] == 74:
                        if self.buttons[3]["text"] != "X":
                            self.buttons[3]["text"] = "O"
                        else:
                            self.buttons[6]["text"] = "O"
                    elif self.plays[3] == 75:
                        if self.buttons[8]["text"] != "X":
                            self.buttons[8]["text"] = "O"
                        else:
                            self.buttons[4]["text"] = "O"
                    elif self.plays[3] == 76:
                        if self.buttons[8]["text"] != "X":
                            self.buttons[8]["text"] = "O"
                        else:
                            self.buttons[4]["text"] = "O"
                    elif self.plays[3] == 77:
                        if self.buttons[2]["text"] != "X":
                            self.buttons[2]["text"] = "O"
                        elif self.buttons[5]["text"] != "X":
                            self.buttons[5]["text"] = "O"
                        elif self.buttons[8]["text"] != "X":
                            self.buttons[8]["text"] = "O"
                    elif self.plays[3] == 78:
                        if self.buttons[2]["text"] != "X":
                            self.buttons[2]["text"] = "O"
                        else:
                            self.buttons[6]["text"] = "O"
                    elif self.plays[3] == 79:
                        if self.buttons[2]["text"] != "X":
                            self.buttons[2]["text"] = "O"
                        elif self.buttons[5]["text"] != "X":
                            self.buttons[5]["text"] = "O"
                        elif self.buttons[8]["text"] != "X":
                            self.buttons[8]["text"] = "O"
                    elif self.plays[3] == 80:
                        if self.buttons[5]["text"] != "X":
                            self.buttons[5]["text"] = "O"
                        else:
                            self.buttons[3]["text"] = "O"
                    elif self.plays[3] == 81:
                        if self.buttons[8]["text"] != "X":
                            self.buttons[8]["text"] = "O"
                        else:
                            self.buttons[3]["text"] = "O"
                    elif self.plays[3] == 82:
                        if self.buttons[8]["text"] != "X":
                            self.buttons[8]["text"] = "O"
                        else:
                            self.buttons[5]["text"] = "O"
                    elif self.plays[3] == 83:
                        if self.buttons[4]["text"] != "X":
                            self.buttons[4]["text"] = "O"
                        else:
                            self.buttons[6]["text"] = "O"
                    elif self.plays[3] == 84:
                        if self.buttons[4]["text"] != "X":
                            self.buttons[4]["text"] = "O"
                        else:
                            self.buttons[6]["text"] = "O"
                    elif self.plays[3] == 85:
                        if self.buttons[8]["text"] != "X":
                            self.buttons[8]["text"] = "O"
                        else:
                            self.buttons[3]["text"] = "O"
                    elif self.plays[3] == 86:
                        if self.buttons[5]["text"] != "X":
                            self.buttons[5]["text"] = "O"
                        else:
                            self.buttons[3]["text"] = "O"
                    elif self.plays[3] == 87:
                        if self.buttons[6]["text"] != "X":
                            self.buttons[6]["text"] = "O"
                        else:
                            self.buttons[2]["text"] = "O"
                    elif self.plays[3] == 88:
                        if self.buttons[2]["text"] != "X":
                            self.buttons[2]["text"] = "O"
                        else:
                            self.buttons[6]["text"] = "O"
                    elif self.plays[3] == 89:
                        if self.buttons[2]["text"] != "X":
                            self.buttons[2]["text"] = "O"
                        elif self.buttons[0]["text"] != "X":
                            self.buttons[0]["text"] = "O"
                        elif self.buttons[1]["text"] != "X":
                            self.buttons[1]["text"] = "O"
                    elif self.plays[3] == 90:
                        if self.buttons[8]["text"] != "X":
                            self.buttons[8]["text"] = "O"
                        else:
                            self.buttons[0]["text"] = "O"
                    elif self.plays[3] == 91:
                        if self.buttons[2]["text"] != "X":
                            self.buttons[2]["text"] = "O"
                        elif self.buttons[0]["text"] != "X":
                            self.buttons[0]["text"] = "O"
                        elif self.buttons[1]["text"] != "X":
                            self.buttons[1]["text"] = "O"
                    elif self.plays[3] == 92:
                        if self.buttons[1]["text"] != "X":
                            self.buttons[1]["text"] = "O"
                        else:
                            self.buttons[7]["text"] = "O"
                    elif self.plays[3] == 93:
                        if self.buttons[2]["text"] != "X":
                            self.buttons[2]["text"] = "O"
                        else:
                            self.buttons[7]["text"] = "O"
                    elif self.plays[3] == 94:
                        if self.buttons[2]["text"] != "X":
                            self.buttons[2]["text"] = "O"
                        else:
                            self.buttons[1]["text"] = "O"
                    elif self.plays[3] == 95:
                        if self.buttons[4]["text"] != "X":
                            self.buttons[4]["text"] = "O"
                        else:
                            self.buttons[8]["text"] = "O"
                    elif self.plays[3] == 96:
                        if self.buttons[8]["text"] != "X":
                            self.buttons[8]["text"] = "O"
                        else:
                            self.buttons[4]["text"] = "O"
                    elif self.plays[3] == 97:
                        if self.buttons[6]["text"] != "X":
                            self.buttons[6]["text"] = "O"
                        elif self.buttons[7]["text"] != "X":
                            self.buttons[7]["text"] = "O"
                        elif self.buttons[8]["text"] != "X":
                            self.buttons[8]["text"] = "O"
                    elif self.plays[3] == 98:
                        if self.buttons[2]["text"] != "X":
                            self.buttons[2]["text"] = "O"
                        else:
                            self.buttons[6]["text"] = "O"
                    elif self.plays[3] == 99:
                        if self.buttons[6]["text"] != "X":
                            self.buttons[6]["text"] = "O"
                        elif self.buttons[7]["text"] != "X":
                            self.buttons[7]["text"] = "O"
                        elif self.buttons[8]["text"] != "X":
                            self.buttons[8]["text"] = "O"
                    elif self.plays[3] == 100:
                        if self.buttons[1]["text"] != "X":
                            self.buttons[1]["text"] = "O"
                        else:
                            self.buttons[7]["text"] = "O"
                    elif self.plays[3] == 101:
                        if self.buttons[1]["text"] != "X":
                            self.buttons[1]["text"] = "O"
                        else:
                            self.buttons[7]["text"] = "O"
                    elif self.plays[3] == 102:
                        if self.buttons[1]["text"] != "X":
                            self.buttons[1]["text"] = "O"
                        else:
                            self.buttons[8]["text"] = "O"
                    elif self.plays[3] == 103:
                        if self.buttons[2]["text"] != "X":
                            self.buttons[2]["text"] = "O"
                        else:
                            self.buttons[6]["text"] = "O"
                    elif self.plays[3] == 104:
                        if self.buttons[2]["text"] != "X":
                            self.buttons[2]["text"] = "O"
                        else:
                            self.buttons[6]["text"] = "O"
                    elif self.plays[3] == 105:
                        if self.buttons[8]["text"] != "X":
                            self.buttons[8]["text"] = "O"
                        else:
                            self.buttons[2]["text"] = "O"
                    elif self.plays[3] == 106:
                        if self.buttons[8]["text"] != "X":
                            self.buttons[8]["text"] = "O"
                        else:
                            self.buttons[6]["text"] = "O"
                    elif self.plays[3] == 107:
                        if self.buttons[2]["text"] != "X":
                            self.buttons[2]["text"] = "O"
                        else:
                            self.buttons[4]["text"] = "O"
                    elif self.plays[3] == 108:
                        if self.buttons[2]["text"] != "X":
                            self.buttons[2]["text"] = "O"
                        else:
                            self.buttons[4]["text"] = "O"
                    elif self.plays[3] == 109:
                        if self.buttons[5]["text"] != "X":
                            self.buttons[5]["text"] = "O"
                        else:
                            self.buttons[3]["text"] = "O"
                    elif self.plays[3] == 110:
                        if self.buttons[3]["text"] != "X":
                            self.buttons[3]["text"] = "O"
                        else:
                            self.buttons[5]["text"] = "O"
                    elif self.plays[3] == 111:
                        if self.buttons[8]["text"] != "X":
                            self.buttons[8]["text"] = "O"
                        else:
                            self.buttons[0]["text"] = "O"
                    elif self.plays[3] == 112:
                        if self.buttons[8]["text"] != "X":
                            self.buttons[8]["text"] = "O"
                        else:
                            self.buttons[0]["text"] = "O"
                    elif self.plays[3] == 113:
                        if self.buttons[8]["text"] != "X":
                            self.buttons[8]["text"] = "O"
                        else:
                            self.buttons[0]["text"] = "O"
                    elif self.plays[3] == 114:
                        if self.buttons[2]["text"] != "X":
                            self.buttons[2]["text"] = "O"
                        else:
                            self.buttons[7]["text"] = "O"
                    elif self.plays[3] == 115:
                        if self.buttons[2]["text"] != "X":
                            self.buttons[2]["text"] = "O"
                        else:
                            self.buttons[7]["text"] = "O"
                    elif self.plays[3] == 116:
                        if self.buttons[7]["text"] != "X":
                            self.buttons[7]["text"] = "O"
                        else:
                            self.buttons[1]["text"] = "O"
                    elif self.plays[3] == 117:
                        if self.buttons[0]["text"] != "X":
                            self.buttons[0]["text"] = "O"
                        else:
                            self.buttons[8]["text"] = "O"
                    elif self.plays[3] == 118:
                        if self.buttons[0]["text"] != "X":
                            self.buttons[0]["text"] = "O"
                        else:
                            self.buttons[8]["text"] = "O"
                    elif self.plays[3] == 119:
                        if self.buttons[0]["text"] != "X":
                            self.buttons[0]["text"] = "O"
                        else:
                            self.buttons[8]["text"] = "O"
                    elif self.plays[3] == 120:
                        if self.buttons[3]["text"] != "X":
                            self.buttons[3]["text"] = "O"
                        else:
                            self.buttons[5]["text"] = "O"
                    elif self.plays[3] == 121:
                        if self.buttons[3]["text"] != "X":
                            self.buttons[3]["text"] = "O"
                        else:
                            self.buttons[2]["text"] = "O"
                    elif self.plays[3] == 122:
                        if self.buttons[1]["text"] != "X":
                            self.buttons[1]["text"] = "O"
                        else:
                            self.buttons[7]["text"] = "O"
                    elif self.plays[3] == 123:
                        if self.buttons[3]["text"] != "X":
                            self.buttons[3]["text"] = "O"
                        else:
                            self.buttons[5]["text"] = "O"
                    elif self.plays[3] == 124:
                        if self.buttons[3]["text"] != "X":
                            self.buttons[3]["text"] = "O"
                        else:
                            self.buttons[5]["text"] = "O"
                    elif self.plays[3] == 125:
                        if self.buttons[1]["text"] != "X":
                            self.buttons[1]["text"] = "O"
                        else:
                            self.buttons[7]["text"] = "O"
                    elif self.plays[3] == 126:
                        if self.buttons[3]["text"] != "X":
                            self.buttons[3]["text"] = "O"
                        else:
                            self.buttons[5]["text"] = "O"
                    elif self.plays[3] == 127:
                        if self.buttons[1]["text"] != "X":
                            self.buttons[1]["text"] = "O"
                        else:
                            self.buttons[7]["text"] = "O"
                    self.plays[0] += 1
                    self.click = True
                    self.check()
                else:
                    x = randint(0, 8)
                    while self.buttons[x]["text"] != " ":
                        x = randint(0, 8)
                    self.buttons[x]["text"] = "O"
                    self.plays[0] += 1
                    self.click = True
                    self.check()


root = Tk()
root.title("Tic_Tac_Toe")
root.configure(bg="black")
root.geometry("460x250")

app = T(root)

root.mainloop()
