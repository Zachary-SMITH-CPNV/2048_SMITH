# 2048 V03
# Author : Zachary Smith
# Classe : SC-C1a
# Last modification: 16.03.2023

# Modules imported
from tkinter import *
import tkinter.font
import random


# Fonction for number combining
def Mix(list, rev):
    # Si il y à un 0
    for obj in list:
        if 0 in list:
            list.remove(0)
    for obj in range(len(list) - 1):
        if list[obj] == list[obj + 1]:
            list[obj] += list[obj + 1]
            list[obj + 1] = 0
    for obj in list:
        if 0 in list:
            list.remove(0)
    if rev:
        totalnumbers = 4 -len(list)
        while totalnumbers != 0:
            totalnumbers -= 1
            list.insert(0,0)
    else:
        while len(list) < 4:
            list.append(0)
    return list


# -------------------------------------------------------------------------------
# Variable for movement
nb_movement = 0

def click_on_letter(event):
    global nb_movement
    # Variable for movements
    if event.keysym == 'Left'or event.keysym == 'a':
        for line in range(len(grid_2048)):
            grid_2048[line] = Mix(grid_2048[line], False)
        objRefresh()
        print('you clicked left')
        nb_movement += 1


    if event.keysym == 'Right' or event.keysym == 'd':
        for line in range(len(grid_2048)):
            grid_2048[line] = Mix(grid_2048[line],True)
        objRefresh()
        print('you clicked right')
        nb_movement += 1


    if event.keysym == 'w' or event.keysym == 'Up':
        for col in range(len(grid_2048)):
            column = [grid_2048[row][col] for row in range(len(grid_2048))]
            mixed_column = Mix(column, False)
            for row in range(len(grid_2048)):
                grid_2048[row][col] = mixed_column[row]
        objRefresh()
        print('you clicked up')
        nb_movement += 1



    if event.keysym == 's' or event.keysym == 'Down':
        for col in range(len(grid_2048)):
            column = [grid_2048[row][col] for row in range(len(grid_2048))]
            reversed_column = column[::-1]
            mixed_column = Mix(reversed_column, False)
            for row in range(len(grid_2048)):
                grid_2048[row][col] = mixed_column[::-1][row]

        nb_movement += 1
        objRefresh()
        print('you clicked on down')


    print(nb_movement)




# Random number générator




# -------------------------------------------------------------------------------
# window size
window_width = 800
window_height = 800
window = Tk()
window.geometry(f"{window_width}x{window_height}")
window.title("2048 By SMITH Zachary | V0.2")
window.bind('<Key>', click_on_letter)

# Defining center of screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# centering window on screen
x_left = int(screen_width/2 - window_width/2)
y_top = int(screen_height/2 - window_height/2)
#
window.geometry("+{}+{}".format(x_left, y_top))

# Variable for base of window

grid_2048= [[2, 4, 4, 16], [32, 64, 0, 256], [512, 1024, 2048, 0], [8, 0, 128, 0]]
labels = [[None, None, None, None], [None, None, None, None], [None, None, None, None],[None, None, None, None]]
# Dictionary for colors

numbers_color = {2:'#e8ffff', 4:'#d9f1ff', 8:'#bfe6ff',16:'#8cd3ff',32:'#59bfff',64:'#26abff',128:'#0da2ff',256:'#009dff',512:'#405db8', 1024: '#36358f', 2048:'#1034a6'}

# Start of window
if __name__ == '__main__':

# -------------------------------------------------------------------------------
# window 2048
    if __name__ == '__main__':
        def objRefresh():
            for line in range(len(grid_2048)):
                for col in range(len(grid_2048[line])):
                    # creation of each label without placing it
                    if grid_2048[line][col] != 0:
                        labels[line][col] = tkinter.Label(text=grid_2048[line][col], width=10, height=5, borderwidth=1, relief="solid",
                                                          font=("Arial", 12), bg='#e6e6f1')
                    else:
                        labels[line][col] = tkinter.Label(text="", width=10, height=5, borderwidth=1, relief="solid",
                                                          font=("Arial", 12), bg='#e6e6f1')
                    # we set the label in the windows with a virtual grid
                    labels[line][col].grid(row=line, column=col)
                    try:labels[line][col].config(bg=numbers_color[int(grid_2048[line][col])])
                    except:labels[line][col].config(bg='#e6e6f1')
        objRefresh()
window.bind('<Key>',click_on_letter)

window.mainloop()



