from tkinter import *
from tkinter.ttk import Style, Button
import random


def create_rcs():
    # Creates list where varibles will be stored
    # rcs stands for row, column, square
    for i in range(1, 10):
        gb["row"]["r{}".format(i)] = []
        gb["column"]["c{}".format(i)] = []

    for i in range(1, 10):
        gb["square"]["s{}".format(i)] = []


def varible_row():
    row = 1
    for i in range(1, 82):
        gb["row"]["r{}".format(row)].append(
            StringVar(root, name="{}".format(i)))

        if i % 9 == 0:
            row += 1


def varible_column():
    column = 1
    for i in range(1, 82):
        if column == 10:
            column = 1

        gb["column"]["c{}".format(column)].append(
            StringVar(root, name="{}".format(i)))
        column += 1


def varible_square():
    square = 1
    inside = 1
    endless = 1
    rerun = 0

    for i in range(1, 82):
        gb["square"]["s{}".format(square)].append(
            StringVar(root, name="{}".format(i)))

        if rerun == 2 and endless == 9:
            rerun = 0
            inside = 0
            endless = 0
            square += 1

        elif endless == 9:
            square -= 2
            inside = 0
            endless = 0
            rerun += 1

        # * Works
        elif inside == 3:
            square += 1
            inside = 0

        inside += 1
        endless += 1


def gen():
    # Generates first row
    random.shuffle(gb["start"])
    for i in range(0, 9):
        root.setvar(name="{}".format(i+1), value="{}".format(gb["start"][i]))

    # Generates the rest
    for name in range(10, 82):
        temp_r = []
        temp_c = []
        temp_s = []

        # TODO Improve here in the loop where everthing is the same
        # TODO Make a range 3 loop and just toggle between r,c,s
        # Temp_r values
        for i in range(1, 10):
            for z in gb["row"]["r{}".format(i)]:
                if str(name) == str(z):
                    for x in range(0, 9):

                        if gb["row"]["r{}".format(i)][x].get() in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                            temp_r.append(
                                int(gb["row"]["r{}".format(i)][x].get()))
                        else:
                            temp_r.append(
                                gb["row"]["r{}".format(i)][x].get())

        # Temp_c values
        for i in range(1, 10):
            for z in gb["column"]["c{}".format(i)]:
                if str(name) == str(z):
                    for x in range(0, 9):

                        if gb["column"]["c{}".format(i)][x].get() in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                            temp_c.append(
                                int(gb["column"]["c{}".format(i)][x].get()))
                        else:
                            temp_c.append(
                                gb["column"]["c{}".format(i)][x].get())

        # Temp_s values
        for i in range(1, 10):
            for z in gb["square"]["s{}".format(i)]:
                if str(name) == str(z):
                    for x in range(0, 9):

                        if gb["square"]["s{}".format(i)][x].get() in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                            temp_s.append(
                                int(gb["square"]["s{}".format(i)][x].get()))

                        else:
                            temp_s.append(
                                gb["square"]["s{}".format(i)][x].get())

        #! Not random, makes it not work
        for i in range(1, 10):
            num = i
            row = True
            coll = True
            sqr = True

            if num in temp_r:
                row = False

            if num in temp_c:
                coll = False

            if num in temp_s:
                sqr = False

            if row == True and coll == True and sqr == True:
                root.setvar(name="{}".format(name), value="{}".format(num))

                temp_r = []
                temp_c = []
                temp_s = []
                break


def gameboard():
    row = 0
    column = 0
    for i in range(1, 82):
        button = Button(root, text=root.getvar(
            "{}".format(i)), style="TButton")
        button.grid(row=row, column=column)

        column += 1
        if i % 9 == 0:
            column = 0
            row += 1


# Data base
gb = {"start": [1, 2, 3, 4, 5, 6, 7, 8, 9],
      "row": {},
      "column": {},
      "square": {},
      "entire": ["--Undefined--"]}

# Make tkinter
root = Tk()
root.title("9x9")
root.geometry("450x350")

# Style
style = Style()
style.configure("TButton", font=("calibri", 15, "bold"), height=10, width=3)

# Create data base function
create_rcs()

# Create varibles function
varible_row()
varible_column()
varible_square()


# Generate the entire board
gen()


# Makes gameboard with varibels
gameboard()

root.mainloop()
