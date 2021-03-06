from tkinter import *


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


    # * Main code
gb = {"start": [1, 2, 3, 4, 5, 6, 7, 8, 9],
      "row": {},
      "column": {},
      "square": {},
      "entire": ["--Undefined--"]}

# Make tkinter
root = Tk()

# Create data base function
create_rcs()

# Create varibles function
varible_row()
varible_column()
varible_square()
