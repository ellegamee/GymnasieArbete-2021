from tkinter import *
from tkinter.ttk import Style, Button
import random

# TODO make import better, with out using star
# * Imports to many functions that are not needed


def create_database():
    # Creates list where varibles will be stored
    for index in range(1, 10):
        data["row"][f"r{index}"] = []
        data["column"][f"c{index}"] = []
        data["square"][f"s{index}"] = []

    row = 1
    column = 1
    square = 1
    for name in range(1, 82):
        data["row"][f"r{row}"].append(StringVar(root, name=f"{name}"))
        data["column"][f"c{column}"].append(StringVar(root, name=f"{name}"))
        data["square"][f"s{square}"].append(StringVar(root, name=f"{name}"))

        if name % 9 == 0:
            row += 1
            column = 0
            square = 1

            if row > 3 and not row > 6:
                square += 3

            if row > 6 and not row > 9:
                square += 6

        if column == 3 or column == 6:
            square += 1

        column += 1


def number_generator(seed):
    # Generates first row

    # random.Random(seed).shuffle(data["start"])
    random.shuffle(data["start"])
    for i in range(0, 9):
        var = data["start"][i]
        root.setvar(name=f"{i+1}", value=f"{var}")

    compare = []
    for item in data["start"]:
        compare.append(str(item))

    name = 10
    loop = True
    while loop:
        temp_r = []
        temp_c = []
        temp_s = []

        # TODO Fix better names for list's
        lst_sector = ["row", "column", "square"]
        lst_lst = [temp_r, temp_c, temp_s]
        lst_c = ["r", "c", "s"]
        for sector, lst, c in zip(lst_sector, lst_lst, lst_c):

            for i in range(9):
                subsector = c + str(i + 1)

                for z in data[sector][subsector]:
                    # TODO Take a look at that
                    if str(name) == str(z):
                        for obj in range(9):

                            if data[sector][subsector][obj].get() in compare:
                                lst.append(int(data[sector][subsector][obj].get()))

                            else:
                                lst.append(data[sector][subsector][obj].get())

        # random.Random(seed).shuffle(data["start"])
        random.shuffle(data["start"])
        for count, num in enumerate(data["start"]):

            # TODO Remove this and make it work with the next if inside
            check = True
            if num in temp_r or num in temp_c or num in temp_s:
                check = False

            if check == True:
                root.setvar(name=f"{name}", value=f"{num}")
                name += 1
                break

            if (count + 1) == 9:
                name = name - (count - 1)

                for i in range(9):
                    root.setvar(name=f"{name+i}", value="")
                break

        if name == 82:
            loop = False

    # * Makes copy of entire grid
    for obj in range(1, 82):
        data["entire"].append(root.getvar(f"{obj}"))


def gameboard():
    row = 0
    column = 0
    for i in range(1, 82):
        button = Button(root, text=root.getvar(f"{i}"), style="TButton")
        button.grid(row=row, column=column)

        column += 1
        if i % 9 == 0:
            column = 0
            row += 1


# Data base
data = {
    "row": {},
    "column": {},
    "square": {},
    "entire": [],
    "start": [1, 2, 3, 4, 5, 6, 7, 8, 9],
}

# Make tkinter
root = Tk()
root.title("9x9")
root.geometry("450x350")

# Style
style = Style()
style.configure("TButton", font=("calibri", 15, "bold"), height=10, width=3)

# Create data base
create_database()

# Generates board
# seed = input("Input a seed: ")
number_generator(seed)
print("done!")

# Makes gameboard with varibels
gameboard()

root.mainloop()
