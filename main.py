# 2048 V02
# Auteur : Zachary Smith
# Dernière modif: 24.02.2023

from tkinter import *
import tkinter.font


# Fonction pour tassage
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


# ------------------

def click_on_letter(event):
    if event.keysym == 'Left'or event.keysym == 'a':
        for line in range(len(grid_2048)):
            grid_2048[line] = Mix(grid_2048[line], False)
        objRefresh()
        print('you clicked left')

    if event.keysym == 'Right' or event.keysym == 'd':
        for line in range(len(grid_2048)):
            grid_2048[line] = Mix(grid_2048[line],True)
        objRefresh()
        print('you clicked right')

    if event.keysym == 'w' or event.keysym == 'Up':
        for col in range(len(grid_2048)):
            column = [grid_2048[row][col] for row in range(len(grid_2048))]
            mixed_column = Mix(column, False)
            for row in range(len(grid_2048)):
                grid_2048[row][col] = mixed_column[row]
        objRefresh()
        print('you clicked up')

    if event.keysym == 's' or event.keysym == 'Down':
        for col in range(len(grid_2048)):
            column = [grid_2048[row][col] for row in range(len(grid_2048))]
            reversed_column = column[::-1]
            mixed_column = Mix(reversed_column, False)
            for row in range(len(grid_2048)):
                grid_2048[row][col] = mixed_column[::-1][row]
        objRefresh()
        print('you clicked on down')


# Définir la fenêtre
window_width = 800
window_height = 800
window = Tk()
window.geometry(f"{window_width}x{window_height}")
window.title("2048 By SMITH Zachary | V0.2")
window.bind('<Key>', click_on_letter)

# Calcul de taille d'écran
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# centrer la fenêtre dans l'écran
x_left = int(screen_width/2 - window_width/2)
y_top = int(screen_height/2 - window_height/2)
#
window.geometry("+{}+{}".format(x_left, y_top))

# Variable pour fenêtre de base

grid_2048= [[2, 4, 4, 16], [32, 64, 0, 256], [512, 1024, 2048, 0], [8, 0, 128, 0]]
labels = [[None, None, None, None], [None, None, None, None], [None, None, None, None],[None, None, None, None]]
# Dictionnaire pour couleurs

numbers_color = {2:'#FFE599', 4:'#F9CB9C',8:'#F1C232',16:'#FFD966',32:'#FF9900',64:'#EA9999',128:'#CF2A27',256:'#990000',512:'#990000',1024:'blue',2048:'#FF00FF'}

# Lancement de la fenêtre
if __name__ == '__main__':


# Fenêtre 2048
    if __name__ == '__main__':
        def objRefresh():
            for line in range(len(grid_2048)):
                for col in range(len(grid_2048[line])):
                    # creation of each label without placing it
                    if grid_2048[line][col] != 0:
                        labels[line][col] = tkinter.Label(text=grid_2048[line][col], width=10, height=5, borderwidth=1, relief="solid",
                                                          font=("Arial", 12), bg="yellow")
                    else:
                        labels[line][col] = tkinter.Label(text="", width=10, height=5, borderwidth=1, relief="solid",
                                                          font=("Arial", 12), bg="yellow")
                    # we set the label in the windows with a virtual grid
                    labels[line][col].grid(row=line, column=col)
                    try:labels[line][col].config(bg=numbers_color[int(grid_2048[line][col])])
                    except:labels[line][col].config(bg="Yellow")
        objRefresh()
window.bind('<Key>',click_on_letter)

window.mainloop()



