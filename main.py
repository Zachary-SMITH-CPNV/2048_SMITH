# 2048 V03
# Author : Zachary Smith
# Classe : SC-C1a
# Last modification: 16.03.2023

# Modules imported
from tkinter import *
import tkinter.font
import random
from tkinter import messagebox


# Fonction for number combining
def mix(list, rev):
    # Delete zero
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
        totalnumbers = 4 - len(list)
        while totalnumbers != 0:
            totalnumbers -= 1
            list.insert(0, 0)
    else:
        while len(list) < 4:
            list.append(0)
    return list


# -------------------------------------------------------------------------------
# Variable for movement
nb_movement = 0


# function for movements, left,right,uo,down,

def click_on_letter(event):
    global nb_movement
    if event.keysym == 'Left' or event.keysym == 'a':
        prev_positions_value = [row[:] for row in grid_2048]
        for line in range(len(grid_2048)):
            grid_2048[line] = mix(grid_2048[line], False)
        objrefresh()
        if grid_2048 != prev_positions_value:
            generate_random_value()
        else:
            table_state()
        print('you clicked left')
        nb_movement += 1

    if event.keysym == 'Right' or event.keysym == 'd':
        prev_positions_value = [row[:] for row in grid_2048]
        for line in range(len(grid_2048)):
            grid_2048[line] = mix(grid_2048[line], True)
        objrefresh()
        if grid_2048 != prev_positions_value:
            generate_random_value()
        else:
            table_state()
        print('you clicked right')
        nb_movement += 1

    if event.keysym == 'w' or event.keysym == 'Up':
        prev_positions_value = [row[:] for row in grid_2048]
        for col in range(len(grid_2048)):
            column = [grid_2048[row][col] for row in range(len(grid_2048))]
            mixed_column = mix(column, False)
            for row in range(len(grid_2048)):
                grid_2048[row][col] = mixed_column[row]
        objrefresh()
        if grid_2048 != prev_positions_value:
            generate_random_value()
        else:
            table_state()
        print('you clicked up')
        nb_movement += 1

    if event.keysym == 's' or event.keysym == 'Down':
        prev_positions_value = [row[:] for row in grid_2048]
        for col in range(len(grid_2048)):
            column = [grid_2048[row][col] for row in range(len(grid_2048))]
            reversed_column = column[::-1]
            mixed_column = mix(reversed_column, False)
            for row in range(len(grid_2048)):
                grid_2048[row][col] = mixed_column[::-1][row]
        objrefresh()
        if grid_2048 != prev_positions_value:
            generate_random_value()
        else:
            table_state()
        print('you clicked on down')
        nb_movement += 1

    score_affichage.config(text=f" Voici le nombre de mouvement {nb_movement}")


# Mouvement checker
def movement_checker():
    for row in range(4):
        for col in range(4):
            if grid_2048[row][col] == 0:
                return True
            if row < 4 - 1 and grid_2048[row][col] == grid_2048[row+1][col]:
                return True
            if col < 4 - 1 and grid_2048[row][col] == grid_2048[row][col+1]:
                return True
    return False


# Refresh grid
def objrefresh():
    for line in range(len(grid_2048)):
        for col in range(len(grid_2048[line])):
            # creation of each label without placing it
            if grid_2048[line][col] != 0:
                labels[line][col].config(text=grid_2048[line][col], bg=numbers_color[int(grid_2048[line][col])])
            elif grid_2048[line][col] == 4096:
                labels[line][col].config(text="2048", bg='pink')
            else:
                labels[line][col].config(text="", bg='#e6e6f1')

# Win, lose function for game


def table_state():
    empty_positions = []
    for i in range(4):
        if 2048 in grid_2048[i]:
            answer = messagebox.askquestion(title="Felicitation !", message="T'as gagné ! On recommence ?")
            print(answer)
            if answer == "yes":
                reset_game()
            else: quit()
            return "Other"
        for j in range(4):
            if grid_2048[i][j] == 0:
                empty_positions.append((i, j))
    if len(empty_positions) == 0:
        # Test if possible to move
        moveable = movement_checker()
        if moveable:
            return "Other"
        else:
            answer = messagebox.askquestion(title="Tu as perdus", message="Veux tu recommencer ?")
            if answer == "yes":
                reset_game()
                objrefresh()
            else: quit()
            return "Other"
    else:
        return "Space"


# Random number generator
def generate_random_value():
    while True:
        random_pos_row, random_pos_col = random.randint(0, len(grid_2048) - 1), random.randint(0, len(grid_2048[0]) - 1)
        state = table_state()
        if state == "Space":
            if grid_2048[random_pos_row][random_pos_col] == 0:
                grid_2048[random_pos_row][random_pos_col] = random.randint(1, 2) * 2
                objrefresh()  # Go to "position refresh" function
                break
            else:
                pass
        else:
            break


# Restart game, buton
def reset_game():
    global grid_2048
    grid_2048 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    generate_random_value()
    objrefresh()


# -------------------------------------------------------------------------------


# window size
window_width = 800
window_height = 800
window = Tk()
window.geometry(f"{window_width}x{window_height}")
window.title("2048 By SMITH Zachary | V0.2")
window.bind('<Key>', click_on_letter)

main_window = Frame(window)
main_window.pack()

top_frame = Frame(main_window)
top_frame.pack()

middle_frame = Frame(main_window)
middle_frame.pack()

score_affichage = Label(top_frame, text=f" Voici le nombre de mouvement {nb_movement}", width=30, height=15)
score_affichage.grid(row=0, column=0)

# Defining center of screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# centering window on screen
x_left = int(screen_width / 2 - window_width / 2)
y_top = int(screen_height / 2 - window_height / 2)
#
window.geometry("+{}+{}".format(x_left, y_top))

# Variable for base of window

grid_2048 = [[1024, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
labels = [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
# Dictionary for colors

numbers_color = {2: '#e8ffff', 4: '#d9f1ff', 8: '#bfe6ff', 16: '#8cd3ff', 32: '#59bfff', 64: '#26abff', 128: '#0da2ff',
                 256: '#009dff', 512: '#405db8', 1024: '#36358f', 2048: '#1034a6'}

# window 2048

if __name__ == '__main__':
    if __name__ == '__main__':
        for line in range(len(grid_2048)):
            for col in range(len(grid_2048[line])):
                # creation of each label without placing it
                if grid_2048[line][col] != 0:
                    labels[line][col] = tkinter.Label(middle_frame, text=grid_2048[line][col], width=10, height=5, borderwidth=1,
                                                      relief="solid",
                                                      font=("Arial", 12), bg='#e6e6f1')
                elif grid_2048[line][col] == 4096:
                    labels[line][col] = tkinter.Label(middle_frame, text="2048", width=10, height=25, borderwidth=5,
                                                      relief="solid",
                                                      font=("Arial", 16), bg=numbers_color[int(grid_2048[line][col])])
                else:
                    labels[line][col] = tkinter.Label(middle_frame, text="", width=10, height=5, borderwidth=1, relief="solid",
                                                      font=("Arial", 12), bg='#e6e6f1')
                # we set the label in the windows with a virtual grid
                labels[line][col].grid(row=line + 1, column=col)
    i = 2
    while i != 0:
        i -= 1
        generate_random_value()
    objrefresh()

window.bind('<Key>', click_on_letter)

window.mainloop()
