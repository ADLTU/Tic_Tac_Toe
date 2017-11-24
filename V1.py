from tkinter import *
from tkinter import messagebox
from tkinter import font
from random import randint


class T(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.configure(bg="black")
        self.grid()
        self.Start_message = Label(self, text="Hello Tkinter!", fg="light grey")
        self.Start_message.grid(row=0, column=3)
        self.Start_message.configure(bg="black")
        self.message = Label(self, text=" ")
        self.message.grid(row=1, column=2)
        self.message.configure(bg="black")
        self.click = True  # Start with X
        self.buttons = []
        self.font = font.Font(family="Helvetica", size=9, weight="bold")
        self.plays = [0, 0, 0]
        # creating all the buttons
        for i in range(2, 5):
            for j in range(2, 5):
                self.buttons.append(self.create_buttons(i, j))

    def create_buttons(self, x, y):
        button = Button(self, height=3, width=20, fg="black", command=lambda: self.hard_play(button))
        button["text"] = " "
        button["font"] = self.font
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
                    elif self.buttons[7]["text"] == "X" or self.buttons[5]["text"] == "X":
                        self.buttons[8]["text"] = "O"
                        self.plays[1] = 2
                    elif self.buttons[1]["text"] == "X" or self.buttons[3]["text"] == "X":
                        self.buttons[0]["text"] = "O"
                        self.plays[1] = 3
                    elif self.buttons[4]["text"] == "X":
                        self.buttons[6]["text"] = "O"
                        self.plays[1] = 4
                    self.plays[0] += 1
                    self.click = True
                elif self.plays[0] == 1 and self.plays[1] == 1:
                    if self.buttons[0]["text"] == "X":
                        if self.buttons[1]["text"] == "X":
                            self.buttons[2]["text"] = "O"
                        elif self.buttons[2]["text"] == "X":
                            self.buttons[1]["text"] = "O"
                        elif self.buttons[3]["text"] == "X":
                            self.buttons[6]["text"] = "O"
                        elif self.buttons[6]["text"] == "X":
                            self.buttons[3]["text"] = "O"
                        elif self.buttons[5]["text"] == "X":
                            self.buttons[7]["text"] = "O"
                        elif self.buttons[7]["text"] == "X":
                            self.buttons[5]["text"] = "O"
                        else:
                            self.buttons[5]["text"] = "O"
                    if self.buttons[2]["text"] == "X":
                        if self.buttons[1]["text"] == "X":
                            self.buttons[0]["text"] = "O"
                        elif self.buttons[0]["text"] == "X":
                            self.buttons[1]["text"] = "O"
                        elif self.buttons[3]["text"] == "X":
                            self.buttons[7]["text"] = "O"
                        elif self.buttons[7]["text"] == "X":
                            self.buttons[3]["text"] = "O"
                        elif self.buttons[8]["text"] == "X":
                            self.buttons[5]["text"] = "O"
                        elif self.buttons[5]["text"] == "X":
                            self.buttons[8]["text"] = "O"
                        else:
                            self.buttons[3]["text"] = "O"
                    if self.buttons[6]["text"] == "X":
                        if self.buttons[3]["text"] == "X":
                            self.buttons[0]["text"] = "O"
                        elif self.buttons[0]["text"] == "X":
                            self.buttons[3]["text"] = "O"
                        elif self.buttons[8]["text"] == "X":
                            self.buttons[7]["text"] = "O"
                        elif self.buttons[7]["text"] == "X":
                            self.buttons[8]["text"] = "O"
                        elif self.buttons[1]["text"] == "X":
                            self.buttons[5]["text"] = "O"
                        elif self.buttons[5]["text"] == "X":
                            self.buttons[1]["text"] = "O"
                        else:
                            self.buttons[3]["text"] = "O"
                    if self.buttons[8]["text"] == "X":
                        if self.buttons[2]["text"] == "X":
                            self.buttons[5]["text"] = "O"
                        elif self.buttons[5]["text"] == "X":
                            self.buttons[2]["text"] = "O"
                        elif self.buttons[6]["text"] == "X":
                            self.buttons[7]["text"] = "O"
                        elif self.buttons[7]["text"] == "X":
                            self.buttons[6]["text"] = "O"
                        elif self.buttons[1]["text"] == "X":
                            self.buttons[3]["text"] = "O"
                        elif self.buttons[3]["text"] == "X":
                            self.buttons[1]["text"] = "O"
                        else:
                            self.buttons[5]["text"] = "O"
                    self.plays[0] += 1
                    self.click = True
                elif self.plays[0] == 1 and self.plays[1] == 2:
                    if self.buttons[7]["text"] == "X":
                        if self.buttons[5]["text"] == "X" or self.buttons[1]["text"] == "X" \
                                or self.buttons[2]["text"] == "X":
                            self.buttons[4]["text"] = "O"
                        elif self.buttons[4]["text"] == "X" or self.buttons[0]["text"] == "X":
                            self.buttons[1]["text"] = "O"
                        elif self.buttons[6]["text"] == "X":
                            self.buttons[5]["text"] = "O"
                        else:
                            self.buttons[2]["text"] = "O"
                    if self.buttons[5]["text"] == "X":
                        if self.buttons[7]["text"] == "X" or self.buttons[6]["text"] == "X" \
                                or self.buttons[3]["text"] == "X":
                            self.buttons[4]["text"] = "O"
                        elif self.buttons[4]["text"] == "X" or self.buttons[0]["text"] == "X":
                            self.buttons[3]["text"] = "O"
                        elif self.buttons[1]["text"] == "X":
                            self.buttons[6]["text"] = "O"
                        else:
                            self.buttons[7]["text"] = "O"
                    self.plays[0] += 1
                    self.click = True
                elif self.plays[0] == 1 and self.plays[1] == 3:
                    if self.buttons[1]["text"] == "X":
                        if self.buttons[3]["text"] == "X" or self.buttons[6]["text"] == "X" \
                                or self.buttons[7]["text"] == "X":
                            self.buttons[4]["text"] = "O"
                        elif self.buttons[4]["text"] == "X" or self.buttons[8]["text"] == "X":
                            self.buttons[7]["text"] = "O"
                        elif self.buttons[2]["text"] == "X":
                            self.buttons[3]["text"] = "O"
                        else:
                            self.buttons[6]["text"] = "O"
                    elif self.buttons[3]["text"] == "X":
                        if self.buttons[1]["text"] == "X" or self.buttons[2]["text"] == "X" \
                                or self.buttons[5]["text"] == "X":
                            self.buttons[4]["text"] = "O"
                        elif self.buttons[4]["text"] == "X" or self.buttons[8]["text"] == "X":
                            self.buttons[5]["text"] = "O"
                        elif self.buttons[7]["text"] == "X":
                            self.buttons[2]["text"] = "O"
                        else:
                            self.buttons[1]["text"] = "O"
                    self.plays[0] += 1
                    self.click = True
                elif self.plays[0] == 1 and self.plays[1] == 4:
                    if self.buttons[0]["text"] == "X":
                        self.buttons[8]["text"] = "O"
                    elif self.buttons[1]["text"] == "X":
                        self.buttons[7]["text"] = "O"
                    elif self.buttons[3]["text"] == "X":
                        self.buttons[5]["text"] = "O"
                    elif self.buttons[5]["text"] == "X":
                        self.buttons[3]["text"] = "O"
                    elif self.buttons[7]["text"] == "X":
                        self.buttons[1]["text"] = "O"
                    elif self.buttons[8]["text"] == "X":
                        self.buttons[0]["text"] = "O"
                    else:
                        self.buttons[8]["text"] = "O"
                    self.plays[0] += 1
                    self.click = True
                else:
                    x = randint(0, 8)
                    while self.buttons[x]["text"] != " ":
                        x = randint(0, 8)
                    self.buttons[x]["text"] = "O"
                    self.click = True
                    self.check()


root = Tk()
root.title("Tic_Tac_Toe")
root.configure(bg="black")
root.geometry("450x250")

app = T(root)

root.mainloop()
