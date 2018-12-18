import tkinter as tk
import numpy as np

N, M = 5, 5

grid = np.full((N, M), False)
squares = np.full((N, M), None)

def mouse_clicked(event):
    canvas = event.widget
    width = canvas.winfo_width()
    height = canvas.winfo_height()


    x = event.x
    y = event.y

    # i = int(x % N)
    # j = int(y % M)

    # print(i, j)
    # print(x,y)

    # grid[i][j] = not grid[i][j]

    x_length = width // N
    y_length = height // M

    canvas.itemconfig(canvas.find_closest(x - x_length, y-y_length)[0], fill='red')
    canvas.itemconfig(canvas.find_enclosed(x, y,x,y)[0], fill='blue')
    canvas.itemconfig(canvas.find_overlapping(x, y,x,y)[0], fill='green')



    # canvas.itemconfig(rect, fill='red')

    # canvas.itemconfig(tk.CURRENT, fill='red')
    # print(canvas.find_withtag(tk.CURRENT))
    # print(x, y)